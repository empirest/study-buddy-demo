import streamlit as st
from openai import OpenAIError

from ai_client import (
    answer_follow_up,
    explain_api_error,
    generate_summary,
    is_live_configured,
)
from sample_responses import preview_notice


st.set_page_config(page_title="Study Buddy", page_icon="📚", layout="centered")

st.markdown(
    """
    <style>
    :root {
        --study-ink: #20352e;
        --study-green: #547a62;
        --study-border: #d5e2d7;
    }
    .stApp {
        background: linear-gradient(145deg, #f2f7f1 0%, #eaf3e9 100%);
        color: var(--study-ink);
    }
    .block-container {
        max-width: 820px;
        padding-top: 2.5rem;
        padding-bottom: 3rem;
    }
    .study-wordmark {
        color: var(--study-ink);
        font-family: Georgia, "Palatino Linotype", "Book Antiqua", serif;
        font-size: 2.6rem;
        font-weight: 700;
        letter-spacing: -0.04em;
        line-height: 1.15;
    }
    [data-testid="stChatMessage"] {
        border: 1px solid var(--study-border);
        border-radius: 1rem;
        padding: 0.8rem 1rem;
        background-color: rgba(255, 255, 255, 0.84);
    }
    div.stButton > button {
        border-radius: 999px;
        border-color: #a9c5ae;
        color: #355643;
        background-color: rgba(255, 255, 255, 0.82);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="study-wordmark">Study Buddy</div>', unsafe_allow_html=True)
st.caption("A calm place to turn your study material into understanding.")
key_available = is_live_configured()
use_live_ai = st.toggle(
    "Enable live AI (may use paid API credits)",
    value=False,
    help="Leave this off to explore the app without sending text to the AI provider.",
)
live_mode = key_available and use_live_ai
if live_mode:
    st.success(
        "API key detected. Study requests will be sent to OpenAI; successful "
        "responses also require available API quota."
    )
else:
    st.info(
        "Demo mode is active. Your text is not analyzed and no API request is "
        "sent. Turn on live AI only if you want to use API credits."
    )

if "messages" not in st.session_state:
    st.session_state.messages = []
if "study_text" not in st.session_state:
    st.session_state.study_text = ""

if not st.session_state.messages:
    st.subheader("What are you studying?")
    st.write("Try a topic, or paste your own chapter or notes below.")
    suggestions = ["Geometry", "Biology", "Chemistry"]
    columns = st.columns(len(suggestions))
    for column, topic in zip(columns, suggestions):
        if column.button(topic, use_container_width=True):
            st.session_state.study_input = f"Help me study {topic.lower()}."

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if st.session_state.study_text:
    st.subheader("Ways to study this")
    study_actions = [
        (
            "Explain more",
            "Explain one key idea from my study material in simpler terms.",
        ),
        (
            "Make flashcards",
            "Create five concise question-and-answer flashcards from my study "
            "material. Keep them in this chat as text.",
        ),
        (
            "Start a short quiz",
            "Create a short three-question practice quiz from my study "
            "material. Ask one question at a time, wait for my answer, and "
            "then tell me whether it is correct before continuing. Keep it "
            "in this chat; do not create a separate quiz or score screen.",
        ),
    ]
    action_columns = st.columns(len(study_actions))
    for column, (label, prompt) in zip(action_columns, study_actions):
        if column.button(label, use_container_width=True, key=f"action_{label}"):
            st.session_state.pending_study_prompt = prompt

with st.form("study_input_form", clear_on_submit=True):
    study_text = st.text_area(
        "Study material or question",
        key="study_input",
        height=180,
        placeholder="Paste a chapter or study passage here...",
    )
    submitted = st.form_submit_button("Send", type="primary")

pending_study_prompt = st.session_state.pop("pending_study_prompt", None)
if submitted or pending_study_prompt is not None:
    text = pending_study_prompt or study_text.strip()
    if not text:
        st.warning("Please paste some study text before sending.")
    else:
        previous_messages = list(st.session_state.messages)
        st.session_state.messages.append({"role": "user", "content": text})
        if not st.session_state.study_text:
            st.session_state.study_text = text

        if not live_mode:
            reply = preview_notice()
        else:
            try:
                with st.spinner("Thinking through your study material..."):
                    if len(previous_messages) == 0:
                        reply = generate_summary(st.session_state.study_text)
                    else:
                        reply = answer_follow_up(
                            st.session_state.study_text,
                            previous_messages,
                            text,
                        )
            except OpenAIError as error:
                reply = explain_api_error(error)
                st.warning(reply)

        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.rerun()
