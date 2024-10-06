# beginners hachathon
スケジュール詳細の見える化アプリ

実行環境
windows11
python 3.9.10
仮想環境名：venv

1. Pythonの仮想環境を作成する
python -m venv venv

2. 仮想環境を有効化する
venv\Scripts\activate

3. Pythonの必要なパッケージをインストールする
pip install -r requirements.txt

4. credentials.jsonを同じディレクトリ上に配置する
このurlを参考に同じディレクトリにcredentials.jsonを配置する
https://dev.classmethod.jp/articles/google-calendar-api-create-schedule/

5. 実行する
streamlit run main.py