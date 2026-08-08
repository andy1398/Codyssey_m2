import random
from datetime import datetime
from typing import List, Dict, Any
from Quiz import Quiz
from storage import StorageHandler
from utils import InputValidator

class QuizGame:
    def __init__(self, file_path: str = "state.json"):
        self.storage = StorageHandler(file_path)
        self.quizzes: List[Quiz] = []
        self.best_score: int = 0
        self.history: List[Dict[str, Any]] = []
        self.user_name: str = "게스트"
        self.reload_data()
        
    def reload_data(self) -> None:
        """저장소로부터 데이터 갱신"""
        self.quizzes, self.best_score, self.history,self.user_name = self.storage.load_data()
        
    def save_current_state(self) -> None:
        """현재 데이터 저장"""
        self.storage.save_data(self.quizzes, self.best_score, self.history,self.user_name)
        
    def play_quiz(self) -> None:
        if not self.quizzes:
            print("\n등록된 퀴즈가 없습니다.")
            return
# 몇 문제 풀래 
        max_count = len(self.quizzes)
        print(f"\n몇 문제를 풀고 싶으신가요? (현재 총 {max_count}문제)")
        target_count = InputValidator.read_int_in_range("문제 수 선택: ", 1, max_count)

        # random.sample을 이용한 무작위 출제 (원본 리스트 순서 보존)
        selected_quizzes = random.sample(self.quizzes, target_count)

        score = 0
        correct_count = 0
        print(f"\n퀴즈를 시작합니다! (플레이어: {self.user_name} | 총 {target_count}문제)")

        for i, quiz in enumerate(selected_quizzes, 1):
            quiz.display(i)

            # 힌트 사용 여부 확인 및 점수 차감 로직
            print("\n힌트를 보시겠습니까?")
            print(" 1. 힌트 보기 (정답 시 점수 50% 차감)")
            print(" 2. 바로 정답 입력하기")
            hint_choice = InputValidator.read_int_in_range("선택: ", 1, 2)

            used_hint = False
            if hint_choice == 1:
                used_hint = True
                print(f"[힌트]: {quiz.hint}")

            user_ans = InputValidator.read_int_in_range(
                "\n정답 입력 (번호): ", 1, len(quiz.choices)
            )
            if quiz.is_correct(user_ans):
                earned = 5 if used_hint else 10
                score += earned
                correct_count += 1
                print(f"정답입니다! (+{earned}점)")
            else:
                print(f"틀렸습니다. (정답: {quiz.answer}번)")
        
        print(f"\n최종 결과: {target_count}문제 중 {correct_count}문제 맞춤 | 총점: {score}점")

        # 게임 기록(일시, 유저 이름, 푼 문제 수, 정답 수, 점수) 히스토리에 추가
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        record = {
            "datetime": now_str,
            "user_name": self.user_name,
            "total_questions": target_count,
            "correct_count": correct_count,
            "score": score,
        }
        self.history.append(record)

        if score > self.best_score:
            print(f" 축하합니다! {self.user_name}님이 최고 점수를 갱신했습니다.")
            self.best_score = score
            
        self.save_current_state()
            
    def add_quiz(self) -> None:
        print("\n새로운 퀴즈 추가")
        question = InputValidator.read_non_empty_string("문제 내용 입력: ")

        raw_choices = InputValidator.read_non_empty_string(
            "선택지 입력 (쉼표 ','로 구분 ex: 사과,바나나,포도,수박): "
        )
        choices = [c.strip() for c in raw_choices.split(",") if c.strip()]
        """raw_choices.split(","):
쉼표(,)를 기준으로 문자열을 잘라 리스트로 만듭니다.
for c in ...:
잘라낸 조각들(c)을 하나씩 순서대로 꺼냅니다
[ 최상적으로 넣을 값 for 변수 in 반복할대상 if 조건식 ]
        """
        
        while len(choices) < 4:
            print("선택지는 최소 4개 이상이어야 합니다.")
            raw_choices = InputValidator.read_non_empty_string("선택지 재입력 (쉼표 구분): ")
            choices = [c.strip() for c in raw_choices.split(",") if c.strip()]

        print("\n등록된 선택지:")
        for idx, c in enumerate(choices, 1):
            print(f"  {idx}. {c}")

        answer = InputValidator.read_int_in_range(
            f"정답 번호 선택 (1~{len(choices)}): ", 1, len(choices)
        )
        
        hint = InputValidator.read_non_empty_string("힌트 내용 입력: ")

        new_quiz = Quiz(question, choices, answer, hint)
        self.quizzes.append(new_quiz)
        self.save_current_state()
        print("성공적으로 저장되었습니다!")

    def delete_quiz(self) -> None:
        """퀴즈 삭제 기능"""
        if not self.quizzes:
            print("\n등록된 퀴즈가 없습니다.")
            return

        self.view_list()
        delete_idx = InputValidator.read_int_in_range(
            f"\n삭제할 퀴즈 번호를 선택하세요 (1~{len(self.quizzes)}): ", 1, len(self.quizzes)
        )

        removed_quiz = self.quizzes.pop(delete_idx - 1)
        self.save_current_state()
        print(f"\n[{removed_quiz.question}] 퀴즈가 성공적으로 삭제되었습니다.")
        
    def view_list(self) -> None:
        if not self.quizzes:
            print("\n등록된 퀴즈가 없습니다.")
            return

        print(f"\n등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("-" * 50)
        for idx, quiz in enumerate(self.quizzes, 1):
            print(f"{idx}. {quiz.question} (힌트: {quiz.hint})")
        print("-" * 50)
        
    def view_score(self) -> None:
        print("\n" + "=" * 50)
        print(f"현재 최고 점수: {self.best_score}점")
        print("=" * 50)

        if not self.history:
            print(" 게임 기록이 존재하지 않습니다.")
            return

        print("\n 최근 게임 기록 (최근 5건)")
        print("-" * 50)
        for record in reversed(self.history[-5:]):
            player = record.get("user_name", "게스트")
            print(
                f"[{record['datetime']}] "
                f"플레이어: {player} | "
                f"풀이 문제 수: {record['total_questions']}개 | "
                f"정답 수: {record['correct_count']}개 | "
                f"점수: {record['score']}점"
            )
        print("-" * 50)
    
    def set_user_name(self) -> None:
        """유저 이름 설정 기능"""
        print(f"\n현재 유저 이름: {self.user_name}")
        new_name = InputValidator.read_non_empty_string("새로운 유저 이름을 입력하세요: ")
        self.user_name = new_name
        self.save_current_state()
        print(f"유저 이름이 '{self.user_name}'(으)로 변경되었습니다!")
        
    def run(self) -> None:
        """메인 실행 메뉴 루프"""
        while True:
            print("\n========================================")
            print("            퀴즈 게임            ")
            print("========================================")
            print(" 1. 퀴즈 풀기 (랜덤 출제 & 힌트)")
            print(" 2. 퀴즈 추가")
            print(" 3. 퀴즈 삭제")
            print(" 4. 퀴즈 목록")
            print(" 5. 최고 점수 및 기록 확인")
            print(" 6. 유저 이름 변경")
            print(" 7. 종료")
            print("========================================")

            choice = InputValidator.read_int_in_range("메뉴 선택: ", 1, 7)

            if choice == 1:
                self.play_quiz()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.delete_quiz()
            elif choice == 4:
                self.view_list()
            elif choice == 5:
                self.view_score()
            elif choice == 6:
                self.set_user_name()
            elif choice == 7:
                print("\n게임을 종료합니다. 이용해 주셔서 감사합니다.")
                self.save_current_state()
                break