import streamlit as st
import sys
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PACKAGE_ROOT = os.path.dirname(os.path.dirname(PROJECT_ROOT))
sys.path.insert(0, PROJECT_ROOT)
if PACKAGE_ROOT not in sys.path:
    sys.path.insert(0, PACKAGE_ROOT)

from agents.base import get_session_history
from orchestrator import Orchestrator
from components import render_app_footer, run_with_status_updates

st.set_page_config(page_title="Resume & Interview Coach", layout="wide")


def render_session_log(session_id: str) -> None:
    """Render the collaboration log so the coaching flow stays inspectable."""
    history = get_session_history(session_id)
    if not history:
        return

    st.subheader("Collaboration Log")
    for entry in history:
        timestamp = entry["timestamp"].replace("T", " ")
        with st.expander(f"{entry['agent']} · {timestamp}", expanded=False):
            st.markdown(entry["content"])


def main():
    st.title("Resume & Interview Coach")
    st.caption("Help job seekers prepare with feedback and mock interviews.")

    st.sidebar.title("Career Inputs")
    career_goal = st.sidebar.text_input(
        "Career Goal",
        placeholder="AI product manager role at a healthcare startup",
    )
    resume_text = st.text_area(
        "Resume Text",
        height=240,
        placeholder="Paste the current resume or a short career summary here.",
    )

    if st.button("Run Coaching Team", type="primary"):
        if not resume_text.strip() and not career_goal.strip():
            st.warning("Add a resume summary or a career goal so the agents can coach against something concrete.")
            return

        inputs = {
            "resume_text": resume_text.strip(),
            "career_goal": career_goal.strip(),
        }
        orch = Orchestrator()
        output = run_with_status_updates(
            lambda: orch.run_workflow(inputs),
            start_message="Agents are preparing career coaching feedback..."
        )

        st.success(f"Workflow Complete! Session ID: {output['session_id']}")

        for agent, response in output["results"].items():
            with st.expander(f"{agent} Response", expanded=True):
                st.markdown(response)

        render_session_log(output["session_id"])


    render_app_footer()

if __name__ == "__main__":
    main()
