import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="환경 비교", layout="wide")

st.title("📊 해양 환경 비교 및 시뮬레이션")

st.markdown("""
현재 해양 환경과 사용자가 변경한 환경을 비교합니다.
향후 이 결과는 AI 예측 모델(Random Forest)과 연결됩니다.
""")

# -----------------------------
# 바다 선택
# -----------------------------
sea = st.selectbox(
    "🌊 비교할 바다를 선택하세요",
    ["동해", "서해", "남해"]
)

# -----------------------------
# 기본 데이터
# -----------------------------
base_data = {
    "동해": {
        "수온": 18.2,
        "염분": 34.3,
        "pH": 8.10,
        "용존산소": 7.8
    },
    "서해": {
        "수온": 20.8,
        "염분": 31.5,
        "pH": 8.00,
        "용존산소": 6.5
    },
    "남해": {
        "수온": 22.4,
        "염분": 33.8,
        "pH": 8.15,
        "용존산소": 6.9
    }
}

current = base_data[sea]

st.divider()

# -----------------------------
# 입력
# -----------------------------
st.subheader("🔧 환경 변화 설정")

col1, col2 = st.columns(2)

with col1:
    temp = st.slider(
        "수온 (℃)",
        0.0,
        35.0,
        float(current["수온"]),
        0.1
    )

    sal = st.slider(
        "염분 (psu)",
        20.0,
        40.0,
        float(current["염분"]),
        0.1
    )

with col2:
    ph = st.slider(
        "pH",
        7.0,
        9.0,
        float(current["pH"]),
        0.01
    )

    oxygen = st.slider(
        "용존산소 (mg/L)",
        2.0,
        12.0,
        float(current["용존산소"]),
        0.1
    )

st.divider()

# -----------------------------
# 현재 vs 변경 비교
# -----------------------------
compare = pd.DataFrame({
    "항목": ["수온", "염분", "pH", "용존산소"],
    "현재": [
        current["수온"],
        current["염분"],
        current["pH"],
        current["용존산소"]
    ],
    "변경 후": [
        temp,
        sal,
        ph,
        oxygen
    ]
})

st.subheader("📋 비교 표")

st.dataframe(compare, use_container_width=True)

# -----------------------------
# 그래프
# -----------------------------
fig = go.Figure()

fig.add_trace(go.Bar(
    name="현재",
    x=compare["항목"],
    y=compare["현재"]
))

fig.add_trace(go.Bar(
    name="변경 후",
    x=compare["항목"],
    y=compare["변경 후"]
))

fig.update_layout(
    barmode="group",
    title=f"{sea} 환경 변화 비교"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# 변화량
# -----------------------------
st.subheader("📈 변화량")

diff = {
    "수온": temp - current["수온"],
    "염분": sal - current["염분"],
    "pH": ph - current["pH"],
    "용존산소": oxygen - current["용존산소"]
}

c1, c2, c3, c4 = st.columns(4)

c1.metric("수온", f"{temp:.1f}℃", f"{diff['수온']:+.1f}")
c2.metric("염분", f"{sal:.1f} psu", f"{diff['염분']:+.1f}")
c3.metric("pH", f"{ph:.2f}", f"{diff['pH']:+.2f}")
c4.metric("용존산소", f"{oxygen:.1f} mg/L", f"{diff['용존산소']:+.1f}")

st.divider()

# -----------------------------
# 시뮬레이션 해석
# -----------------------------
st.subheader("🧠 시뮬레이션 해석")

if temp >= current["수온"] + 2:
    st.warning("🌡 수온이 크게 상승했습니다. 냉수성 어류의 서식 환경이 악화될 가능성이 있습니다.")

elif temp <= current["수온"] - 2:
    st.info("❄ 수온이 낮아졌습니다. 냉수성 어류에 유리한 환경이 될 수 있습니다.")

if oxygen < current["용존산소"]:
    st.warning("🫧 용존산소가 감소했습니다. 일부 어종의 생존에 영향을 줄 수 있습니다.")

if sal > current["염분"]:
    st.info("🌊 염분이 증가했습니다. 고염분 환경에 적응한 어종이 유리할 수 있습니다.")

st.success("향후 이 페이지는 AI 모델과 연동되어 실제 어종 변화 예측 결과를 제공합니다.")