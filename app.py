import streamlit as st
import time

# 1. 초기 세션 상태 설정 (게임의 데이터 저장소)
if 'page' not in st.session_state:
    st.session_state.page = "Intro"
if 'inventory' not in st.session_state:
    st.session_state.inventory =
if 'mood_history' not in st.session_state:
    st.session_state.mood_history =
if 'steps_data' not in st.session_state:
    st.session_state.steps_data = {}

# 2. 유틸리티 함수
def change_page(page_name):
    st.session_state.page = page_name
    st.rerun()

def add_inventory(item):
    if item not in st.session_state.inventory:
        st.session_state.inventory.append(item)
        st.toast(f"✨ 새로운 보석 획득: {item}")

# 3. 사이드바 구성 (가이드 및 진행도)
with st.sidebar:
    st.title("🕊️ 가이드의 안내")
    st.image("https://cdn-icons-png.flaticon.com/512/3251/3251501.png", width=100) # 가상 가이드 이미지
    st.info("우리는 부정적인 생각(GNATs)에 맞서 세상의 균형을 되찾아야 합니다. ")
    
    # 진행도 표시
    provinces = ["동굴", "얼음", "화산", "산맥", "늪지", "다리", "협곡"]
    progress_idx = 0
    if st.session_state.page in provinces:
        progress_idx = provinces.index(st.session_state.page) + 1
    
    st.write(f"**현재 위치:** {st.session_state.page}")
    st.progress(progress_idx / 7)
    
    st.write("---")
    st.subheader("🎒 수집한 마음의 보석")
    for item in st.session_state.inventory:
        st.write(f"💎 {item}")

# 4. 메인 게임 로직
# --- Intro: 캐릭터 생성 및 심리 교육 ---
if st.session_state.page == "Intro":
    st.title("⚔️ K-SPARX: 마음의 수호자")
    st.subheader("모험을 시작하기 전에")
    st.write("""
    이곳은 부정적인 생각인 'GNATs'에 점령당해 빛을 잃었습니다. 
    당신은 7개의 지역을 여행하며 마음을 지키는 기술을 배우게 될 것입니다. [1, 2]
    """)
    
    name = st.text_input("당신의 용사 이름은 무엇인가요?")
    mood = st.select_slider("지금 당신의 마음 날씨는 어떤가요?", 
                           options=["폭풍우", "흐림", "보통", "맑음", "매우 맑음"], value="보통")
    
    if st.button("포털로 입장하기"):
        if name:
            st.session_state.user_name = name
            change_page("동굴")
        else:
            st.error("이름을 입력해야 모험을 시작할 수 있습니다!")

# --- Level 1: Cave Province (희망과 호흡) ---
elif st.session_state.page == "동굴":
    st.header("🕸️ Level 1: 동굴 지역 - 희망 찾기")
    st.write(f"{st.session_state.user_name}님, 첫 번째 시련입니다. 어둠 속에서 안정을 찾아야 합니다.")
    
    st.warning("기법: 복식 호흡 (Relaxation Training) [2, 3]")
    st.write("화면의 지시에 따라 숨을 깊게 들이마시고 내뱉으세요.")
    
    if st.button("🔵 4초간 들이마시기"):
        with st.empty():
            for i in range(4, 0, -1):
                st.write(f"후우... {i}")
                time.sleep(1)
            st.success("잘하셨습니다! 마음이 조금 차분해졌나요?")
            add_inventory("희망의 불꽃")
            st.button("다음 지역으로: 얼음 지역", on_click=lambda: change_page("얼음"))

# --- Level 2: Ice Province (행동 활성화) ---
elif st.session_state.page == "얼음":
    st.header("❄️ Level 2: 얼음 지역 - 활동하기")
    st.write("모든 것이 차갑게 얼어붙었습니다. 몸을 움직여 온기를 되찾아야 합니다. ")
    
    st.warning("기법: 행동 활성화 (Behavioral Activation)")
    option = st.selectbox("마을을 녹이기 위해 현실에서 실천할 작은 활동을 골라보세요:", 
                         ["창문 열고 환기하기", "좋아하는 노래 1곡 듣기", "기지개 크게 켜기", "물 한 잔 마시기"])
    
    if st.button("얼음 녹이기"):
        st.balloons()
        st.write(f"'{option}'을(를) 선택하셨군요! 이 작은 행동이 기분을 변화시키는 시작입니다. [4]")
        add_inventory("활동의 온기")
        st.button("다음 지역으로: 화산 지역", on_click=lambda: change_page("화산"))

# --- Level 3: Volcano Province (감정 조절) ---
elif st.session_state.page == "화산":
    st.header("🌋 Level 3: 화산 지역 - 감정 다루기")
    st.write("강렬한 분노와 슬픔이 용암처럼 끓어오르고 있습니다. 감정을 조절하는 기술이 필요합니다. [5]")
    
    st.warning("기법: 자기 주장 및 감정 인식 (Emotional Regulation)")
    emotion_input = st.text_area("누군가 당신에게 상처를 주었을 때, '나'를 주어로 하여 건강하게 표현해 보세요 (예: 나는 네가 ~라고 말해서 속상해):")
    
    if st.button("열기 식히기"):
        if len(emotion_input) > 5:
            st.success("자신의 감정을 솔직하고 건강하게 표현하는 것은 매우 중요합니다! [2]")
            add_inventory("평정의 방패")
            st.button("다음 지역으로: 산맥 지역", on_click=lambda: change_page("산맥"))

