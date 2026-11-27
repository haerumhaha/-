import streamlit as st

# 1. 페이지 기본 설정 및 모던 MBTI 디자인 CSS 적용
st.set_page_config(page_title="대학생활 성향 유형 테스트", page_icon="🎓", layout="centered")

st.markdown("""
    <style>
    .stApp {
        background-color: #f8fafc;
    }
    
    /* 상단 MBTI 헤더 */
    .mbti-header {
        text-align: center;
        padding: 10px 0 20px 0;
    }
    .mbti-header h2 {
        font-size: 24px !important;
        font-weight: 800 !important;
        color: #4f46e5 !important;
        margin-bottom: 4px !important;
    }
    .mbti-header p {
        color: #64748b;
        font-size: 14px;
        margin: 0;
    }

    /* 질문 전용 카드 상자 */
    .q-box {
        background-color: #ffffff;
        padding: 32px 24px;
        border-radius: 20px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
        text-align: center;
        margin-top: 10px;
        margin-bottom: 20px;
    }
    .q-box h3 {
        color: #0f172a;
        font-size: 20px !important;
        font-weight: 700 !important;
        line-height: 1.5 !important;
        margin: 0 !important;
    }

    /* MBTI 결과 카드 스타일 */
    .mbti-result-card {
        background: linear-gradient(135deg, #ffffff 0%, #f5f3ff 100%);
        padding: 36px 28px;
        border-radius: 24px;
        border: 2px solid #6366f1;
        box-shadow: 0 20px 25px -5px rgba(99, 102, 241, 0.15);
        text-align: center;
        margin-top: 10px;
    }
    .mbti-badge {
        display: inline-block;
        background: #4f46e5;
        color: #ffffff;
        font-size: 15px;
        font-weight: 800;
        padding: 6px 18px;
        border-radius: 30px;
        letter-spacing: 1px;
        margin-bottom: 14px;
    }
    .mbti-title {
        font-size: 26px;
        font-weight: 800;
        color: #1e1b4b;
        margin-bottom: 20px;
    }
    .mbti-desc {
        font-size: 15px;
        line-height: 1.8;
        color: #334155;
        text-align: left;
        background: #ffffff;
        padding: 20px;
        border-radius: 16px;
        border: 1px solid #e0e7ff;
        white-space: pre-line;
    }
    </style>
""", unsafe_allow_html=True)


