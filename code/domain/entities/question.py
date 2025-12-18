class Question:
    def __init__(self, question_id: str, text: str, max_score: int):
        self.id = question_id
        self.text = text
        self.max_score = max_score
