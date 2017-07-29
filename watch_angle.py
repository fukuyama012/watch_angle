# -*- coding: utf-8 -*- 
# angle monitoring system by TWELITE 2525A
# * you have to prepare TWELITE 2525A device and USB MONOSTICK
#
# Source available at https://github.com/fukuyama012/watch_angle
# This is distributed under the terms of the MIT license.

import serial
from datetime import datetime
from lib import LineNotify
from config import config

#acceleration value range about -100 ~ 100
#For example) z-axis value -100 is device facedown state
ANGLE_THRESHOLD = -50
AXIS = "z"

def debug_print(m):
    """debug print"""
    #if len(m) == 16:
    print('親機連番[{}] 続き番号[{}] 電波強度[{}] 電池[{}]'.format(m[1], m[4], m[3], m[6]))
    print(' X[{}] Y[{}] Z[{}] 動き[{}]'.format(m[12], m[13], m[14], m[7]))


def alerm_angle(messages, axis = AXIS, threshold = ANGLE_THRESHOLD):
    """
    check angle
    
    :param messages: array device data
    :param axis: string which axis
    :param threshold: int amount for checking
    :return boolean: Needs Alerm or not
    """
    if axis == "x":
        angle = messages[12]
    elif axis == "y":
        angle = messages[13]
    elif axis == "z":
        angle = messages[14]
    else:
        return  False, 0
        
    if('-' in angle):
        angle = int(angle.replace("-", ""))
        angle = -angle
    else:
        angle = int(angle)
        
    if angle < threshold:
        return True, angle
    else:
        return False, angle
   
   
def notify(angle, count):    
    """
    notify core
    
    :param angle: int angle data
    :return: string Responce
    """
    obj_notify = LineNotify()
    res = obj_notify.notify(angle)
    print('[{}] {} {} {}'.format(count, datetime.now(), res, angle))
    
    
def main():
    """main"""
    count = 0
    s = serial.Serial(config.SERIAL_PORT, config.SERIAL_BITRATE)
    while True:
        line = s.readline()
        messages = str(line).split(";")
        if len(messages) == 16:
            #debug_print(messages)
            result, angle = alerm_angle(messages)
            if(result == True):
                count += 1
                notify(angle, count)


if __name__ == "__main__":
    main()