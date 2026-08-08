from typing import List, Dict, Any

class Quiz:
    def __init__(self, question: str, choices: List[str], answer: int, hint: str = "힌트가 없습니다."):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint
        
    def is_correct(self, user_choice: int) -> bool:
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

    def to_dict(self) -> Dict[str, Any]:
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
            "hint": self.hint,
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Quiz":
        """JSON 딕셔너리로부터 Quiz 객체 생성"""
        return cls(
            question=data["question"],
            choices=data["choices"],
            answer=data["answer"],
            hint=data.get("hint", "힌트가 제공되지 않는 문제입니다."),
        )
    """
객체(인스턴스)를 생성하지 않고도 클래스 자체에서 직접 호출할 수 있는 메서드로 만들어주는 데코레이터
클래스 메서드(@classmethod) 내부에서 cls(...)를 호출하여 리턴하면 해당 클래스의 인스턴스(객체)를 생성하여 반환
"""