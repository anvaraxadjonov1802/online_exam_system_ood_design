from typing import List
from .question import Question


class Exam:
    def __init__(self, exam_id: str, title: str, duration_minutes: int, questions: List[Question]):
        self.id = exam_id
        self.title = title
        self.duration_minutes = duration_minutes
        self.questions = questions
