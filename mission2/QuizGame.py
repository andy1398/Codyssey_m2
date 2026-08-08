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
        
    def save_current_state(self) -> None:
        """현재 데이터 저장"""
        self.storage.save_data(self.quizzes, self.best_score)
        
    def play_quiz(self) -> None:
        if not self.quizzes:
            print("\n등록된 퀴즈가 없습니다.")
            return
# 몇 문제 풀래 
        max_count = len(self.quizzes)
        print(f"\n몇 문제를 풀고 싶으신가요? (현재 총 {max_count}문제)")
        target_count = InputValidator.read_int_in_range("문제 수 선택: ", 1, max_count)

        score = 0
        print(f"\n📝 퀴즈를 시작합니다! (총 {target_count}문제)")

        for i in range(target_count):
            quiz = self.quizzes[i]
            quiz.display(i + 1)

            user_ans = InputValidator.read_int_in_range(
                "\n정답 입력 (번호): ", 1, len(quiz.choices)
            )
            if quiz.is_correct(user_ans):
                print("정답입니다!")
                score += 1
            else:
                print(f"틀렸습니다. (정답: {quiz.answer}번)")
        
        print(f"\n최종 결과: {target_count}문제 중 {score}문제 맞춤!")
        if score > self.best_score:
            print("축하합니다! 최고 점수를 갱신했습니다.")
            self.best_score = score
            self.save_current_state()
