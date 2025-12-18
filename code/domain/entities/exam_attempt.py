from datetime import datetime
from typing import List, Optional
from .student import Student
from .exam import Exam
from ..enums.attempt_status import AttemptStatus
from .answer import Answer
from .violation import Violation
from .result import Result
from ..enums.violation_type import ViolationType


class ExamAttempt:
    def __init__(self, attempt_id: str, student: Student, exam: Exam):
        self.id = attempt_id
        self.student = student
        self.exam = exam
        self.status = AttemptStatus.IN_PROGRESS
        self.started_at = datetime.utcnow()
        self.finished_at: Optional[datetime] = None
        self.answers: List[Answer] = []
        self.violations: List[Violation] = []
        self.result: Optional[Result] = None

    def submit_answer(self, question_id: str, selected_option: str):
        if self.status != AttemptStatus.IN_PROGRESS:
            raise Exception("Cannot submit answer. Exam is not in progress.")

        answer = Answer(question_id, selected_option)
        self.answers.append(answer)

    def record_violation(self, violation_type: ViolationType):
        violation = Violation(violation_type)
        self.violations.append(violation)

    def finish(self, pass_score: int):
        if self.status != AttemptStatus.IN_PROGRESS:
            raise Exception("Exam already finished.")

        self.status = AttemptStatus.SUBMITTED
        self.finished_at = datetime.utcnow()

        self.result = Result()
        self.result.calculate(self.answers, pass_score)

    def auto_submit(self, pass_score: int):
        self.status = AttemptStatus.AUTO_SUBMITTED
        self.finished_at = datetime.utcnow()

        self.record_violation(ViolationType.TIME_EXCEEDED)

        self.result = Result()
        self.result.calculate(self.answers, pass_score)
