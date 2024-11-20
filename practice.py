import streamlit as st


page_one = st.Page(
    page= "sub/page1.py",
    title="page 1"
)

page_two = st.Page(
    page= "sub/page2.py",
    title="page 2"
)

page_three = st.Page(
    page= "sub/page3.py",
    title="page 3"
)

import streamlit as st

# HTML을 사용하여 링크로 이동하는 버튼
naver_button = """
    <style>
    .naver-button {
        background-color: #03C75A;
        color: green;
        padding: 10px 24px;
        border: none;
        border-radius: 4px;
        text-align: center;
        font-size: 16px;
        cursor: pointer;
        text-decoration: none;
        display: inline-block;
    }
    .naver-button:hover {
        background-color: #029e4b;
    }
    </style>
    <a href="https://www.naver.com" target="_blank" class="naver-button">네이버로 이동</a>
"""
st.markdown(naver_button, unsafe_allow_html=True)

# Streamlit 버튼을 사용해 네이버로 이동
if st.button("네이버로 이동 (Streamlit 버튼)"):
    st.markdown('<meta http-equiv="refresh" content="0;url=https://www.naver.com">', unsafe_allow_html=True)




pages = st.navigation(
    {
        "Home" : [page_one],
        "Products" : [page_two],
        "Contacts" : [page_three]
    }
)
pages.run()


import streamlit as st

# 페이지 상태를 세션에 저장
if 'page' not in st.session_state:
    st.session_state.page = 'page1'

# 페이지 이동 버튼 정의
def navigate_to_page(page_name):
    st.session_state.page = page_name

# 현재 페이지에 따라 다른 내용 표시
if st.session_state.page == 'page1':
    st.title("페이지 1")
    st.write("여기는 페이지 1입니다.")
    if st.button("페이지 2로 이동"):
        navigate_to_page('page2')

elif st.session_state.page == 'page2':
    st.title("페이지 2")
    st.write("여기는 페이지 2입니다.")
    if st.button("페이지 1로 이동"):
        navigate_to_page('page1')
