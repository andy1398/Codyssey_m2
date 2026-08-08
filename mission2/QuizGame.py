from typing import List
from Quiz import Quiz
from storage import StorageHandler
from mission2.utils import InputValidator

class QuizGame:
    def __init__(self, file_path: str = "state.json"):
        self.storage = StorageHandler(file_path)
        self.quizzes: List[Quiz] = []
        self.best_score: int = 0
        self.reload_data()
        
    def reload_data(self) -> None:
        """저장소로부터 데이터 갱신"""
        self.quizzes, self.best_score = self.storage.load_data()