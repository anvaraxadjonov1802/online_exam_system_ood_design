# application/exam_service.py
from ..domain.entities.exam_attempt import ExamAttempt

class ExamService:
    def start_exam(self, student, exam):
        return ExamAttempt("id", student, exam)
