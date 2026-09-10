# ==========================================================
# File: gait_torque_step.py
# Date: 2026-09-10
# Description: 1-DOF 보행/달리기 계단형 토크 제어 프로파일 프로토타입
# ==========================================================

# 1. 센서 입력 및 물리 파라미터
theta_cur = 20.0        # 현재 관절 각도 [deg]
theta_pre = 19.5        # 0.01초 전 관절 각도 [deg]
dt = 0.01               # 샘플링 주기 [s] (P7/P10: dt > 0)
l = 0.5                 # 하지 링크 길이 [m]
peak = 35.0             # 현재 추정된 최대 관절 가동 범위 (추후 동적 갱신 예정)

# 2. 수치 차분을 통한 각속도 산출 및 기본 힘 초기화
theta_velocity = (theta_cur - theta_pre) / dt
f = 0                   # 구간 외 기본 보조 힘은 0N으로 안전 유지

# 3. 보행/달리기 스윙 가속 구간별 계단형 힘 프로파일 (2N -> 7N -> 2N)
# 전진 운동(theta_velocity > 0)일 때만 활성화
if peak * 0.55 > theta_cur > peak * 0.45 and theta_velocity > 0:
    f = 2
elif peak * 0.65 > theta_cur >= peak * 0.55 and theta_velocity > 0:
    f = 7
elif peak * 0.75 > theta_cur >= peak * 0.65 and theta_velocity > 0:
    f = 2

# 4. 최종 확정된 힘(f)을 바탕으로 모터 토크 연산
motor_torque = f * l    # Torque = Force * Length [Nm]

print(f"Angular Velocity: {theta_velocity:.2f} deg/s")
print(f"Assistance Force: {f} N")
print(f"Motor Torque: {motor_torque:.2f} Nm")