from domain.entities.student import Student
from domain.entities.exam import Exam
from domain.entities.question import Question
from domain.entities.exam_attempt import ExamAttempt
from domain.enums.violation_type import ViolationType


def main():
    student = Student("S1", "Ali")

    questions = [
        Question("Q1", "2 + 2 = ?", 5),
        Question("Q2", "5 * 3 = ?", 5)
    ]

    exam = Exam("E1", "Math Exam", duration_minutes=30, questions=questions)

    attempt = ExamAttempt("A1", student, exam)

    attempt.submit_answer("Q1", "4")
    attempt.submit_answer("Q2", "15")

    attempt.record_violation(ViolationType.TAB_SWITCH)

    attempt.finish(pass_score=5)

    print("Student:", student.name)
    print("Total score:", attempt.result.total_score)
    print("Passed:", attempt.result.passed)


if __name__ == "__main__":
    main()
