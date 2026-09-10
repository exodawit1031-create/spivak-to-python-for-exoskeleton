# spivak-to-python-exo
Mathematical Rigor & Real-Time Lower-Limb Exoskeleton Control Log

---

## Daily Study Log

### 2026-09-10
* **Topic:** 계단형 힘 프로파일(2N-7N-2N) 구현 및 파이썬 연산 타이밍 디버깅
* **Progress & Logic:**
  - 관절 가속 구간($45\% \sim 75\%$)의 충격을 완화하기 위한 3단계 계단형 힘 인가 로직 설계.
  - 전진 운동(`theta_velocity > 0`) 조건 검증으로 역방향 토크 인가 방지.
* **Engineering Bug Fix:**
  - `f = f + 2` 형태의 누적 연산 시 발생하는 값 발산 위험 차단 (`f = 0` 기본값 기반 정적 할당으로 수정).
  - 수학 방정식과 프로그래밍 대입문의 차이 인식: `motor_torque = f * l`이 조건문 위에 위치할 때 갱신된 $f$가 누락되는 문제를 확인하고 조건문 최하단으로 재배치.
* **Next Task:**
  - 고정된 `peak` 상수를 어떻게 해야 할지 고민임 ㅠㅠ.
