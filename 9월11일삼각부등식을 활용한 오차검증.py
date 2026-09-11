#sensor's error detected tryangle inequality

#situation : when people run, sensor give information to software



theta_cur = 입력값 #it is current theta that the moment is run and theta beteween 허벅지 hips and when "stop" state is 기준, 기준 is "0" theta

theta_pre = 입력값 #it is pre theta that perform 전에 0.01second

dt = 0.01 #it is 기준시, delta sencond

theta_velocity = (theta_cur - theta_pre)/dt

peak = 입력값 #this is problem that yet not conclued



if peak*0.55>theta_cur>peak*0.45

f = 3

if peak*0.65>theta_cur>=peak*0.55

f = 7

if peak*0.75>theta_cur>=peak*0.65

f=3



motor_torque = f*l

l=입력값

f=o



if abs(theta_cur-theta_pre) < abs(theta_cur)-abs(theta_pre) and theta_velocity>0#this situation is that only forward walk

printf (error) 

