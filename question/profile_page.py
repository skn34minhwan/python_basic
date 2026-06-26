import streamlit as st
import pydeck as pdk
import random

st.set_page_config(page_title="노민환 프로필", page_icon="👤", layout="centered")
st.title("Profile")

col_img, col_text = st.columns([1, 2.5])

with col_img:
    st.markdown("<div style='text-align: center; font-size: 80px;'>👤</div>", unsafe_allow_html=True)

with col_text:
    st.markdown("### 안녕하세요, 노민환입니다.")
    st.markdown("""
    **데이터사이언스**를 전공하였으며, 현재는 **AI**를 공부하고 있습니다.     
    """)

st.divider() 

st.header("기본 정보")
col1, col2 = st.columns(2)

with col1:
    st.subheader("정보")
    st.write("👉️ **사는 곳:** 서울시 도봉구")
    st.write("👉️ **출생:** 00년생")
    st.write("👉️ **깃허브:** https://github.com/minhwan123")


with col2:
    st.subheader("관심 분야 & 취미")
    st.write("🧠 **관심 분야:** 머신러닝/딥러닝 모델링")
    st.write("🎵 **취미:** 집에서 쉬기, 유튜브 보기")

st.divider()
st.header("🚇등교 경로")
# 도봉구 <-> 금천구
start = [127.0441, 37.6672]
end = [126.8894, 37.4662]

view_state = pdk.ViewState(latitude=37.56, longitude=126.97, zoom=10)

layer = pdk.Layer(
    "LineLayer",
    data=[{"start": start, "end": end}],
    get_source_position="start",
    get_target_position="end",
    get_color=[255, 0, 0],
    get_width=5,
)

st.pydeck_chart(pdk.Deck(
    initial_view_state=view_state,
    layers=[layer]
))

st.divider()
if st.button("파이팅 메시지 💡"):
    messages = [
        "오늘도 무난하게 가봅시다.",
        "할 일은 많지만 하나씩 하면 됩니다.",
        "커피 한 잔 하고 다시 시작해볼까요?",
        "일단 시작하면 절반은 한 겁니다."
    ]
    st.success(random.choice(messages))

st.divider()
st.header("오늘 상태📝")
today_mood = st.selectbox(
    "오늘의 기분?", 
    ["아주 좋아요 😄", "그냥 그래요 😐", "피곤해요 😩", "열정 🔥", "집중 💻"]
)
resolution = st.text_input("오늘의 한 줄 다짐?")

if resolution:
    st.success(f"현재 기분: **{today_mood}**")
    st.info(f"오늘의 다짐: **{resolution}**")