# --- Level 4: Mountain Province (문제 해결) ---
elif st.session_state.page == "산맥":
    st.header("⛰️ Level 4: 산맥 지역 - 문제 해결하기")
    st.write("앞에 거대한 절벽이 가로막고 있습니다. STEPS 기법으로 길을 찾아봅시다. ")
    
    st.warning("기법: STEPS (Problem Solving)")
    col1, col2 = st.columns(2)
    with col1:
        s = st.text_input("S (Say): 해결하고 싶은 고민은?")
        t = st.text_input("T (Think): 생각나는 해결책 한 가지는?")
    with col2:
        e = st.text_input("E (Examine): 그 해결책의 장점은?")
        p = st.text_input("P (Pick): 지금 바로 시도해볼 것은?")
        
    if st.button("절벽 오르기"):
        if s and t and e and p:
            st.info("문제를 작게 쪼개면 정복할 수 있습니다. 마지막 S(See)는 실행 후 결과를 확인하는 단계입니다. [6, 2]")
            add_inventory("지혜의 밧줄")
            st.button("다음 지역으로: 늪지 지역", on_click=lambda: change_page("늪지"))

# --- Level 5: Swamp Province (생각 인식) ---
elif st.session_state.page == "늪지":
    st.header("🤢 Level 5: 늪지 지역 - 생각의 덫")
    st.write("이곳은 GNATs가 가장 많이 서식하는 곳입니다. 그들이 어떤 유형인지 파악해야 합니다. [5, 4]")
    
    st.warning("기법: 사고 오류 식별 (Identifying Cognitive Errors)")
    gnat_msg = "내가 시험에 떨어진 건 내가 원래 멍청해서야. 앞으로도 다 망칠 거야."
    st.chat_message("monster").write(f"GNAT: '{gnat_msg}'")
    
    gnat_type = st.radio("이 생각에 담긴 오류는 무엇일까요? [2]", 
                        ["전부 아니면 전무(흑백논리)", "낙인찍기(Labeling)", "재앙화(Catastrophizing)", "감정적 판단"])
    
    if st.button("진흙탕 탈출"):
        st.success(f"정답입니다! 이것은 '{gnat_type}'의 오류입니다. 생각을 객관적으로 보는 것만으로도 힘이 생깁니다. [7]")
        add_inventory("통찰의 등불")
        st.button("다음 지역으로: 다리 지역", on_click=lambda: change_page("다리"))

# --- Level 6: Bridgeland Province (생각 바꾸기) ---
elif st.session_state.page == "다리":
    st.header("🌉 Level 6: 다리 지역 - 생각 교체하기")
    st.write("부정적인 생각을 현실적인 생각으로 바꾸어 다리를 건너야 합니다. [6, 8]")
    
    st.warning("기법: 인지 재구성 (Cognitive Restructuring)")
    st.chat_message("monster").write("GNAT: '아무도 나를 좋아하지 않아. 나는 혼자야.'")
    
    new_thought = st.selectbox("이 생각을 어떻게 바꾸면(Swap) 좋을까요?", 
                              ["선택하세요...", 
                               "모두가 나를 좋아할 순 없지만, 나를 아껴주는 친구가 한 명이라도 있어.", 
                               "내가 먼저 연락하면 친구들도 반가워할 거야.", 
                               "지금은 외롭지만 이 기분은 곧 지나갈 거야."])
    
    if new_thought!= "선택하세요...":
        if st.button("다리 건너기"):
            st.success("완벽한 SPARX 사고입니다! 유연한 생각이 다리를 튼튼하게 만듭니다. [9, 10]")
            add_inventory("유연한 마음의 검")
            st.button("마지막 지역으로: 협곡 지역", on_click=lambda: change_page("협곡"))

# --- Level 7: Canyon Province (통합 및 복구) ---
elif st.session_state.page == "협곡":
    st.header("✨ Level 7: 협곡 지역 - 모두 함께 적용하기")
    st.write("여정의 마지막입니다. 지금까지 모은 보석들로 세상의 균형을 되찾으세요! [6, 2]")
    
    st.warning("기법: 마음챙김 및 재발 방지 (Mindfulness & Resilience)")
    st.write(f"용사 {st.session_state.user_name}님이 모은 보석: {', '.join(st.session_state.inventory)}")
    
    if st.button("최종 SPARX 해제"):
        st.balloons()
        st.snow()
        st.write("""
        ### 🎉 축하합니다! 세상을 구했습니다.
        당신은 이제 현실 세계에서도 **SPARX** 기술을 쓸 수 있습니다.
        - **S**mart (영리하게 오류 찾기)
        - **P**ositive (긍정적인 면 발견)
        - **A**ctive (작은 일부터 행동하기)
        - **R**ealistic (현실적으로 생각하기)
        - **X**-factor (나만의 강점 믿기)
        """)
        if st.button("다시 처음부터 연습하기"):
            st.session_state.clear()
            st.rerun()

# 5. 하단 풋노트
st.write("---")
st.caption("본 프로그램은 뉴질랜드 SPARX 게임의 임상 프로토콜을 기반으로 제작된 교육용 프로토토타입입니다. [11, 12, 2]")
