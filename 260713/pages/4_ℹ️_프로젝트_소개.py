import streamlit as st

st.set_page_config(
    page_title="프로젝트 소개",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ 대한민국 해양 생태 AI 분석 플랫폼")

st.markdown("---")

# -------------------------------
# 프로젝트 개요
# -------------------------------

st.header("📌 프로젝트 개요")

st.markdown("""
대한민국 **동해, 서해, 남해**의 해양 환경 데이터를 분석하고,
환경 변화가 해양 생태계에 미치는 영향을 시각적으로 확인할 수 있는 AI 플랫폼입니다.

본 프로젝트는 단순한 정보 제공을 넘어,
**환경 변화에 따른 어류 서식 가능성을 머신러닝(Random Forest)으로 예측하는 것**을 목표로 합니다.
""")

st.markdown("---")

# -------------------------------
# 프로젝트 목표
# -------------------------------

st.header("🎯 프로젝트 목표")

col1, col2 = st.columns(2)

with col1:

    st.success("""
✔ 대한민국 3개 해역의 환경 정보 제공

✔ 화학적 조성 시각화

✔ 대표 어류 정보 제공

✔ 환경 변화 시뮬레이션
""")

with col2:

    st.success("""
✔ AI 기반 어류 서식 예측

✔ 기후변화 영향 분석

✔ 데이터 기반 해양 생태 연구

✔ 교육용 플랫폼 구축
""")

st.markdown("---")

# -------------------------------
# 사용 기술
# -------------------------------

st.header("💻 사용 기술")

tech = {
    "Python": "전체 프로그램 개발",
    "Streamlit": "웹 플랫폼 제작",
    "Pandas": "데이터 처리",
    "Plotly": "데이터 시각화",
    "Scikit-Learn": "Random Forest 머신러닝",
    "Joblib": "AI 모델 저장 및 불러오기",
    "Kaggle Dataset": "학습 데이터",
}

for name, desc in tech.items():
    st.write(f"**{name}** : {desc}")

st.markdown("---")

# -------------------------------
# 시스템 구조
# -------------------------------

st.header("⚙️ 시스템 구성")

st.code("""
사용자

↓

대한민국 바다 선택

↓

환경 데이터 조회

↓

환경 변수 변경

↓

Random Forest AI

↓

어류 서식 예측

↓

그래프 및 결과 출력
""")

st.markdown("---")

# -------------------------------
# 제공 기능
# -------------------------------

st.header("🌊 제공 기능")

features = [
    "동해 · 서해 · 남해 환경 정보",
    "수온 · 염분 · pH · 용존산소 확인",
    "대표 어류 정보",
    "환경 데이터 그래프",
    "환경 변화 시뮬레이션",
    "AI 기반 어류 서식 예측",
    "기후변화 시나리오 분석 (예정)"
]

for f in features:
    st.checkbox(f, value=True, disabled=True)

st.markdown("---")

# -------------------------------
# 머신러닝
# -------------------------------

st.header("🤖 AI 예측 모델")

st.info("""
학습 데이터(Kaggle)를 전처리하여

Temperature

Salinity

pH

Dissolved Oxygen

등을 입력 변수(feature)로 사용합니다.

Random Forest 모델이

각 어종의 서식 가능성을 예측합니다.
""")

st.markdown("---")

# -------------------------------
# 향후 계획
# -------------------------------

st.header("🚀 향후 개발 계획")

plans = [
    "Kaggle 데이터 자동 연동",
    "실시간 해양환경 데이터(Open API) 적용",
    "대한민국 지도 클릭 기능",
    "2050년 기후변화 시뮬레이션",
    "어종 분포 지도",
    "AI 정확도 향상(XGBoost 비교)",
    "데이터 다운로드 기능"
]

for p in plans:
    st.write("✅", p)

st.markdown("---")

# -------------------------------
# 제작자
# -------------------------------

st.header("👨‍💻 프로젝트 정보")

st.write("""
**프로젝트명**

대한민국 해양 생태 AI 분석 플랫폼

**개발 환경**

Python 3

Streamlit

Plotly

Scikit-Learn

**프로젝트 목적**

해양 환경 데이터를 활용한
AI 기반 해양 생태 분석 플랫폼 개발
""")

st.markdown("---")

st.success("감사합니다. 🌊")