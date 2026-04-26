"""Role-fit analyzer agent for Project 24."""

from agents.base import run_agent_task


def analyze_fit(session_id: str, context_data: dict) -> str:
    """Estimate where the current candidate story already fits and where it does not."""
    return run_agent_task(
        session_id=session_id,
        agent_name="Role-Fit Analyzer",
        context_data=context_data,
        objective=(
            "Compare the candidate's current material to the stated career goal "
            "and identify both fit signals and the gaps that still need work."
        ),
        sections=[
            "Match signals",
            "Gaps to address",
            "Targeted next actions",
        ],
        extra_guidance=(
            "Be candid but supportive. This should read like coaching a real job "
            "seeker, not scoring them from a distance."
        ),
    )
