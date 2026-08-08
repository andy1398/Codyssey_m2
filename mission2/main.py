import sys
from QuizGame import QuizGame


def main():
    try:
        game = QuizGame()
        game.run()
    except (KeyboardInterrupt, EOFError):
        print("\n\n사용자에 의해 프로그램이 중단되었습니다. 진행 상태를 안전하게 저장합니다...")
        try:
            if "game" in locals():
                game.save_current_state()
            print("안전하게 저장 후 종료되었습니다.")
        except Exception as e:
            print(f"저장 중 오류 발생: {e}")
        sys.exit(0)

    """파이썬에는 현재 스코프(영역)에 선언되어 있는 모든 지역 변수(Local Variables)를 { '변수명': 변수값 } 형태의 딕셔너리로 반환해 주는 locals()라는 내장 함수
    객체 생성전에 ^c 를 하면 game이라는 변수 자체가 메모리에 만들어지지 못한 상태로 except 블록으로 넘어가게 됩니다. 
    이때 game.save_current_state()를 실행하려고 하면 파이썬은 NameError: name 'game' is not defined라는 2차 예외(에러)를 터뜨리며
    프로그램이 지저분하게 강제 종료되기 때문에
    """

# main 파일을 실핼할때만 게임이 실행됨
if __name__ == "__main__":
    main()
