class Answer:
    def __init__(self, question_id: str, selected_option: str, score: int = 0):
        self.question_id = question_id
        self.selected_option = selected_option
        self.score = score

    def __eq__(self, other):
        if not isinstance(other, Answer):
            return False
        return (
            self.question_id == other.question_id and
            self.selected_option == other.selected_option and
            self.score == other.score
        )