# ====================================================
# 1. 클래스 적용 (Class) & 자료구조 (dict, tuple, list)
# ====================================================
class UniversityMBTITest:
    def __init__(self):
        # 딕셔너리(dict) 및 튜플(tuple) 자료구조 - 원본 데이터 100% 보존
        self.dataset = {
            "questions": (
                "1. 과제가 일주일 뒤까지라면 나는?", 
                "2. 시험기간 공부 방식은?", 
                "3. 해야 할 일이 여러 개 있을 때 나는?", 
                "4. 팀플 과제가 주어지면?", 
                "5. 수업 과제를 제출할 때 나는?",
                "6. 새로운 수업에서 아는 사람이 없다면?",
                "7. 공강 시간이 생겼다면?",
                "8. 대학생활에서 인간관계는?",
                "9. 조별 활동을 할 때 나는?",
                "10. 동아리나 학과 행사에 참석할 때는?",
                "11. 대학생활에서 가장 중요하다고 생각하는 것은?",
                "12. 공강 시간이 두 시간 생겼다면?",
                "13. 방학 계획을 세울 때 나는?",
                "14. 동아리 활동과 시험공부 일정이 겹친다면?",
                "15. 졸업할 때 가장 남기고 싶은 것은?",
                "16. 하루에 일정이 없는 시간이 생기면?",
                "17. 공강이 길게 생겼을 때 나는?",
                "18. 일주일 일정표를 보면?",
                "19. 주말에는?",
                "20. 여러 활동을 동시에 할 기회가 생기면?"
            ),
            "answersA": (
                "받은 날부터 조금씩 시작한다.",
                "시험 일정에 맞춰 미리 계획을 세워 공부한다.",
                "우선순위를 정하고 하나씩 처리한다",
                "초반에 역할과 일정을 정해두는 편이다.",
                "마감 전에 여유 있게 제출하려고 한다.",
                "주변 사람에게 먼저 말을 걸어보는 편이다.",
                "친구를 불러 함께 밥을 먹거나 시간을 보낸다.",
                "다양한 사람을 알아가는 것이 중요하다고 생각한다.",
                "조원들과 대화하고 의견을 적극적으로 나누는 편이다",
                "새로운 사람을 만나는 것이 기대된다.",
                "좋은 학점과 취업 준비이다.",
                "과제, 공부, 자격증 준비 등에 사용한다.",
                "자격증, 인턴, 공부 등 미래 준비를 우선한다.",
                "시험공부를 우선한다.",
                "좋은 학점과 취업에 도움이 되는 경력이다.",
                "새로운 할 일이나 약속을 잡는 편이다",
                "공부, 운동, 동아리 등 다른 활동을 한다.",
                "일정이 어느 정도 차 있어야 만족스럽다.",
                "약속이나 활동을 계획해서 보내는 편이다",
                "가능하면 최대한 참여하려고 한다."
            ),
            "answersB": (
                "마감이 가까워져야 본격적으로 시작한다.",
                "시험 직전에 집중해서 몰아서 공부한다.",
                "가장 급한 일이 생길 때마다 그때그때 처리한다.",
                "마감일이 가까워져야 속도가 붙는 편이다.",
                "제출 마감 직전까지 수정하거나 미룬다.",
                "굳이 먼저 말을 걸지 않아도 괜찮다.",
                "혼자 밥을 먹거나 개인 시간을 보낸다.",
                "몇 명의 친한 사람만 있어도 충분하다고 생각한다.",
                "맡은 역할을 혼자 집중해서 처리하는 편이다.",
                "친한 사람이 없다면 참여가 조금 부담스럽다.",
                "다양한 경험과 추억을 쌓는 것이다.",
                "친구를 만나거나 카페, 취미 활동을 즐긴다.",
                "여행, 취미, 새로운 경험을 우선한다.",
                "중요한 동아리 활동이라면 참여한다.",
                "다양한 사람들과 만든 추억과 경험이다.",
                "아무 일정 없이 쉬는 시간이 좋다.",
                "카페에서 쉬거나 집에 가고 싶어진다.",
                "비어 있는 시간이 많아야 마음이 편하다.",
                "특별한 계획 없이 쉬는 것을 좋아한다.",
                "꼭 필요한 것만 하고 여유를 남긴다."
            )
        }
        
        # 16가지 결과 유형 딕셔너리 - 원본 텍스트 100% 보존
        self.results_info = {
            "PSGB": ("학점 사수형", "공부와 과제를 미리 계획해서 준비하고, 주변 사람들과도 잘 어울리는 유형이다.\n\n대학생활에서 학점과 진로를 중요하게 생각하며 공강이나 여유 시간도 공부, 자격증, 대외활동 등에 활용하는 편이다."),
            "PSGR": ("출석 만점형", "수업과 과제를 계획적으로 챙기고 친구들과도 원만하게 지내는 유형이다.\n\n학점과 학교생활을 성실하게 관리하지만 지나치게 많은 활동을 하기보다는 안정적인 생활을 선호한다."),
            "PSEB": ("새내기 행사 올참형", "공부와 일정은 계획적으로 관리하면서도 학과 행사, 동아리, 축제 등 대학생활의 다양한 활동에 적극적으로 참여하는 유형이다.\n\n학교에서 할 수 있는 경험을 최대한 많이 해보려는 편이다."),
            "PSER": ("낭만 대학생형", "기본적인 학업은 계획적으로 챙기면서 친구들과의 추억, 축제, 여행, 카페 등 대학생활의 즐거움을 중요하게 생각하는 유형이다.\n\n바쁘게 모든 활동에 참여하기보다는 여유롭게 대학생활을 즐긴다."),
            "PIGB": ("취업 준비형", "혼자 공부하거나 준비하는 것을 선호하며 자격증, 학점, 취업 준비 등 자신의 목표를 체계적으로 관리하는 유형이다.\n\n남들과 어울리는 것보다 자신의 계획을 달성하는 데 집중하는 편이다."),
            "PIGR": ("도서관 상주형", "혼자 조용히 공부하는 것을 좋아하고 학점과 진로도 꾸준히 관리하는 유형이다.\n\n많은 활동에 참여하기보다는 도서관이나 카페 등에서 자신의 페이스대로 공부하는 것을 선호한다."),
            "PIEB": ("대외활동 수집형", "혼자 행동하는 것에 익숙하고 계획적으로 생활하지만 새로운 프로젝트, 공모전, 대외활동 등 다양한 경험에는 적극적으로 참여하는 유형이다.\n\n관심 있는 활동에는 많은 시간을 투자하는 편이다."),
            "PIER": ("혼밥 마스터형", "혼자 밥을 먹거나 공부하는 것을 자연스럽게 생각하고 자신의 생활을 계획적으로 관리하는 유형이다.\n\n대학생활에서 지나치게 많은 활동이나 인간관계보다는 개인 시간과 여유를 중요하게 생각한다."),
            "CSGB": ("팀플 캐리형", "평소에는 일을 미루는 경우가 있지만 필요할 때 집중력을 발휘하고 사람들과 협력하는 데 능숙한 유형이다.\n\n목표가 생기면 적극적으로 움직이며 팀플이나 과제에서 중요한 역할을 맡기도 한다."),
            "CSGR": ("과제 미루기형", "친구들과 어울리는 것을 좋아하지만 공부나 과제는 마감이 가까워져야 시작하는 경우가 많은 유형이다.\n\n해야 할 일은 결국 처리하지만 최대한 여유롭게 생활하려는 편이다."),
            "CSEB": ("인맥 확장형", "공부는 벼락치기하는 경우가 많지만 새로운 사람을 만나거나 동아리, 행사 등에 참여하는 것을 좋아하는 유형이다.\n\n대학생활에서 다양한 사람들과의 관계와 경험을 중요하게 생각한다."),
            "CSER": ("동아리 올인형", "학업보다는 친구, 동아리, 축제 등 사람들과 함께하는 대학생활을 중요하게 생각하는 유형이다.\n\n시험이나 과제는 미루는 경우가 많고 활동과 인간관계에 많은 시간을 사용하는 편이다."),
            "CIGB": ("벼락치기형", "혼자 공부하는 것을 선호하고 평소에는 과제나 시험 준비를 미루지만 마감 직전에 높은 집중력을 발휘하는 유형이다.\n\n학점이나 목표는 중요하게 생각하기 때문에 필요한 순간에는 몰아서 공부한다."),
            "CIGR": ("공강 낭비형", "혼자 있는 것을 편하게 생각하고 일정이나 과제를 미리 준비하기보다는 그때그때 처리하는 유형이다.\n\n공강이 생겨도 특별한 계획 없이 쉬거나 시간을 보내는 경우가 많다."),
            "CIEB": ("과방 지박령형", "정해진 계획에 따라 움직이기보다는 자신이 관심 있는 활동이나 사람들과 어울리는 것을 중요하게 생각하는 유형이다.\n\n학교 안에서 자유롭게 시간을 보내거나 관심 있는 활동에 갑자기 몰입하는 경우가 많다."),
            "CIER": ("자체휴강형", "공부나 과제를 미리 준비하는 편이 아니며 혼자 있는 시간과 여유를 중요하게 생각하는 유형이다.\n\n학교생활에 필요한 만큼만 참여하고 공강이나 빈 시간이 생기면 집이나 기숙사에서 쉬는 것을 선호한다.")
        }

    # ====================================================
    # 2. 함수 정의 (def), 반복문 (while, for), 조건문 (if/elif/else)
    # ====================================================
    def calculate_mbti(self, user_answers_list):
        # 리스트(list) 자료구조 적용
        response = [0, 0, 0, 0]
        idx = 0
        
        # while 반복문 사용
        while idx < len(user_answers_list):
            ans = user_answers_list[idx]
            
            # 조건문 (if/elif/else) 적용
            if ans == "A":
                score = 1
            else:
                score = -1

            if idx < 5:
                response[0] += score
            elif idx < 10:
                response[1] += score
            elif idx < 15:
                response[2] += score
            else:
                response[3] += score
            
            idx += 1

        isP = response[0] > 0
        isS = response[1] > 0
        isG = response[2] > 0
        isB = response[3] > 0

        mbti_code = ""
        mbti_code += "P" if isP else "C"
        mbti_code += "S" if isS else "I"
        mbti_code += "G" if isG else "E"
        mbti_code += "B" if isB else "R"

        return mbti_code, self.results_info.get(mbti_code, ("알 수 없음", "결과를 찾을 수 없습니다."))


