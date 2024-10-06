import google.generativeai as genai
from dotenv import load_dotenv
import os
import PIL.Image

load_dotenv()

#質問文を読み込む
question = input()

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(question)
print(response.text)