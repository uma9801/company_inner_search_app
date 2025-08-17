import os
from langchain_core.documents import Document
import streamlit as st
import constants as ct

path = "./data/社員について/社員名簿.csv"

# ファイルの拡張子を取得
file_extension = os.path.splitext(path)[1]
# ファイル名（拡張子を含む）を取得
file_name = os.path.basename(path)

# 想定していたファイル形式の場合のみ読み込む
if file_extension in ct.SUPPORTED_EXTENSIONS:
    # csvファイルは1つのドキュメントにまとめる
    if file_extension == ".csv":
        # csvモジュールで1行ずつ読み込む
        docs_all = []
        
        loader = ct.SUPPORTED_EXTENSIONS[file_extension](path)
        docs = loader.load()
        
        delete_words = [
            "氏名（フルネーム）:", "性別:", "メールアドレス:",
            "従業員区分:", "役職:", "大学名:", "学部・学科:"
        ]
        for doc in docs:
            for word in delete_words:
                doc.page_content = doc.page_content.replace(word, "")
                
        st.write(docs)
        # すべてのドキュメントのテキストを改行で連結
        merged_content = "\n".join([doc.page_content for doc in docs])
        # 最初のドキュメントのメタデータを流用（必要に応じて調整）
        merged_metadata = docs[0].metadata if docs else {}
        # 1つのDocumentにまとめる
        merged_doc = Document(page_content=merged_content, metadata=merged_metadata)
        docs_all.append(merged_doc)
        st.write(len(docs_all[0].page_content))
        st.write(docs_all)
