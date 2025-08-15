############################################################
# ライブラリの読み込み
############################################################
import streamlit as st
import utils
import constants as ct

main_page_number = 0
content = {"main_page_number": main_page_number}
message = {'content': content}
st.success(f"（ページNo.{message['content']['main_page_number']+1}）")

page_number = 0
file_info = f"（ページNo.{page_number+1}）"
st.info(file_info)