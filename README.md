# beginners hackathon
スケジュール詳細の見える化アプリ

実行環境
windows11
python 3.9.10
仮想環境名：venv

1. Pythonの仮想環境を作成する
```
python -m venv venv
```

3. 仮想環境を有効化する
```
venv\Scripts\activate
```

5. Pythonの必要なパッケージをインストールする
```
pip install -r requirements.txt
```

7. Google calendar apiを使用するためのcredentials.jsonを同じディレクトリ上に配置する  
このurlを参考に同じディレクトリにcredentials.jsonを配置する(名前を変更する必要あり)  
[GoogleカレンダーにPythonから予定を追加・編集してみた](https://dev.classmethod.jp/articles/google-calendar-api-create-schedule/)  

9. gemini apiのapi keyを取得する  
[Gemini API のスタートガイド](https://ai.google.dev/gemini-api/docs?hl=ja#:~:text=Gemini%20API%20%E3%81%AE%E3%82%B9%E3%82%BF%E3%83%BC%E3%83%88%E3%82%AC%E3%82%A4%E3%83%89%20Gemini%20API%20%E3%81%A8%20Google,AI%20Studio%20%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%99%E3%82%8B%E3%81%A8%E3%80%81Google%20%E3%81%AE%E6%9C%80%E6%96%B0%E3%83%A2%E3%83%87%E3%83%AB%E3%82%92%E4%BD%BF%E3%81%84%E5%A7%8B%E3%82%81%E3%82%8B%E3%81%93%E3%81%A8%E3%81%8C%E3%81%A7%E3%81%8D%E3%81%BE%E3%81%99%E3%80%82%20Gemini%20%E3%83%A2%E3%83%87%E3%83%AB%20%E3%83%95%E3%82%A1%E3%83%9F%E3%83%AA%E3%83%BC%E5%85%A8%E4%BD%93%E3%81%AB%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E3%81%A7%E3%81%8D%E3%80%81%E3%82%A2%E3%82%A4%E3%83%87%E3%82%A2%E3%82%92%E6%8B%A1%E5%BC%B5%E5%8F%AF%E8%83%BD%E3%81%AA%E5%AE%9F%E9%9A%9B%E3%81%AE%E3%82%A2%E3%83%97%E3%83%AA%E3%82%B1%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%81%AB%E5%A4%89%E6%8F%9B%E3%81%A7%E3%81%8D%E3%81%BE%E3%81%99%E3%80%82)を参考にapi keyを取得して
.envファイルに以下のように書き込む
```
GOOGLE_API_KEY = 取得したapi key
```  

11. 実行する
```
streamlit run main.py
```
