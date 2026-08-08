from typing import List, Dict, Any

class Quiz:
    def __init__(self, question: str, choices: List[str], answer: int):
        self.question = question
        self.choices = choices
        self.answer = answer
    def is_correct(self,user_choice: int) -> bool:
        return self.answer == user_choice
    
    """
: int 를 이용하여 코드를 읽을때 이건 정수형으로 넣어야 하는점을 알려줌
-> bool 을 적어서 해당 함수가 t/f 를 반환할것을 알려줌
모두 가독성을 위해서임
"""

    def display(self, index: int) -> None:
        print(f"\n[문제 {index}] {self.question}")
        for idx, choice in enumerate(self.choices, 1):
            print(f"  {idx}번. {choice}")

    """
enumerate(리스트, 시작할_숫자)
["사자", "뱀", "고양이"]라면, 자동으로
1번째 바퀴: (1, "사자")
2번째 바퀴: (2, "뱀")
3번째 바퀴: (3, "고양이") 이렇게 됨. 따라서 for 뒤에변수 이름은 맘대로 적어도됨.
"""
