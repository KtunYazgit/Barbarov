import time

from pymavlink import mavutil
import time

time.sleep(10)
master = mavutil.mavlink_connection( # aracin baglantisi
            '/dev/ttyACM0',
            baud=115200)

master.wait_heartbeat()
mode = 'MANUAL'

mode_id = master.mode_mapping()[mode]

master.set_mode(mode_id)

master.arducopter_arm()

def set_rc_channel_pwm(channel_id, pwm=1500):

    if channel_id < 1 or channel_id > 9:
        print("Channel does not exist.")
        return

    rc_channel_values = [65535 for _ in range(9)]
    rc_channel_values[channel_id - 1] = pwm
    master.mav.rc_channels_override_send(
        master.target_system,
        master.target_component,
        *rc_channel_values)



def ileri():
    set_rc_channel_pwm(5, 1650) # ileri git
def geri():
    set_rc_channel_pwm(5, 1400) # geri git
def sol():
    set_rc_channel_pwm(6, 1400)
def sag():
    set_rc_channel_pwm(6, 1600)
def alcal():
    set_rc_channel_pwm(3, 1450)
def yuksel():
    set_rc_channel_pwm(3, 1510)
def don():
    set_rc_channel_pwm(4, 1400)



"""
def ileri():
    set_rc_channel_pwm(5, 1400) # ileri git
def geri():
    set_rc_channel_pwm(5, 1400) # geri git
def sol():
    set_rc_channel_pwm(6, 1400)
def sag():
    set_rc_channel_pwm(6, 1400)
def alcal():
    set_rc_channel_pwm(3, 1400)
def yuksel():
    set_rc_channel_pwm(1, 1400)
def don():
    set_rc_channel_pwm(4, 1400)
"""
git = 0
while(True):
    git += 1
    if(10000 > git):
        alcal()
        print(git)
    elif(git > 10000):
        master.arducopter_disarm()