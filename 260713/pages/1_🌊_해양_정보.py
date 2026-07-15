import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="해양 정보", layout="wide")

st.title("🌊 대한민국 해양 정보")

st.write("동해, 서해, 남해의 해양환경과 대표 어종을 확인할 수 있습니다.")

# ====================================================
# 이미지 폴더
# ====================================================

BASE_DIR = Path(__file__).resolve().parent.parent
IMAGE_DIR = BASE_DIR / "images"
FISH_DIR = IMAGE_DIR / "fish"

# ====================================================
# 데이터
# ====================================================

sea_info = {

    "동해": {
        "image": IMAGE_DIR / "east_sea.png",
        "temperature": 16.8,
        "salinity": 34.1,
        "ph": 8.12,
        "oxygen": 8.2,
        "nitrate": 1.8,
        "phosphate": 0.15,
        "silicate": 4.5,
        "fish": ["명태", "대구", "오징어", "연어", "꽁치"]
    },

    "서해": {
        "image": IMAGE_DIR / "west_sea.png",
        "temperature": 14.5,
        "salinity": 31.8,
        "ph": 8.03,
        "oxygen": 7.4,
        "nitrate": 6.5,
        "phosphate": 0.45,
        "silicate": 12.5,
        "fish": ["조기", "꽃게", "낙지", "농어", "우럭"]
    },

    "남해": {
        "image": IMAGE_DIR / "south_sea.png",
        "temperature": 18.2,
        "salinity": 33.5,
        "ph": 8.09,
        "oxygen": 7.6,
        "nitrate": 4.2,
        "phosphate": 0.3,
        "silicate": 7.8,
        "fish": ["방어", "참돔", "고등어", "멸치", "전갱이"]
    }

}

# ====================================================
# 바다 선택
# ====================================================

st.subheader("🌊 바다 선택")

sea = st.radio(
    "",
    ["동해", "서해", "남해"],
    horizontal=True
)

data = sea_info[sea]

st.divider()

col1, col2 = st.columns([1,1])

# ====================================================
# 바다 사진
# ====================================================

with col1:

    st.subheader(f"📷 {sea}")

    if data["image"].exists():
        st.image(data["image"], use_container_width=True)
    else:
        st.warning("바다 사진이 없습니다.")

# ====================================================
# 환경 정보
# ====================================================

with col2:

    st.subheader("🌡 환경 정보")

    st.metric("평균 수온", f"{data['temperature']} ℃")
    st.metric("평균 염분", f"{data['salinity']} psu")
    st.metric("pH", data["ph"])
    st.metric("용존산소", f"{data['oxygen']} mg/L")
    st.metric("질산염", f"{data['nitrate']} mg/L")
    st.metric("인산염", f"{data['phosphate']} mg/L")
    st.metric("규산염", f"{data['silicate']} mg/L")

st.divider()

# ====================================================
# 대표 어종
# ====================================================

st.subheader("🐟 주로 서식하는 어종")

cols = st.columns(len(data["fish"]))

for i, fish in enumerate(data["fish"]):

    with cols[i]:

        st.markdown(f"### {fish}")

        fish_image = FISH_DIR / f"{fish}.png"

        if fish_image.exists():
            st.image(fish_image, use_container_width=True)
        else:
            st.info("이미지 준비 중")

st.divider()

# ====================================================
# 그래프
# ====================================================

graph_df = pd.DataFrame({

    "항목": [
        "수온",
        "염분",
        "pH",
        "용존산소"
    ],

    "값": [
        data["temperature"],
        data["salinity"],
        data["ph"],
        data["oxygen"]
    ]

})

fig = px.bar(
    graph_df,
    x="항목",
    y="값",
    title=f"{sea} 환경 정보",
    color="값"
)

st.plotly_chart(fig, use_container_width=True)

st.success("해양 정보를 불러왔습니다.")