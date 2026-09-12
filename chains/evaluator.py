#feedback chain

from pydantic import BaseModel, Field
from typing import List, Optional

class AnswerFeedback(BaseModel):
    """Structured feedback for a single answer."""

    score: int = Field(
        description="Score from 1-10 (1=poor, 10=excellent)",
        ge=1,
        le=10
    )
    understanding: str = Field(
        description="Assessment of conceptual understanding"
    )
    communication: str = Field(
        description="How well they explained their answer"
    )
    strengths: List[str] = Field(
        description="Specific things the candidate did well"
    )
    improvements: List[str] = Field(
        description="Specific areas to improve"
    )
    follow_up_question: Optional[str] = Field(
        description="A follow-up question to probe deeper",
        default=None
    )

class InterviewReport(BaseModel):
    """Final interview evaluation report."""

    overall_score: int = Field(ge=1, le=10)
    recommendation: str = Field(
        description="hire / maybe / no_hire"
    )
    summary: str = Field(
        description="2-3 sentence overall assessment"
    )
    technical_skills: int = Field(ge=1, le=10)
    communication_skills: int = Field(ge=1, le=10)
    problem_solving: int = Field(ge=1, le=10)
    strengths: List[str]
    areas_to_improve: List[str]
    suggested_topics_to_study: List[str]