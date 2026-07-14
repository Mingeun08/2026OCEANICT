import streamlit as st
from PIL import Image
from streamlit_image_coordinates import streamlit_image_coordinates

st.set_page_config(
    page_title="대한민국 해양 생태계 분석 플랫폼",
    page_icon="🌊",
    layout="wide"
)

st.title("🌊 대한민국 해양 생태계 분석 플랫폼")
st.write("지도의 바다를 클릭하면 해당 해역의 정보를 확인할 수 있습니다.")

# 지도 불러오기
image = Image.open("남한바다.png")

# 클릭 가능한 이미지
value = streamlit_image_coordinates(
    image,
    key="korea_map"
)

if value:

    x = value["x"]
    y = value["y"]

    st.write(f"클릭 좌표 : ({x}, {y})")

    sea = None

    # ----------------------------
    # 이 부분은 네 지도에 맞게 나중에 수정한다.
    # ----------------------------

    if x > image.width * 0.72:
        sea = "동해"

    elif y > image.height * 0.73:
        sea = "남해"

    else:
        sea = "서해"

    st.success(f"🌊 선택한 해역 : {sea}")

    if sea == "동해":

        st.header("동해")

        st.markdown("""
### 🌡 환경 특징
- 평균 수온 : 17℃
- 염분 : 34 PSU
- 용존산소가 높음
- 수심이 깊음
- 한류와 난류가 만나는 해역
""")

        st.markdown("""
### 🐟 잘 서식하는 어류

- 명태
- 대구
- 오징어
- 도루묵
- 연어
""")

    elif sea == "남해":

        st.header("남해")

        st.markdown("""
### 🌡 환경 특징
- 평균 수온 : 21℃
- 난류 영향
- 플랑크톤 풍부
- 양식업 발달
""")

        st.markdown("""
### 🐟 잘 서식하는 어류

- 멸치
- 갈치
- 고등어
- 전갱이
- 참돔
""")

    elif sea == "서해":

        st.header("서해")

        st.markdown("""
### 🌡 환경 특징
- 조수간만의 차 큼
- 갯벌 발달
- 영양염 풍부
""")

        st.markdown("""
### 🐟 잘 서식하는 어류

- 조기
- 꽃게
- 우럭
- 농어
- 숭어
""")