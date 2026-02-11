import streamlit as st
import time

# --- 1. 세션 상태 초기화 (오류 방지를 위해 최상단 배치) ---
if 'page' not in st.session_state:
    st.session_state.page = "Intro"
if 'inventory' not in st.session_state:
    st.session_state.inventory = # 오류 수정됨: 빈 리스트로 초기화
if 'user_name' not in st.session_state:
    st.session_state.user_name = "용사"
if 'mood_score' not in st.session_state:
    st.session_state.mood_score = 5

# --- 2. 게임 유틸리티 함수 ---
def change_page(page_name):
    """페이지를 전환하고 화면을 새로고침합니다."""
    st.session_state.page = page_name
    st.rerun()

def collect_gem(gem_name):
    """새로운 보석을 인벤토리에 추가합니다."""
    if gem_name not in st.session_state.inventory:
        st.session_state.inventory.append(gem_name)
        st.toast(f"💎 새로운 마음의 보석 획득: {gem_name}")

# --- 3. 사이드바: 가이드 및 상태창 ---
with st.sidebar:
    st.title("🕊️ SPARX 가이드")
    st.image("https://cdn-icons-png.flaticon.com/512/3251/3251501.png", width=100)
    
    # 가이드의 따뜻한 조언 (The Guide's Voice) [2, 6]
    if st.session_state.page == "Intro":
        st.info("반가워요! 나는 당신의 여정을 도울 가이드입니다. 우울한 기분은 영원하지 않아요. ")
    else:
        st.success(f"할 수 있어요, {st.session_state.user_name}님! 당신은 혼자가 아닙니다. [2]")
    
    st.divider()
    # 진행도 표시
    provinces = ["Intro", "동굴", "얼음", "화산", "산맥", "늪지", "다리", "협곡"]
    try:
        current_step = provinces.index(st.session_state.page)
        st.write(f"**현재 위치:** {st.session_state.page} 지역")
        st.progress(current_step / (len(provinces) - 1))
    except ValueError:
        pass

    st.write(f"**나의 기분 점수:** {st.session_state.mood_score}/10")
    
    st.divider()
    st.subheader("🎒 보석 가방")
    if not st.session_state.inventory:
        st.write("아직 획득한 보석이 없습니다.")
    for item in st.session_state.inventory:
        st.write(f"✨ {item}")

# --- 4. 메인 게임 화면 로직 ---

# [도입] Intro: 캐릭터 생성 및 심리 교육
if st.session_state.page == "Intro":
    st.title("⚔️ K-SPARX: 마음의 수호자")
    st.markdown("---")
    st.write("이곳은 **GNATs(우울하고 부정적인 자동적 사고)**가 점령하여 빛을 잃은 세계입니다. [3, 4]")
    st.write("당신은 7개의 지역을 여행하며 마음을 치유하는 기술을 배우게 될 것입니다.")
    
    name_input = st.text_input("당신의 용사 이름을 알려주세요:", placeholder="이름을 입력하세요")
    st.session_state.mood_score = st.slider("지금 기분이 어떠신가요? (0: 매우 우울, 10: 아주 좋음)", 0, 10, 5)
    
    if st.button("모험 시작하기"):
        if name_input:
            st.session_state.user_name = name_input
            change_page("동굴")
        else:
            st.warning("이름을 입력해야 문이 열립니다!")

# [Level 1] Cave Province: 희망 찾기 및 이완 기법
elif st.session_state.page == "동굴":
    st.header("🕸️ Level 1: 동굴 지역 - 희망 찾기")
    st.write(f"가이드: '{st.session_state.user_name}님, 대부분의 사람들은 우울증에서 회복됩니다. '")
    st.write("어두운 동굴에서 마음을 진정시키기 위해 **복식 호흡**을 배워봅시다. ")
    
    with st.expander("🔵 복식 호흡 훈련 시작"):
        st.write("4초 동안 코로 깊게 숨을 들이마시고, 다시 4초 동안 천천히 내뱉으세요.")
        if st.button("호흡 훈련 완료"):
            st.balloons()
            collect_gem("희망의 불꽃")
            st.success("마음이 한결 차분해졌습니다!")
            st.button("얼음 지역으로 이동", on_click=lambda: change_page("얼음"))

# [Level 2] Ice Province: 행동 활성화 (Thawing the Ice)
elif st.session_state.page == "얼음":
    st.header("❄️ Level 2: 얼음 지역 - 활동하기")
    st.write("이곳은 우울함으로 인해 모든 것이 얼어붙었습니다. 몸을 움직여 마을을 녹여야 합니다. ")
    st.warning("기법: 행동 활성화 (Behavioral Activation)")
    
    activity = st.selectbox("마을을 녹이기 위해 오늘 실천할 수 있는 작은 활동은?", 
                            ["30분 산책하기", "방 청소 조금 하기", "친구에게 연락하기", "좋아하는 노래 듣기"])
    
    if st.button("얼음 녹이기 퀘스트 수행"):
        st.write(f"좋습니다! '{activity}' 활동은 뇌에서 천연 우울제인 엔도르핀을 나오게 합니다. [5]")
        collect_gem("활동의 온기")
        st.button("화산 지역으로 이동", on_click=lambda: change_page("화산"))

