st.title("🎈 My new app")
st.write(

import streamlit as st
    st.write("Hello, Streamlit!")  # 페이지 인삿말 예시

st.title("Streamlit 주요 요소 예시")  # 페이지 제목
st.header("헤더 예시")  # 큰 제목
st.subheader("서브헤더 예시")  # 작은 제목
st.text("텍스트 예시: 일반 텍스트를 표시합니다.")  # 일반 텍스트
st.markdown("**마크다운 예시:** _굵게, 이탤릭, 링크 등 지원_ [Streamlit](https://streamlit.io)")  # 마크다운 텍스트
st.caption("캡션 예시: 설명이나 부가 정보")  # 캡션
st.code("print('Hello Streamlit!')", language='python')  # 코드 블록
st.latex(r"E=mc^2")  # LaTeX 수식

st.divider()  # 구분선

st.write("write 함수 예시: 다양한 타입의 데이터를 자동으로 렌더링합니다.")  # write 함수
st.write({"key": "value"})  # 딕셔너리 출력

st.image("https://static.streamlit.io/examples/dog.jpg", caption="이미지 예시")  # 이미지
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")  # 오디오
st.video("https://www.w3schools.com/html/mov_bbb.mp4")  # 비디오

st.divider()  # 구분선

st.button("버튼 예시")  # 버튼
st.checkbox("체크박스 예시")  # 체크박스
st.radio("라디오 버튼 예시", ["옵션 1", "옵션 2", "옵션 3"])  # 라디오 버튼
st.selectbox("셀렉트박스 예시", ["A", "B", "C"])  # 셀렉트박스
st.multiselect("멀티셀렉트 예시", ["X", "Y", "Z"])  # 멀티셀렉트
st.slider("슬라이더 예시", 0, 100, 50)  # 슬라이더
st.number_input("숫자 입력 예시", min_value=0, max_value=100, value=10)  # 숫자 입력
st.text_input("텍스트 입력 예시")  # 텍스트 입력
st.text_area("텍스트 에어리어 예시")  # 텍스트 에어리어
st.date_input("날짜 입력 예시")  # 날짜 입력
st.time_input("시간 입력 예시")  # 시간 입력
st.file_uploader("파일 업로더 예시")  # 파일 업로더

st.divider()  # 구분선

import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(10, 3),
    columns=["a", "b", "c"]
)
st.dataframe(df)  # 데이터프레임 표시
st.table(df.head())  # 테이블 표시

st.divider()  # 구분선

st.progress(70)  # 진행률 바
st.spinner("스피너 예시: 작업 중...")  # 스피너
st.success("성공 메시지 예시")  # 성공 메시지
st.info("정보 메시지 예시")  # 정보 메시지
st.warning("경고 메시지 예시")  # 경고 메시지
st.error("에러 메시지 예시")  # 에러 메시지

st.divider()  # 구분선

st.sidebar.title("사이드바 예시")  # 사이드바 제목
st.sidebar.button("사이드바 버튼")  # 사이드바 버튼
st.sidebar.selectbox("사이드바 셀렉트박스", ["1", "2", "3"])  # 사이드바 셀렉트박스

st.divider()  # 구분선

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 2, 3])
st.pyplot(fig)  # Matplotlib 차트

import altair as alt
chart = alt.Chart(df).mark_bar().encode(x='a', y='b')
st.altair_chart(chart)  # Altair 차트

import plotly.express as px
fig2 = px.scatter(df, x="a", y="b")
st.plotly_chart(fig2)  # Plotly 차트
