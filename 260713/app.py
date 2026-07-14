import streamlit as st

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="대한민국 해양 AI 플랫폼",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# CSS
# -----------------------------
st.markdown("""
<style>

.main-title{
    font-size:42px;
    font-weight:bold;
    color:#0077b6;
}

.sub-title{
    font-size:20px;
    color:gray;
}

.info-box{
    padding:18px;
    border-radius:12px;
    background-color:#E3F2FD;
    border:1px solid #90CAF9;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# 제목
# -----------------------------
st.markdown(
    '<p class="main-title">🌊 대한민국 해양 생태 AI 분석 플랫폼</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub-title">Marine Ecosystem Analysis Platform</p>',
    unsafe_allow_html=True
)

st.divider()

# -----------------------------
# 소개
# -----------------------------
st.markdown("""
### 프로젝트 소개

이 플랫폼은 대한민국의 **동해, 서해, 남해**의

- 수온
- 염분
- pH
- 용존산소(DO)
- 질산염(NO₃⁻)
- 인산염(PO₄³⁻)
- 규산염(SiO₂)

등의 화학적·환경적 특성을 확인하고,

환경 변화에 따른 **어류 서식 가능성**을 AI가 예측하는 플랫폼입니다.
""")

st.divider()

# -----------------------------
# 기능 소개
# -----------------------------
col1, col2 = st.columns(2)

with col1:

    st.markdown("""
### 🌊 해양 정보

- 동해
- 서해
- 남해

지역별

- 화학적 조성
- 수온
- 염분
- 용존산소
- 영양염

확인
""")

with col2:

    st.markdown("""
### 🤖 AI 예측

사용자가

- 수온 변경
- 염분 변경

↓

Random Forest 모델이

↓

어류 서식 확률 예측
""")

st.divider()

# -----------------------------
# 향후 추가 기능
# -----------------------------
st.header("📌 포함될 기능")

features = [
    "대한민국 지도 클릭",
    "동해 · 서해 · 남해 정보",
    "Plotly 그래프",
    "화학 조성 시각화",
    "대표 어류 정보",
    "Kaggle 데이터 분석",
    "Random Forest AI 예측",
    "환경 변화 시뮬레이션",
    "2050년 기후 변화 예측"
]

for feature in features:
    st.checkbox(feature, value=False, disabled=True)

st.divider()

# -----------------------------
# 사용 방법
# -----------------------------
st.info("""
왼쪽 사이드바에서 원하는 메뉴를 선택하세요.

① 해양 정보

② AI 예측

③ 환경 비교

④ 프로젝트 소개
""")

st.success("프로젝트가 정상적으로 실행되었습니다.")