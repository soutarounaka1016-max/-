import streamlit as st

st.title("AI受験コーチ（テスト版）")
st.write("ここまで動けば公開準備は完了です！")

text = st.text_input("今日の勉強内容を入力してください")
if text:
    st.write(f"あなたの入力: {text}")
