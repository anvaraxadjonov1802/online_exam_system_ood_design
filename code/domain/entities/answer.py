class Answer:
    def __init__(self, question_id: str, selected_option: str):
        self.question_id = question_id
        self.selected_option = selected_option
        self.score: int = 0
