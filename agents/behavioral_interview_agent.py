"""Behavioral interview agent for Project 24."""

from agents.base import run_agent_task


def conduct_interview(session_id: str, context_data: dict) -> str:
    """Turn the target role into a set of useful interview prep prompts."""
    return run_agent_task(
        session_id=session_id,
        agent_name="Behavioral Interview Agent",
        context_data=context_data,
        objective=(
            "Prepare the candidate for likely behavioral interviews by mapping "
            "their goal to the stories and prompts they should practice first."
        ),
        sections=[
            "Core stories to prepare",
            "Sample behavioral questions",
            "Coaching notes",
        ],
        extra_guidance=(
            "Make the questions realistic and explain what a strong answer would "
            "need to prove."
        ),
    )
