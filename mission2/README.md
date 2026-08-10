# 1. Git 저장소 설정
git init
touch README.md 
git add .
git commit -m "Feat: 프로젝트 초기 설정 및 기본 파일 생성"
git branch -M main
git remote add origin https://github.com/andy1398/Codyssey_m2.git
git push -u origin main

**새 저장소 깃 연결**

<img width="583" height="558" alt="Image" src="https://github.com/user-attachments/assets/fade1465-4814-48f3-beb7-212a651f0ef4" />

**커밋 10번**

<img width="744" height="772" alt="Image" src="https://github.com/user-attachments/assets/f9361280-1ce3-4f3f-8ed8-ff1df4ea13bd" />

**병합**

<img width="369" height="232" alt="Image" src="https://github.com/user-attachments/assets/c34e3d24-0ce9-4964-a094-df246f666051" />

# 2. 프로젝트 개요
프로젝트 이름: Python Quiz Game (나만의 퀴즈 게임)
개발 기간: 2026년 8월 (개인 프로젝트)
프로젝트 설명:
Python 기초 문법과 객체 지향 프로그래밍(OOP) 개념을 활용하여 터미널(콘솔) 환경에서 동작하는 콘솔 퀴즈 게임입니다.
사용자가 직접 문제를 풀고, 새로운 퀴즈를 등록할 수 있으며, 등록된 퀴즈 목록과 최고 점수를 확인할 수 있습니다.
JSON 파일 입출력(state.json)을 통해 프로그램을 종료하더라도 데이터가 영구적으로 유지되도록 구현되었습니다.
Git 및 GitHub의 브랜치 전략과 커밋 규칙을 준수하여 버전 관리 및 협업 프로세스를 학습하고 적용했습니다.

# 3. 퀴즈 주제와 선정 이유
선정 주제: 기본 상식
선정 이유: 쉽게 풀수 있기 때문에 선정했다. 

# 4. 실행 방법
python3 main.py

# 5. 기능 목록
1. 퀴즈 풀기 (랜덤 출제 & 힌트)
   - `random.sample()`을 활용하여 원본 데이터 훼손 없이 사용자가 선택한 문제 수만큼 무작위 출제
   - 문제 출제 전 힌트 사용 여부를 선택 가능하며, 힌트 사용 시 점수 감점(50% 차감) 적용

2. 퀴즈 추가
   - 사용자로부터 문제, 선택지(쉼표 `,` 구분으로 최소 4개 이상), 정답 번호, 힌트를 입력받아 등록
   - 입력값 검증을 통해 빈 값이나 유효하지 않은 숫자 입력 시 재입력 유도
   
3. 퀴즈 삭제
   - 등록된 퀴즈 목록을 확인하고 원하는 번호의 퀴즈를 리스트에서 제거(`pop`) 후 `state.json`에 즉시 반영

4. 퀴즈 목록 조회
   - 현재 등록된 모든 퀴즈의 질문과 힌트 정보를 한눈에 확인

5. 최고 점수 및 기록(History) 확인
   - 현재까지의 최고 점수 출력
   - `datetime` 모듈을 이용해 저장된 최근 게임 플레이 기록(일시, 푼 문제 수, 정답 수, 획득 점수) 확인

6. 안전한 예외 처리 & 데이터 영속성
   - `Ctrl+C`(KeyboardInterrupt) 또는 `EOFError` 발생 시, 프로그램이 중단되기 전 상태 데이터를 자동 저장하고 안전하게 종료
   - `state.json` 파일이 손상되었거나 없을 경우 기본 데이터로 자동 복구

# 6. 파일 구조
mission2/
├── Quiz.py          # 개별 퀴즈 엔티티 (Quiz 클래스)
├── storage.py       # JSON 데이터 입출력 및 손상 복구 관리 (StorageHandler 클래스)
├── utils.py         # 공통 콘솔 입력 검증 및 예외 처리 (InputValidator 클래스)
├── QuizGame.py      # 게임 메인 비즈니스 로직 및 메뉴 흐름 제어 (QuizGame 클래스)
├── main.py          # 최상위 프로그램 실행 엔트리 포인트 및 예외 감지
└── state.json       # 퀴즈 및 게임 상태 저장 데이터 파일 (자동 생성)

# 7. 데이터 파일 설명(state.json 경로/역할/스키마)
경로: 프로젝트 루트 (mission2/state.json)
역할: 프로그램을 종료하거나 재시작해도 추가/삭제된 퀴즈, 최고 점수, 플레이 히스토리가 유지되도록 해주는 데이터 영속성(Persistence) 파일
인코딩: UTF-8 (ensure_ascii=False 설정을 적용하여 한글 데이터의 유니코드 변환 깨짐 방지)

{
  "quizzes": [
    {
      "question": "1+1 = ?",
      "choices": ["1", "2", "3", "4"],
      "answer": 2,
      "hint": "가장 기본적인 짝수 수식입니다."
    }
  ],
  "best_score": 10,
  "history": [
    {
      "datetime": "2026-03-30 14:20:00",
      "total_questions": 5,
      "correct_count": 4,
      "score": 35
    }
  ]
}

# 8. 주요 코드 구현 메모
1. 
choices = [c.strip() for c in raw_choices.split(",") if c.strip()]

split(",")로 잘라낸 조각(c)에서 공백을 제거(strip())하고, 빈 문자열이 아닌 것만 필터링하여 한 줄로 효율적으로 리스트를 생성.
2. 
for idx, choice in enumerate(self.choices, 1):

리스트의 요소를 순회할 때 인덱스 번호를 1부터 지정하여 (번호, 값) 형태의 튜플로 반환받아 깔끔하게 화면 출력.
3. 
@classmethod
def from_dict(cls, data: Dict[str, Any]) -> "Quiz":

클래스 인스턴스를 직접 생성하지 않고도 JSON 딕셔너리 데이터를 받아 Quiz 객체로 복원하는 팩토리 메서드 구현.
4. 
if "game" in locals():
    game.save_current_state()

Ctrl+C나 EOF로 프로그램이 기습 중단될 때, game 변수가 메모리에 정상 할당된 상태인지 locals() 목록을 검사하여 NameError 방지.

5. 
파일 저장 과정에서 권한, 용량, 경로 문제 등으로 발생할 수 있는 거의 모든 문제는 입출력 오류(IOError)에 해당하므로 try-except로 예외를 쳐내어 안정성 확보.

6. 클래스는 상태와 동작을 저장하는것.
그래서 문제 생길때 해당 부분을 수정, 확장하면 됨.

예외처리는 되도록이면 throw 해서 국소적으로 처리하는게 좋다. 메인으로 하면 플젝의 커질때 처리 못하는게 생길수 있다. 

상태를 관리하는 클래스가 별도로 있으면 실력있는 개발자 ㅇㅇ
