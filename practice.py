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

st.title('Streamlit 앱의 테마 사용자 정의하기')

st.write('이 앱의 `.streamlit/config.toml` 파일 내용')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")

number = st.sidebar.slider('숫자를 선택하세요:', 0, 10, 5)
st.write('슬라이더 위젯에서 선택된 숫자:', number)


[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
