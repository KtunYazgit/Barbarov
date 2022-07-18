# Import mavutil
from pymavlink import mavutil
import time

time.sleep(10)

# connection olusturma
master = mavutil.mavlink_connection(
            '/dev/ttyACM0',
            baud=115200)# Raspberry pi ile pixhawk'ın iletişim kurabilmesi için

master.wait_heartbeat()
mode = 'MANUAL'

mode_id = master.mode_mapping()[mode]

master.set_mode(mode_id)

master.arducopter_arm()
git =0
while(True):
    git += 1
    if(5000 > git):
        master.mav.manual_control_send(
            master.target_system,
            master.component,
            mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
            0,
            0,
            -500,
            0,
            0)
        print(git)
    elif(git > 5000):
        master.arducopter_disarm()

