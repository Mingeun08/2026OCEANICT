import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import os

st.set_page_config(page_title="해양 정보", layout="wide")

st.title("🌊 대한민국 해양 정보")

st.write("대한민국의 동해, 서해, 남해의 환경 정보를 확인할 수 있습니다.")

# ------------------------
# 데이터
# ------------------------

sea_info = {
    "동해": {
        "image": "images/east_sea.jpg",
        "temperature": 18.2,
        "salinity": 34.3,
        "ph": 8.10,
        "oxygen": 7.8,
        "nitrate": 0.13,
        "phosphate": 0.04,
        "silicate": 1.8,
        "fish": ["명태", "대구", "오징어", "연어", "꽁치"]
    },

    "서해": {
        "image": "images/west_sea.jpg",
        "temperature": 20.8,
        "salinity": 31.5,
        "ph": 8.00,
        "oxygen": 6.5,
        "nitrate": 0.16,
        "phosphate": 0.06,
        "silicate": 2.3,
        "fish": ["조기", "꽃게", "낙지", "농어", "우럭"]
    },

    "남해": {
        "image": "images/south_sea.jpg",
        "temperature": 22.4,
        "salinity": 33.8,
        "ph": 8.15,
        "oxygen": 6.9,
        "nitrate": 0.09,
        "phosphate": 0.03,
        "silicate": 1.2,
        "fish": ["방어", "참돔", "고등어", "멸치", "전갱이"]
    }
}

# ------------------------
# 지도
# ------------------------

st.subheader("🗺 대한민국")

if os.path.exists("images/korea_map.png"):
    st.image("images/korea_map.png", use_container_width=True)
else:
    st.info("images 폴더에 korea_map.png를 넣어주세요.")

# ------------------------
# 선택
# ------------------------

sea = st.radio(
    "바다를 선택하세요.",
    ["동해", "서해", "남해"],
    horizontal=True
)

data = sea_info[sea]

st.divider()

col1, col2 = st.columns([1,1])

# ------------------------
# 사진
# ------------------------

with col1:

    st.subheader(f"📷 {sea}")

    if os.path.exists(data["image"]):
        st.image(data["image"], use_container_width=True)
    else:
        st.warning("사진을 넣어주세요.")

# ------------------------
# 환경정보
# ------------------------

with col2:

    st.subheader("🌡 환경 정보")

    st.metric("평균 수온", f'{data["temperature"]} ℃')

    st.metric("평균 염분", f'{data["salinity"]} psu')

    st.metric("pH", data["ph"])

    st.metric("용존산소", f'{data["oxygen"]} mg/L')

    st.metric("질산염", f'{data["nitrate"]} mg/L')

    st.metric("인산염", f'{data["phosphate"]} mg/L')

    st.metric("규산염", f'{data["silicate"]} mg/L')

st.divider()

# ------------------------
# 대표 어류
# ------------------------

st.subheader("🐟 대표 어류")

cols = st.columns(len(data["fish"]))

for i, fish in enumerate(data["fish"]):

    with cols[i]:
        st.success(fish)

st.divider()

# ------------------------
# 그래프
# ------------------------

graph_df = pd.DataFrame({

    "항목":[
        "수온",
        "염분",
        "pH",
        "용존산소"
    ],

    "값":[
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
    title=f"{sea} 환경 정보"
)

st.plotly_chart(fig, use_container_width=True)

st.success("해양 정보를 불러왔습니다.")