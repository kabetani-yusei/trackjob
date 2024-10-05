import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from datetime import datetime, timedelta, date  # datetimeモジュールから必要なクラスをインポート
from dateutil import parser 
import time
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from calendarapi import CalendarAPI
import streamlit_calendar as st_calendar

# カレンダーAPIのインスタンスを作成
calendar = CalendarAPI()

# Streamlit アプリ設定
st.set_page_config(
    page_title="Time Detail",
    page_icon=":stopwatch:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.header("スケジュール詳細見える化アプリ", divider=True)
st.markdown("#### やること")
# ボタンの状態管理
if "start" not in st.session_state:
    st.session_state.start = None
if "is_started" not in st.session_state:
    st.session_state.is_started = False
if "reset_input" not in st.session_state:
    st.session_state.reset_input = False
if st.session_state.reset_input:
    st.session_state.task = ""
    st.session_state.reset_input = False

# タスク入力
doing_text = st.text_input(label='タスクを入力してください', key="task")

# 開始ボタンの処理
if not st.session_state.is_started:
    if doing_text:  # テキストが入力されている場合のみボタンを有効に
        if st.button("開始"):
            st.session_state.start = datetime.utcnow()
            st.session_state.is_started = True
            st.write(f"'{doing_text}' の開始時刻: {st.session_state.start}")
            st.rerun()  # ページ再描画
    else:
        st.button("開始", disabled=True)  # テキストが空ならボタンは無効

# 終了ボタンの処理
if st.session_state.is_started:
    start_time_formatted = st.session_state.start.strftime('%H:%M')
    st.write(f"{doing_text} の開始時刻: {start_time_formatted}")
    if st.button("終了"):
        end = datetime.utcnow()
        event = {
            'summary': doing_text,
            'start': {'dateTime': st.session_state.start.isoformat() + 'Z'},
            'end': {'dateTime': end.isoformat() + 'Z'},
        }
        calendar.add_event(event)

        # 状態をリセット
        del st.session_state.start
        st.session_state.is_started = False
        st.session_state.reset_input = True
        st.rerun()  # ページ再描画

# カレンダー表示のヘッダー
st.markdown("##### カレンダーイベント (過去1週間)")

events = calendar.get_events()
print(events)
for i, event in enumerate(events):
    event['id'] = i + 1
    event['start'] = event['start'].replace('Z', '')
    event['end'] = event['end'].replace('Z', '')

print(events)

today = date.today()
week_dates = [today - timedelta(days=i) for i in range(7)]
cal = st_calendar.calendar(events=events, options={'initialView': 'timeGridWeek'})


# 前日の睡眠時間の表示
st.markdown("##### 睡眠時間")

# 前日の睡眠時間を探す
yesterday = datetime.utcnow() - timedelta(days=1)
yesterday_start = yesterday.replace(hour=0, minute=0, second=0, microsecond=0).isoformat() + 'Z'
yesterday_end = yesterday.replace(hour=23, minute=59, second=59, microsecond=0).isoformat() + 'Z'

events_result = calendar.service.events().list(
    calendarId='primary',
    timeMin=yesterday_start,
    timeMax=yesterday_end,
    singleEvents=True,
    orderBy='startTime'
).execute()

events_yesterday = events_result.get('items', [])
sleep_event = None

for event in events_yesterday:
    if 'summary' in event and event['summary'] == '睡眠':
        sleep_event = event
        break

if sleep_event:
    # sleep_start, sleep_end は datetime 形式または日付形式の文字列が入ると仮定
    sleep_start = sleep_event['start'].get('dateTime', sleep_event['start'].get('date'))
    sleep_end = sleep_event['end'].get('dateTime', sleep_event['end'].get('date'))

    # dateutil.parser.parseで日付文字列を柔軟に変換
    start_time = parser.parse(sleep_start)
    end_time = parser.parse(sleep_end)

    # 時刻部分だけを取得
    start_str = start_time.strftime("%H:%M")
    end_str = end_time.strftime("%H:%M")

    # 時間の差を計算
    duration = end_time - start_time
    hours, remainder = divmod(duration.total_seconds(), 3600)
    minutes = remainder // 60

    # 結果を表示
    st.write(f"前日の睡眠時間: {start_str} から {end_str} まで（{int(hours)}時間 {int(minutes)}分）")
else:
    st.write("睡眠情報が見つかりません。")

# AIからの前日のfeedbackを表示
st.markdown("##### AIからの前日のフィードバック")
feedback = "運動時間とか、空き時間とかからいい感じに生成させたい"
if feedback:
    st.write(f"AIからのフィードバック: {feedback}")
