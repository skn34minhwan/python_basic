import streamlit as st
import pandas as pd

st.title("게임 캐릭터의 인지도")

characters = ["전사", "법사", "힐러", "탱커", "랜덤"]
selection_count = [120, 95, 150, 80, 111]
odds_of_winning = [52, 48, 56, 60, 49]
awareness = [25, 20, 30, 15, 22]

df = pd.DataFrame({
    "캐릭터" : characters,
    "선택횟수" : selection_count,
    "승률(%)" : odds_of_winning,
    "인지도(%)" : awareness
})

st.dataframe(df)
st.bar_chart(df.set_index("캐릭터")["선택횟수"])
st.line_chart(df.set_index("캐릭터")["승률(%)"])