# 코드 상단에 아래를 추가해서 테스트해보세요
import sys, os
sys.path.append(os.path.abspath("../deep-learning-from-scratch"))

try:
    from common.functions import sigmoid
    print("성공: common 모듈을 찾았습니다!")
except ImportError as e:
    print(f"실패: 모듈을 찾을 수 없습니다. 경로를 확인하세요. 에러 내용: {e}")