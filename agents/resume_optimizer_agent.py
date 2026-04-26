"""Resume optimizer agent for Project 24."""

from agents.base import run_agent_task


def optimize_resume(session_id: str, context_data: dict) -> str:
    """Highlight the strongest resume edits for the target role."""
    return run_agent_task(
        session_id=session_id,
        agent_name="Resume Optimizer Agent",
        context_data=context_data,
        objective=(
            "Review the candidate's resume material and career goal, then point "
            "to the most valuable edits that would improve positioning."
        ),
        sections=[
            "Strongest current signals",
            "Resume rewrite priorities",
            "Missing proof points",
        ],
        extra_guidance=(
            "Focus on measurable impact, positioning, and clearer storytelling. "
            "If the resume text is short, say what details would strengthen it."
        ),
    )
