import os
from google.cloud import translate_v2 as translate

# 設定金鑰路徑（假設 key.json 在腳本同目錄）
current_dir = os.path.dirname(os.path.abspath(__file__))
key_path = os.path.join(current_dir, "key.json")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_path

# 初始化翻譯客戶端
client = translate.Client()

text = "Hello, world!"
lang_list = client.get_languages()

for language in lang_list:
    target_language = language["language"]
    result = client.translate(text, target_language=target_language)
    print(f"[{target_language}] {result['translatedText']}")
