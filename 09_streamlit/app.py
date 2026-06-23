import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 가상 일일 매출 데이터 생성
dates = pd.date_range(start='2024-01-01', periods=50)
sales = np.random.randint(100, 500, 50)

# 데이터프레임 생성
df = pd.DataFrame({
    "Date": dates,
    "Sales": sales
})

# 데이터프레임 출력
st.write("Daily Sales DataFrame:", df)

# Matplotlib 선 그래프 생성
fig, ax = plt.subplots()
ax.plot(df["Date"], df["Sales"], marker='o', linestyle='-')
ax.set_title("2026-01 Sales")
ax.set_xlabel("Date")
ax.set_ylabel("Sales (KRW)")
plt.xticks(rotation=45)

# 그래프 출력
st.write(fig)