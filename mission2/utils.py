class InputValidator:
    """사용자 콘솔 입력 검증 및 예외 처리 헬퍼 클래스"""

# 빈 입력 채크
    @staticmethod
    def read_non_empty_string(prompt: str) -> str:
        while True:
            val = input(prompt).strip()
            if val:
                return val
            print("빈 값은 입력할 수 없습니다. 다시 입력해 주세요.")
        """prompt(프롬프트)는 사용자에게 "입력창에 무엇을 적어야 할지 안내해 주는 문구(질문 메시지)"입니다.
        prompt라는 매개변수는 결국 문자열이나 문자열이 담긴 변수를 받기 위해 비워둔 자리
        """

# 빈 입력 + 숫자가 아니면
    @staticmethod
    def read_int_in_range(prompt: str, min_val: int, max_val: int) -> int:
        """지정한 범위(min~max) 내의 정수만 받도록 검증"""
        while True:
            raw = input(prompt).strip()
            if not raw:
                print("입력값이 없습니다. 숫자를 입력해 주세요.")
                continue
            try:
                val = int(raw)
                if min_val <= val <= max_val:
                    return val
                print(f"⚠️ {min_val}~{max_val} 사이의 숫자를 입력하세요.")
            except ValueError:
                print("숫자가 아닙니다. 올바른 숫자를 입력하세요.")