#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import numpy as np
#import argparse
#import cv2
#import cv2 as CV #eğer python2 kullanıyorsanız eklemek zorundasınız aksi halde hata alırsınız
import time
import threading
from pymavlink import mavutil



master = mavutil.mavlink_connection( # aracin baglantisi
            'COM12',
            baud=115200)

#master = "mavutil.mavlink_connection('udpin:192.168.2.2:14550')" #eğer bilgisayardan konttrol edilecekse
def set_rc_channel_pwm(id, pwm=1500):

    if id < 1:
        print("Channel does not exist.")
        return


    if id < 9: # ardusubla iletisim
        rc_channel_values = [65535 for _ in range(8)]
        rc_channel_values[id - 1] = pwm
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

ileri()
geri()
sol()