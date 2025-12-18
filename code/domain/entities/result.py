from .answer import Answer
from typing import List



class Result:
    def __init__(self):
        self.total_score: int = 0
        self.passed: bool = False

    def calculate(self, answers: List[Answer], pass_score: int):
        self.total_score = sum(answer.score for answer in answers)
        self.passed = self.total_score >= pass_score