# [Level 3] Volcano Province: 감정 조절 (Strong Emotions)
elif st.session_state.page == "화산":
    st.header("🌋 Level 3: 화산 지역 - 감정 다루기")
    st.write("끓어오르는 분노와 슬픔을 다스려야 합니다. 자신의 감정을 건강하게 표현하는 법을 배웁니다. ")
    
    st.info("연습: '나'를 주어로 말하기 (I-Statement)")
    msg = st.text_input("누군가 당신의 기분을 상하게 했을 때, 어떻게 말하면 좋을까요?", 
                       placeholder="예: 나는 네가 ~라고 해서 조금 속상했어.")
    
    if st.button("용암 식히기"):
        if len(msg) > 5:
            st.success("자신의 감정을 인정하고 표현하는 것만으로도 감정의 파도를 조절할 수 있습니다. ")
            collect_gem("평정의 결정")
            st.button("산맥 지역으로 이동", on_click=lambda: change_page("산맥"))

# [Level 4] Mountain Province: 문제 해결 (STEPS)
elif st.session_state.page == "산맥":
    st.header("⛰️ Level 4: 산맥 지역 - 문제 해결하기")
    st.write("앞에 거대한 절벽이 있습니다. **STEPS 기법**을 사용하여 넘어가야 합니다. [6, 7]")
    
    col1, col2 = st.columns(2)
    with col1:
        s = st.text_input("S (Say): 당신을 힘들게 하는 구체적인 문제는?")
        t = st.text_area("T (Think): 가능한 해결책 3가지는?")
    with col2:
        e = st.text_input("E (Examine): 각 해결책의 장단점은?")
        p = st.text_input("P (Pick): 지금 당장 시도해볼 하나는?")
        
    if st.button("절벽 오르기 성공"):
        if s and t and e and p:
            st.info("문제를 한 걸음씩(Steps) 해결하면 거대한 절벽도 정복할 수 있습니다. [8]")
            collect_gem("지혜의 밧줄")
            st.button("늪지 지역으로 이동", on_click=lambda: change_page("늪지"))

# [Level 5] Swamp Province: 부정적 생각 인식 (GNATs)
elif st.session_state.page == "늪지":
    st.header("🤢 Level 5: 늪지 지역 - 생각의 덫 인식")
    st.write("이곳의 늪에는 GNATs 몬스터들이 숨어 있습니다. 그들의 정체를 파악하세요. ")
    
    st.chat_message("monster").write("GNAT: '너는 패배자야(You're a loser). 절대 아무것도 해내지 못할걸?' ")
    
    error_type = st.radio("이 GNAT가 사용하는 사고의 오류는 무엇일까요?", 
                         ["재앙화 (최악의 상황만 생각하기)", "낙인찍기 (부정적인 이름 붙이기)", "전부 아니면 전무(흑백논리)"])
    
    if st.button("정체 파악 완료"):
        st.success(f"맞습니다! '{error_type}'의 정체를 파악했습니다. 정체를 아는 것만으로도 GNAT은 약해집니다. [9]")
        collect_gem("통찰의 등불")
        st.button("다리 지역으로 이동", on_click=lambda: change_page("다리"))

# [Level 6] Bridgeland Province: 생각 바꾸기 (Cognitive Restructuring)
elif st.session_state.page == "다리":
    st.header("🌉 Level 6: 다리 지역 - 생각 교체하기")
    st.write("끊어진 다리를 잇기 위해 부정적인 생각을 **SPARX 사고**로 교체(Swap)해야 합니다. [6, 10]")
    
    st.chat_message("monster").write("GNAT: '아무도 나를 좋아하지 않아. 나는 평생 혼자일 거야.' ")
    
    swap = st.selectbox("이 생각을 어떻게 바꾸는 것이 현실적이고 도움이 될까요?", 
                       ["선택하세요...", 
                        "가끔 외로울 수 있지만, 나를 아껴주는 친구와 가족이 분명히 있어.", 
                        "모든 사람이 나를 좋아할 순 없어. 그건 자연스러운 일이야.", 
                        "기분은 날씨처럼 변해. 지금은 외롭지만 곧 괜찮아질 거야."])
    
    if swap!= "선택하세요...":
        if st.button("다리 복구하기"):
            st.success("유연한 사고가 다리를 튼튼하게 만들었습니다! [11]")
            collect_gem("유연한 마음의 검")
            st.button("협곡 지역으로 이동", on_click=lambda: change_page("협곡"))

# [Level 7] Canyon Province: 통합 및 재발 방지
elif st.session_state.page == "협곡":
    st.header("✨ Level 7: 협곡 지역 - 여정의 마무리")
    st.write("드디어 마지막 지역입니다. 지금까지 모은 6개의 보석을 하나로 합쳐야 합니다. [8, 1]")
    
    if len(st.session_state.inventory) < 6:
        st.warning("아직 보석을 모두 모으지 못했습니다. 이전 단계들을 완료해 주세요.")
    
    if st.button("최종 SPARX 기술 발동"):
        st.balloons()
        st.snow()
        st.markdown("""
        ### 🎉 축하합니다! 마음의 수호자님.
        세상에 다시 빛이 돌아왔습니다. 당신은 이제 현실 세계에서도 **SPARX** 기술을 사용할 준비가 되었습니다!
        - **S**mart (영리하게 GNATs 찾아내기)
        - **P**ositive (긍정적인 면에 집중하기)
        - **A**ctive (작은 일부터 행동하기)
        - **R**ealistic (현실적으로 생각하기)
        - **X**-factor (나만의 강점 믿기)
        
        [12, 11, 13]
        """)
        if st.button("처음부터 다시 연습하기"):
            st.session_state.clear()
            st.rerun()

# --- 5. 푸터 ---
st.divider()
st.caption("※ 본 프로그램은 뉴질랜드 오클랜드 대학교의 SPARX 게임 임상 가이드라인을 바탕으로 제작되었습니다. [14, 15, 1]")
