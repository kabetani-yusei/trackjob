from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from datetime import datetime, timedelta

class CalendarAPI:
    def __init__(self):
        scopes = ['https://www.googleapis.com/auth/calendar']
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', scopes)
        creds = flow.run_local_server(port=0)
        self.service = build('calendar', 'v3', credentials=creds)

    def get_events(self):
        now_utc = datetime.utcnow()
        today_end_utc = now_utc.replace(hour=23, minute=59, second=59, microsecond=0)
        weekday = now_utc.weekday()
        one_week_ago_utc = (now_utc - timedelta(days=6)).replace(hour=0, minute=0, second=0, microsecond=0)

        one_week_ago_utc_iso = one_week_ago_utc.isoformat() + 'Z'
        today_end_utc_iso = today_end_utc.isoformat() + 'Z'

        # イベントを取得
        events_result = self.service.events().list(
            calendarId='primary',
            timeMin=one_week_ago_utc_iso,
            timeMax=today_end_utc_iso,
            singleEvents=True,
            orderBy='startTime'
        ).execute()

        events = events_result.get('items', [])
        event_list = []

        for event in events:
            # イベント情報をリストに追加
            event_info = {
                'id': event['id'],
                'summary': event.get('summary', 'No Title'),
                'start': event['start'].get('dateTime', event['start'].get('date')),
                'end': event['end'].get('dateTime', event['end'].get('date')),
            }
            event_list.append(event_info)

        return event_list

    def add_event(self, event):
        # イベントをカレンダーに追加
        event_result = self.service.events().insert(calendarId='primary', body=event).execute()
        return event_result['id']

    def delete_event(self, event_id):
        # イベントを削除
        try:
            self.service.events().delete(calendarId='primary', eventId=event_id).execute()
            print(f"Event with ID {event_id} deleted.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    # UTCでのイベント日時を指定
    event = {
        'summary': 'サンプルイベント',
        'start': {
            'dateTime': '2024-10-05T20:00:00Z',  # UTCで設定
        },
        'end': {
            'dateTime': '2024-10-05T22:00:00Z',  # UTCで設定
        },
    }

    calendar = CalendarAPI()

    # イベント追加
    event_id = calendar.add_event(event)
    print(f"Event created with ID: {event_id}")
    # イベント取得
    events = calendar.get_events()
    print(events)
