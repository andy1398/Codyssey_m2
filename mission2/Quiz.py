from typing import List, Dict, Any

class Quiz:
    def __init__(self, question: str, choices: List[str], answer: int):
        self.question = question
        self.choices = choices
        self.answer = answer
    def is_correct(self,user_choice: int) -> bool:
        return self.answer == user_choice
