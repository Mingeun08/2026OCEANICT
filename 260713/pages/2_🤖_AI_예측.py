import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="AI 예측", layout="wide")

st.title("🤖 AI 어류 서식 예측")

st.write("""
환경 조건을 변경하면 AI가 어떤 어류가 잘 서식할 가능성이 높은지 예측합니다.
(현재는 프로토타입 버전입니다.)
""")

# ------------------------
# 바다 선택
# ------------------------

sea = st.selectbox(
    "바다 선택",
    ["동해", "서해", "남해"]
)

st.divider()

# ------------------------
# 입력값
# ------------------------

col1, col2 = st.columns(2)

with col1:

    temperature = st.slider(
        "수온 (℃)",
        min_value=0.0,
        max_value=35.0,
        value=18.0,
        step=0.1
    )

    salinity = st.slider(
        "염분 (psu)",
        min_value=20.0,
        max_value=40.0,
        value=34.0,
        step=0.1
    )

with col2:

    oxygen = st.slider(
        "용존산소 (mg/L)",
        min_value=2.0,
        max_value=12.0,
        value=7.5,
        step=0.1
    )

    ph = st.slider(
        "pH",
        min_value=7.0,
        max_value=9.0,
        value=8.1,
        step=0.01
    )

st.divider()

# ------------------------
# 예측 버튼
# ------------------------

if st.button("🔍 예측하기"):

    scores = {}

    if temperature <= 15:
        scores["명태"] = 95
        scores["대구"] = 90
        scores["연어"] = 88

    elif temperature <= 20:
        scores["오징어"] = 92
        scores["대구"] = 83
        scores["꽁치"] = 80

    elif temperature <= 25:
        scores["방어"] = 91
        scores["참돔"] = 87
        scores["고등어"] = 85

    else:
        scores["멸치"] = 90
        scores["전갱이"] = 87
        scores["참치"] = 80

    st.success("예측 완료!")

    result = pd.DataFrame({
        "어종": list(scores.keys()),
        "서식 확률": list(scores.values())
    })

    st.dataframe(result, use_container_width=True)

    fig = px.bar(
        result,
        x="어종",
        y="서식 확률",
        color="서식 확률",
        title="AI 예측 결과"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("AI 분석")

    best = result.iloc[0]["어종"]

    st.info(f"""
현재 입력한 환경에서는 **{best}**의 서식 가능성이 가장 높습니다.

예측 근거

• 수온 : {temperature}℃

• 염분 : {salinity} psu

• 용존산소 : {oxygen} mg/L

• pH : {ph}
""")