# 인스턴스 객체 생성
app = UniversityMBTITest()

# ====================================================
# 3. 세션 상태 관리 (페이지 이동)
# ====================================================
if "current_q" not in st.session_state:
    st.session_state.current_q = 0

if "user_answers" not in st.session_state:
    st.session_state.user_answers = ["A"] * 20

# 상단 헤더
st.markdown("""
    <div class="mbti-header">
        <h2>🎓 대학생활 성향 유형 테스트</h2>
        <p>나의 대학생활 스타일을 MBTI 검사처럼 확인해보세요!</p>
    </div>
""", unsafe_allow_html=True)

total_q = len(app.dataset["questions"])
current_idx = st.session_state.current_q

# ----------------------------------------------------
# 화면 1: 질문 카드 화면 ([이전] / [다음] 페이지 이동 지원)
# ----------------------------------------------------
if current_idx < total_q:
    progress_val = (current_idx + 1) / total_q
    st.progress(progress_val)
    st.caption(f"✨ **Q{current_idx + 1} / Q{total_q}** (진행률 {(progress_val * 100):.0f}%)")

    q_text = app.dataset["questions"][current_idx]
    ans_a = app.dataset["answersA"][current_idx]
    ans_b = app.dataset["answersB"][current_idx]

    # 질문 상자
    st.markdown(f'<div class="q-box"><h3>{q_text}</h3></div>', unsafe_allow_html=True)

    saved_choice = st.session_state.user_answers[current_idx]
    default_index = 0 if saved_choice == "A" else 1

    selected_option = st.radio(
        "선택지:",
        options=["A", "B"],
        format_func=lambda x: f"A. {ans_a}" if x == "A" else f"B. {ans_b}",
        index=default_index,
        key=f"radio_q_{current_idx}",
        label_visibility="collapsed"
    )

    st.write("")
    col1, col2 = st.columns([1, 1])

    # 이전 버튼
    with col1:
        if current_idx > 0:
            if st.button("⬅️ 이전 질문", use_container_width=True):
                st.session_state.user_answers[current_idx] = selected_option
                st.session_state.current_q -= 1
                st.rerun()

    # 다음 / 결과 버튼
    with col2:
        btn_label = "결과 확인하기 🚀" if current_idx == total_q - 1 else "다음 질문 ➡️"
        if st.button(btn_label, type="primary", use_container_width=True):
            st.session_state.user_answers[current_idx] = selected_option
            st.session_state.current_q += 1
            st.rerun()

# ----------------------------------------------------
# 화면 2: MBTI 스타일 결과 화면
# ----------------------------------------------------
else:
    mbti_code, (title, desc) = app.calculate_mbti(st.session_state.user_answers)

    st.balloons()
    
    st.markdown(f"""
        <div class="mbti-result-card">
            <span class="mbti-badge">{mbti_code}</span>
            <div class="mbti-title">{title}</div>
            <div class="mbti-desc">{desc}</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    st.caption("※ 본 테스트는 단순 성향 참고용으로 제공됩니다.")
    st.divider()

    if st.button("🔄 다시 테스트하기", use_container_width=True):
        st.session_state.current_q = 0
        st.session_state.user_answers = ["A"] * 20
        st.rerun()
