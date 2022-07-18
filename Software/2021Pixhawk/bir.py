from pymavlink import mavutil
import time

# https://www.ardusub.com/developers/pymavlink.html

#mavutil.set_dialect("ardupilotmega")

master = mavutil.mavlink_connection( # aracin baglantisi
            'COM12',
            baud=115200)
master.wait_heartbeat()

def set_rc_channel_pwm(id, pwm=1500):
    """ Set RC channel pwm value
    Args:
        id (TYPE): Channel ID
        pwm (int, optional): Channel pwm value 1100-1900
    """
    if id < 1:
        print("Channel does not exist.")
        return

    if id < 9:
        rc_channel_values = [65535 for _ in range(8)]
        rc_channel_values[id - 1] = pwm
        master.mav.rc_channels_override_send(
            master.target_system,                # target_system
            master.target_component,             # target_component
            *rc_channel_values)                  # RC channel list, in microseconds.
print("run")
# Set some roll
set_rc_channel_pwm(3, 1300)
time.sleep(2)
# Set some yaw
set_rc_channel_pwm(3, 1000)