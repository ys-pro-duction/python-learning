class Question:
    text: str = None
    answer: str = None

    def __init__(self, text: str, answer: str):
        self.text = text
        self.answer = answer

