"""Orchestrator for Project 24."""

import os
import sys
from typing import Any, Dict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from agents.base import generate_session_id, log_agent_response
from agents.resume_optimizer_agent import optimize_resume
from agents.behavioral_interview_agent import conduct_interview
from agents.role_fit_analyzer_agent import analyze_fit

AGENT_SEQUENCE = (
    ("Resume Optimizer Agent", optimize_resume),
    ("Behavioral Interview Agent", conduct_interview),
    ("Role-Fit Analyzer", analyze_fit),
)


class Orchestrator:
    """Coordinate the career-coaching specialists in one pass."""

    def generate_session_id(self) -> str:
        return generate_session_id()

    def run_workflow(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        session_id = self.generate_session_id()
        results = {}

        log_agent_response(
            session_id,
            "Workflow Input",
            "\n".join(
                f"- {key.replace('_', ' ').title()}: {value or 'Not provided'}"
                for key, value in inputs.items()
            ),
            {"kind": "input"},
        )

        for agent_name, agent_runner in AGENT_SEQUENCE:
            results[agent_name] = agent_runner(session_id, inputs)

        return {"session_id": session_id, "results": results}
