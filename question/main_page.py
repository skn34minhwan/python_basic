import streamlit as st

st.title("오늘은 수요일")
st.header("오늘은 Streamlit 배우는 날")
st.subheader("Streamlit으로 나만의 데모 페이지 만들기")

user_input = st.text_input("오늘 내가 만들어볼 사이트는?")

if user_input:
    st.write(user_input)

    if st.button(f"{user_input} 접속"):
        st.success(f"{user_input} 접속 중")
