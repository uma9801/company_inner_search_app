import os
from langchain_community.document_loaders import TextLoader

# 日本語パスを含むファイル
relative_path = r"data\MTG議事録\議事録ルール.txt"

# 1. 相対パスでのテスト
try:
    loader = TextLoader(relative_path, encoding="utf-8")
    docs = loader.load()
    print("相対パスでの読み込み成功:", docs)
except Exception as e:
    print("相対パスでの読み込みエラー:", e)

# 2. 絶対パスでのテスト
abs_path = os.path.abspath(relative_path)
try:
    loader = TextLoader(abs_path, encoding="utf-8")
    docs = loader.load()
    print("絶対パスでの読み込み成功:", docs)
except Exception as e:
    print("絶対パスでの読み込みエラー:", e)