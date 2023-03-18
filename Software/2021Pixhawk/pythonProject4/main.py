# Import mavutil
from pymavlink import mavutil
import time
mode = 'MANUAL'


master = mavutil.mavlink_connection('COM12', baud=115200)







def asagi():
    i=0
    while i<3 :
        master.wait_heartbeat()

        mode_id = master.mode_mapping()[mode]
        master.set_mode(mode_id)

        master.mav.command_long_send(
            master.target_system,
            master.target_component,
            mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
            0,
            1,0,0,0,0,0,0)
        master.mav.manual_control_send(
            master.target_system,
            0,
            0,
            -500,
            0,
            0)
        i = i+1
        if i==3:
            master.wait_heartbeat()
            master.mav.command_long_send(
                master.target_system,
                master.target_component,
                mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
                0,
                0, 0, 0, 0, 0, 0, 0)






def yukari():
    i=0
    while i<3 :

        master.wait_heartbeat()

        mode_id = master.mode_mapping()[mode]
        master.set_mode(mode_id)

        master.mav.command_long_send(
            master.target_system,
            master.target_component,
            mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
            0,
            1,0,0,0,0,0,0)
        master.mav.manual_control_send(
            master.target_system,
            0,
            0,
            3000,
            0,
            0)
        i = i+1
        if i==3:
            master.wait_heartbeat()
            master.mav.command_long_send(
                master.target_system,
                master.target_component,
                mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
                0,
                0, 0, 0, 0, 0, 0, 0)



def geri():
    i=0
    while i<3 :

        master.wait_heartbeat()

        mode_id = master.mode_mapping()[mode]
        master.set_mode(mode_id)

        master.mav.command_long_send(
            master.target_system,
            master.target_component,
            mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
            0,
            1,0,0,0,0,0,0)
        master.mav.manual_control_send(
            master.target_system,
            0,
            2000,
            500,
            0,
            0)
        i = i+1
        if i==3:
            master.wait_heartbeat()
            master.mav.command_long_send(
                master.target_system,
                master.target_component,
                mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
                0,
                0, 0, 0, 0, 0, 0, 0)





def ileri():
    i=0
    while i<3 :

        master.wait_heartbeat()

        mode_id = master.mode_mapping()[mode]
        master.set_mode(mode_id)

        master.mav.command_long_send(
            master.target_system,
            master.target_component,
            mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
            0,
            1,0,0,0,0,0,0)
        master.mav.manual_control_send(
            master.target_system,
            0,
            -2000,
            500,
            0,
            0)
        i = i+1
        if i==3:
            master.wait_heartbeat()
            master.mav.command_long_send(
                master.target_system,
                master.target_component,
                mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
                0,
                0, 0, 0, 0, 0, 0, 0)



def sag():
    i=0
    while i<3 :

        master.wait_heartbeat()

        mode_id = master.mode_mapping()[mode]
        master.set_mode(mode_id)

        master.mav.command_long_send(
            master.target_system,
            master.target_component,
            mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
            0,
            1,0,0,0,0,0,0)
        master.mav.manual_control_send(
            master.target_system,
            2000,
            0,
            500,
            0,
            0)
        i = i+1
        if i==3:
            master.wait_heartbeat()
            master.mav.command_long_send(
                master.target_system,
                master.target_component,
                mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
                0,
                0, 0, 0, 0, 0, 0, 0)


def sol():
    i=0
    while i<3 :

        master.wait_heartbeat()

        mode_id = master.mode_mapping()[mode]
        master.set_mode(mode_id)

        master.mav.command_long_send(
            master.target_system,
            master.target_component,
            mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
            0,
            1,0,0,0,0,0,0)
        master.mav.manual_control_send(
            master.target_system,
            -2000,
            0,
            500,
            0,
            0)
        i = i+1
        if i==3:
            master.wait_heartbeat()
            master.mav.command_long_send(
                master.target_system,
                master.target_component,
                mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
                0,
                0, 0, 0, 0, 0, 0, 0)


sol()
sol()
sol()
sol()
