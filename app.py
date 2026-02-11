import streamlit as st

# 세션 상태 초기화 (게임 진행 상황 저장)
if 'level' not in st.session_state:
    st.session_state.level = 0
if 'mood' not in st.session_state:
    st.session_state.mood = 5
if 'steps_input' not in st.session_state:
    st.session_state.steps_input = {}

def next_level():
    st.session_state.level += 1

def reset_game():
    st.session_state.level = 0
    st.session_state.steps_input = {}

# 사이드바: 가이드의 조언 (The Guide)
st.sidebar.title("🕊️ SPARX 가이드")
if st.session_state.level == 0:
    st.sidebar.info("반가워요! 나는 당신의 여정을 도울 가이드입니다. 우울한 기분은 영원하지 않아요. 함께 균형을 되찾아 봅시다. [1, 2]")
elif st.session_state.level < 7:
    st.sidebar.success(f"현재 {st.session_state.level}단계 진행 중입니다. 당신은 잘하고 있어요!")
    st.sidebar.metric("나의 기분 점수", f"{st.session_state.mood}/10")

# 메인 게임 화면
st.title("🛡️ SPARX: 마음의 수호자")

# 레벨 0: 도입 및 아바타 설정
if st.session_state.level == 0:
    st.subheader("모험을 시작하기 전에")
    st.write("SPARX는 영리하고(Smart), 긍정적이고(Positive), 활동적이며(Active), 현실적인(Realistic) 사고를 통해 마음의 'X-인자'를 깨우는 여정입니다. [3, 4]")
    
    avatar = st.selectbox("당신의 아바타 스타일을 선택하세요:", ["용맹한 전사", "지혜로운 마법사", "민첩한 탐험가"])
    st.session_state.mood = st.slider("지금 기분이 어떠신가요? (0: 매우 우울, 10: 아주 좋음)", 0, 10, 5)
    
    if st.button("포털 진입하기"):
        next_level()
        st.rerun()

# 레벨 1: 동굴 지역 - GNATs 퇴치 (인지적 외재화)
elif st.session_state.level == 1:
    st.subheader("Level 1: 동굴 지역 - 희망 찾기")
    st.write("어두운 동굴 속에 'GNATs(우울하고 부정적인 자동적 사고)' 몬스터들이 나타났습니다! [5, 2]")
    
    gnat = st.radio("공격해오는 GNAT의 말을 선택하여 SPARX 사고로 물리치세요:", 
                   )
    
    if gnat == "너는 패배자야 (You're a loser)":
        answer = st.button("반격: '나는 지금 실수를 했을 뿐, 내 존재 자체가 패배자인 건 아니야!'")
    elif gnat == "이 일은 절대 나아지지 않아":
        answer = st.button("반격: '기분은 날씨처럼 변해. 지금은 비가 오지만 곧 갤 거야.'")
    else:
        answer = st.button("반격: '나를 아껴주는 사람들도 분명히 있어.'")
        
    if answer:
        st.balloons()
        st.success("GNAT을 물리쳤습니다! 당신의 마음속에 희망의 불꽃이 피어오릅니다. [6, 7]")
        st.button("다음 지역으로 이동", on_click=next_level)

# 레벨 2: 얼음 지역 - 행동 활성화
elif st.session_state.level == 2:
    st.subheader("Level 2: 얼음 지역 - 활동하기")
    st.write("이곳은 모든 것이 얼어붙었습니다. 활동을 통해 마을을 녹여야 합니다.")
    
    activity = st.selectbox("현실 세계에서 실천할 활동을 하나 골라보세요:", 
                            ["30분 동안 가볍게 산책하기", "좋아하는 노래 크게 듣기", "방 청소 조금만 하기"])
    
    if st.button("활동 계획 확정"):
        st.write(f"좋은 선택입니다! '{activity}'을(를) 실천하면 뇌에서 엔도르핀이 분비될 거예요. [8, 9]")
        st.button("얼음 녹이기 완료", on_click=next_level)

# 레벨 4: 산악 지역 - STEPS 문제 해결
elif st.session_state.level == 3: # 간단한 구현을 위해 레벨 4 기법을 3단계에 배치
    st.subheader("Level 4: 산악 지역 - 문제 해결 (STEPS)")
    st.write("앞에 거대한 절벽이 있습니다. STEPS 기법으로 문제를 해결해 봅시다. ")
    
    p = st.text_input("S (Say the problem): 지금 당신을 힘들게 하는 문제는 무엇인가요?")
    t = st.text_area("T (Think of solutions): 가능한 해결책들을 적어보세요.")
    
    if p and t:
        st.write("이제 장단점을 따져보고(E), 하나를 골라 시도하고(P), 결과를 확인(S)하면 됩니다!")
        if st.button("절벽 오르기 성공"):
            next_level()
            st.rerun()

# 최종 레벨: Canyon - 마무리
elif st.session_state.level == 4:
    st.subheader("최종 단계: 여정의 마무리")
    st.write("당신은 이제 스스로를 지킬 수 있는 SPARX 무기를 가졌습니다. [5, 11]")
    st.write("- **S**mart (영리하게)")
    st.write("- **P**ositive (긍정적으로)")
    st.write("- **A**ctive (활동적으로)")
    st.write("- **R**ealistic (현실적으로)")
    st.write("- **X**-factor (나만의 강점)")
    
    if st.button("처음부터 다시 연습하기"):
        reset_game()
        st.rerun()
