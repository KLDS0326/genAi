import streamlit as st #모든 streamlit 명령은 "st" alias로 사용할 수 있습니다.

st.set_page_config(page_title="Streamlit Demo") #HTML 제목
st.title("Streamlit Demo") #page 제목

color_text = st.text_input("가장 좋아하는 색깔이 뭔가요?") #텍스트 상자 표시
go_button = st.button("Go", type="primary") #기본 버튼 표시

if go_button: #버튼이 클릭될 때 이 if 블록의 코드가 실행됩니다.
    st.write(f"저도 {color_text} 좋아해요!") #응답 콘텐츠 표시

    
