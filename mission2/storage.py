import json
import os
from typing import List, Dict, Any, Tuple
from Quiz import Quiz

DEFAULT_QUIZZES = [
    {"question": "1+1 = ?", "choices": ["1", "2", "3", "4"], "answer": 2},
    {"question": "France의 수도는?", "choices": ["London", "Berlin", "Paris", "Madrid"], "answer": 3},
    {"question": "Python의 개발자는?", "choices": ["Guido van Rossum", "James Gosling", "Brendan Eich", "Dennis Ritchie"], "answer": 1},
    {"question": "JavaScript의 창시자는?", "choices": ["Brendan Eich", "Guido van Rossum", "James Gosling", "Dennis Ritchie"], "answer": 1},
    {"question": "C언어의 창시자는?", "choices": ["Dennis Ritchie", "Brendan Eich", "Guido van Rossum", "James Gosling"], "answer": 1},
]

# state.json 파일 읽기/쓰기 관리 클래스
class StorageHandler:
    def __init__(self, file_path: str = "state.json"):
        self.file_path = file_path
        
    def load_data(self) -> Tuple[List[Quiz], int]:
        if not os.path.exists(self.file_path):
            return self._get_default_data()
        """os가 컴터에 해당 경로에 파일이 있는지 물어보는 거임
        """
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                quizzes = [Quiz.from_dict(q) for q in data.get("quizzes", [])]
                best_score = data.get("best_score", 0)

                """
                data.get("quizzes", []): data 딕셔너리에서 "quizzes"라는 키의 값을 가져옵니다. 만약 그 키가 없으면 안전하게 빈 리스트 []를 기본값으로 가져옵니다.
                for q in ...: 가져온 퀴즈 딕셔너리 목록에서 문제 1개씩(q) 꺼내며 반복합니다.
                Quiz.from_dict(q): 아까 만든 클래스 메서드죠! 딕셔너리 q를 넣어서 Quiz 객체로 완성합니다.
                """

                if not quizzes:
                    return self._get_default_data()

                return quizzes, best_score

        except (json.JSONDecodeError, KeyError, TypeError, IOError) as e:
            print(f"\n[경고] 데이터 파일({self.file_path})이 손상되었습니다. 기본 데이터로 복구합니다. ({e})")
            return self._get_default_data()
        
    def _get_default_data(self) -> Tuple[List[Quiz], int]:
        quizzes = [Quiz.from_dict(q) for q in DEFAULT_QUIZZES]
        return quizzes, 0
    
    def save_data(self, quizzes: List[Quiz], best_score: int) -> bool:
        data = {
            "quizzes": [q.to_dict() for q in quizzes],
            "best_score": best_score,
        }
        try:
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            return True
        except IOError as e:
            print(f"\n[오류] 데이터 저장 실패: {e}")
            return False
        
        """
        q라는 변수 이름을 사용했기 때문에 q.to_dict()
        파일을 저장(쓰기)하는 과정에서 발생할 수 있는 거의 모든 문제는 '입출력 오류(Input/Output Error)'에 해당하기 때문에 IOError 사용
        (권한 , 용량, 경로)
        json 모듈은 기본 설정이 ensure_ascii=True 로 되어 있기때문에 SON 파일에 한글이 전부 이상한 유니코드 암호 코드(16진수)로 저장됨
        """