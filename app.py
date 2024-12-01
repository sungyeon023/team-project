import streamlit as st
import pandas as pd
import bcrypt
import os

# 데이터 저장용 파일 경로
DATA_FILE = "user.csv"

# 데이터 파일 초기화
if not os.path.exists(DATA_FILE):
    pd.DataFrame(columns=["아이디", "비밀번호", "성별", "나이", "얼굴상", "DISC 검사 결과"]).to_csv(DATA_FILE, index=False)

# 비밀번호 암호화 함수
def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

# 비밀번호 확인 함수
def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed.encode())

# 회원가입 페이지
def register():
    st.title("회원가입 페이지")
    st.write("아래 정보를 입력해 주세요.")
    
    아이디 = st.text_input("아이디")
    비밀번호 = st.text_input("비밀번호", type="password")
    성별 = st.radio("성별", ["남성", "여성", "기타"])
    나이 = st.number_input("나이", min_value=0, step=1)
    얼굴상 = st.text_input("얼굴상 (예: 고양이상, 강아지상)")
    DISC_결과 = st.text_input("DISC 검사 결과")
    
    if st.button("회원가입"):
        if 아이디 and 비밀번호:
            # 데이터 읽기
            data = pd.read_csv(DATA_FILE)
            
            if 아이디 in data["아이디"].values:
                st.error("이미 사용 중인 아이디입니다.")
            else:
                hashed_pw = hash_password(비밀번호)
                # 데이터 저장
                new_user = {
                    "아이디": 아이디,
                    "비밀번호": hashed_pw,
                    "성별": 성별,
                    "나이": 나이,
                    "얼굴상": 얼굴상,
                    "DISC 검사 결과": DISC_결과,
                }
                data = data.append(new_user, ignore_index=True)
                data.to_csv(DATA_FILE, index=False)
                st.success("회원가입 완료!")
                # 로그인 페이지로 이동
                st.experimental_rerun()
        else:
            st.error("아이디와 비밀번호를 입력하세요.")

# 로그인 페이지
def login():
    st.title("로그인 페이지")
    아이디 = st.text_input("아이디")
    비밀번호 = st.text_input("비밀번호", type="password")
    
    if st.button("로그인"):
        data = pd.read_csv(DATA_FILE)
        user = data[data["아이디"] == 아이디]
        
        if not user.empty and verify_password(비밀번호, user.iloc[0]["비밀번호"]):
            st.success(f"환영합니다, {아이디}님!")
            st.session_state["logged_in"] = True
            st.session_state["user"] = user.iloc[0].to_dict()
            st.experimental_rerun()
        else:
            st.error("아이디 또는 비밀번호가 올바르지 않습니다.")

# 대시보드 페이지
def dashboard():
    st.title("대시보드")
    st.write(f"환영합니다, {st.session_state['user']['아이디']}님!")
    st.write("회원 정보를 확인하세요:")
    st.write(f"성별: {st.session_state['user']['성별']}")
    st.write(f"나이: {st.session_state['user']['나이']}")
    st.write(f"얼굴상: {st.session_state['user']['얼굴상']}")
    st.write(f"DISC 검사 결과: {st.session_state['user']['DISC 검사 결과']}")
    
    if st.button("로그아웃"):
        st.session_state["logged_in"] = False
        st.session_state["user"] = None
        st.experimental_rerun()

# 메인 앱
def main():
    # 세션 상태 초기화
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
        st.session_state["user"] = None

    st.sidebar.title("메뉴")
    
    if st.session_state["logged_in"]:
        dashboard()
    else:
        choice = st.sidebar.selectbox("옵션 선택", ["회원가입", "로그인"])
        if choice == "회원가입":
            register()
        elif choice == "로그인":
            login()

if __name__ == "__main__":
    main()
