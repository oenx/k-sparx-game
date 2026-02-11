import streamlit as st
from dataclasses import dataclass
from typing import List

st.set_page_config(page_title="K-SPARX Game Design", layout="wide")

# -----------------------------
# Data Models
# -----------------------------

@dataclass
class CBTModule:
    title: str
    theme: str
    goal: str
    skills: List[str]
    quest: str


modules = [
    CBTModule(
        title="레벨 1: 희망 찾기",
        theme="동굴 지역",
        goal="우울증 이해 및 희망 형성",
        skills=["심리교육", "복식호흡", "GNATs 개념 이해"],
        quest="어둠 속에서 희망의 빛 찾기",
    ),
    CBTModule(
        title="레벨 2: 행동 활성화",
        theme="얼음 지역",
        goal="활동 증가로 기분 변화 유도",
        skills=["활동 계획", "점진적 근육 이완", "기초 의사소통"],
        quest="얼어붙은 마을 녹이기",
    ),
    CBTModule(
        title="레벨 3: 감정 다루기",
        theme="화산 지역",
        goal="강렬한 감정 조절",
        skills=["감정 인식", "자기 주장", "협상 기술"],
        quest="폭발하는 화산 안정시키기",
    ),
    CBTModule(
        title="레벨 4: 문제 해결",
        theme="산악 지역",
        goal="체계적 문제 해결 습득",
        skills=["STEPS 모델", "의사결정", "실행 평가"],
        quest="절벽을 넘어 정상 도달",
    ),
    CBTModule(
        title="레벨 5: 사고 인식",
        theme="늪지 지역",
        goal="왜곡된 사고 발견",
        skills=["인지 오류 탐색", "메타인지"],
        quest="늪의 속삭임 정체 파악",
    ),
    CBTModule(
        title="레벨 6: 사고 전환",
        theme="다리 지역",
        goal="부정적 사고 재구성",
        skills=["증거 찾기", "대안 사고 생성"],
        quest="무너진 다리 복원",
    ),
    CBTModule(
        title="레벨 7: 통합과 회복",
        theme="협곡 지역",
        goal="기술 통합 및 재발 예방",
        skills=["마음챙김", "회복탄력성", "자기 돌봄"],
        quest="최종 협곡을 건너 귀환",
    ),
]


# -----------------------------
# Sidebar Navigation
# -----------------------------

st.sidebar.title("K‑SPARX 설계")
page = st.sidebar.radio(
    "메뉴 선택",
    [
        "프로젝트 개요",
        "CBT 모듈 설계",
        "GNATs 변환 연습",
        "게임 시스템 구조",
        "개발 로드맵",
    ],
)


# -----------------------------
# Page 1 – Overview
# -----------------------------

if page == "프로젝트 개요":
    st.title("한국형 디지털 CBT 게임 – K‑SPARX")

    st.markdown(
        """
        ### 목표
        한국 청년의 우울·불안 완화를 위한 **디지털 치료형 게임 콘텐츠** 기획

        ### 핵심 특징
        - 인지행동치료 기반 7단계 구조
        - 판타지 세계관 + 심리 훈련 결합
        - 모바일 중심 인터랙티브 설계
        - 현실 행동 변화 유도 시스템
        """
    )

    st.info("이 Streamlit 문서는 게임기획서이자 인터랙티브 설계 프로토타입입니다.")


# -----------------------------
# Page 2 – CBT Modules
# -----------------------------

elif page == "CBT 모듈 설계":
    st.title("7단계 CBT 게임 구조")

    selected = st.selectbox("레벨 선택", modules, format_func=lambda x: x.title)

    st.subheader(selected.title)
    st.write(f"**지역 테마:** {selected.theme}")
    st.write(f"**치료 목표:** {selected.goal}")
    st.write(f"**핵심 퀘스트:** {selected.quest}")

    st.markdown("#### 학습 기술")
    for skill in selected.skills:
        st.write(f"- {skill}")


# -----------------------------
# Page 3 – GNATs Practice
# -----------------------------

elif page == "GNATs 변환 연습":
    st.title("부정적 사고 → SPARX 사고 변환")

    negative = st.text_area("현재 떠오르는 부정적 생각 입력")

    if st.button("SPARX 사고 생성"):
        if negative.strip() == "":
            st.warning("문장을 입력하세요.")
        else:
            positive = (
                "이 생각이 완전히 사실인지 증거를 살펴보고, "
                "지금 할 수 있는 작은 행동에 집중해 보자."
            )

            st.success("재구성된 사고")
            st.write(positive)


# -----------------------------
# Page 4 – Game System
# -----------------------------

elif page == "게임 시스템 구조":
    st.title("게임 메커닉 설계")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("플레이 루프")
        st.markdown(
            """
            1. 감정 체크
            2. CBT 퀘스트 수행
            3. GNAT 전투
            4. 현실 숙제 제시
            5. 피드백 시각화
            """
        )

    with col2:
        st.subheader("보상 시스템")
        st.markdown(
            """
            - 감정 회복 게이지
            - 희망의 조각 수집
            - 아바타 성장
            - 스토리 해금
            """
        )


# -----------------------------
# Page 5 – Roadmap
# -----------------------------

elif page == "개발 로드맵":
    st.title("개발 단계 계획")

    roadmap = {
        "1단계": "기획 및 CBT 구조 설계",
        "2단계": "Streamlit 인터랙션 프로토타입",
        "3단계": "모바일 앱 전환 (Flutter/Unity)",
        "4단계": "임상 파일럿 테스트",
        "5단계": "정식 서비스 출시",
    }

    for k, v in roadmap.items():
        st.write(f"**{k}** – {v}")

    st.progress(20)
