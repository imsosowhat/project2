import streamlit as st
import random

# 1. 파스텔톤 배경 및 중앙 정렬을 위한 CSS 설정
st.markdown(
    """
    <style>
    /* 전체 배경을 부드러운 파스텔 블루/라벤더 톤으로 설정 */
    .stApp {
        background-color: #E8F0FE !important;
        text-align: center !important;
    }
    
    /* 텍스트 스타일 정의 (진한 회색으로 가독성 확보) */
    .stApp h1, .stApp h2, .stApp h3, .stApp p, .stApp span {
        color: #4A4A4A !important;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    
    /* 가위바위보 선택 버튼들을 가로로 예쁘게 중앙 정렬 */
    .stHorizontalBlock {
        justify-content: center !important;
        gap: 15px !important;
    }
    
    /* 버튼 자체 디자인 (파스텔톤에 어울리는 둥글고 부드러운 느낌) */
    div.stButton > button {
        background-color: #FFFFFF !important;
        color: #5C6BC0 !important; /* 부드러운 진한 파란색 글자 */
        font-weight: bold !important;
        font-size: 24px !important; /* 이모티콘이 잘 보이도록 크기 키움 */
        border: 2px solid #C5CAE9 !important;
        padding: 15px 30px !important;
        border-radius: 15px !important;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
    }
    
    /* 버튼에 마우스를 올렸을 때 효과 */
    div.stButton > button:hover {
        background-color: #C5CAE9 !important;
        color: white !important;
        transform: translateY(-2px);
    }
    
    /* 결과창 박스 스타일 */
    .result-box {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
        display: inline-block;
        margin-top: 30px;
        min-width: 300px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 타이틀 설정
st.title("✊✌️🖐️ 가위바위보 게임 🖐️✌️✊")
st.write("아래 버튼 중 하나를 선택하세요!")

# 가위바위보 데이터 정의
choices = ["✌️", "✊", "🖐️"]
name_map = {"✌️": "가위", "✊": "바위", "🖐️": "보"}

# 가로로 버튼 배치 (Streamlit의 columns 활용)
col1, col2, col3 = st.columns(3)

user_choice = None

with col1:
    if st.button("✌️ 가위"):
        user_choice = "✌️"
with col2:
    if st.button("✊ 바위"):
        user_choice = "✊"
with col3:
    if st.button("🖐️ 보"):
        user_choice = "🖐️"

# 사용자가 버튼을 클릭했을 때 게임 진행
if user_choice:
    # 컴퓨터의 랜덤 선택
    computer_choice = random.choice(choices)
    
    # 승패 로직 판정
    if user_choice == computer_choice:
        result = "비겼습니다! 🤝"
    elif (user_choice == "✌️" and computer_choice == "🖐️") or \
         (user_choice == "✊" and computer_choice == "✌️") or \
         (user_choice == "🖐️" and computer_choice == "✊"):
        result = "승!! 🎉"
    else:
        result = "패ㅠㅠ 😢"
        
    # 결과 화면 출력 (HTML 마크다운으로 중앙 배치 및 스타일링)
    st.markdown(
        f"""
        <div style='display: flex; justify-content: center;'>
            <div class='result-box'>
                <h3 style='margin: 0; color: #5C6BC0 !important;'>나: {user_choice} ({name_map[user_choice]})</h3>
                <h3 style='margin: 10px 0; color: #E57373 !important;'>컴퓨터: {computer_choice} ({name_map[computer_choice]})</h3>
                <hr style='border: 0; height: 1px; background: #E0E0E0; margin: 15px 0;'>
                <h1 style='margin: 0; font-size: 36px; font-weight: bold; color: #4A4A4A !important;'>{result}</h1>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )# project2
