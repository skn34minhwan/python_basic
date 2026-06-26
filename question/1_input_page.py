import streamlit as st

st.title("사용자 입력 받는 페이지")

col1, col2 = st.columns(2)

with col1: 
    nickname = st.text_input("닉네임 입력")
    age = st.number_input(
                "나이 입력", 
                min_value = 13, 
                max_value = 100)
    nationality = st.selectbox(
                "국적 선택", 
                options = ['한국', '중국', '일본', '미국', '외계']
                )
    hobby = st.radio(
                "취미 선택", 
                options = ['맛집 탐방', '영화 감상', '음악 감상', '뜨개질']
                )
    agreement = st.checkbox("개인정보 제공 동의")

with col2:
    if st.button("입력 완료"):
        st.write(f"이름: {nickname}")
        st.write(f"나이: {age}")
        st.write(f"국적: {nationality}")
        st.write(f"취미: {hobby}")
        st.write(f"개인정보 제공 동의 여부: {agreement}")
    