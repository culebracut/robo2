import asyncio
import evdev
from evdev import InputDevice, categorize, ecodes, KeyEvent 
from jetbot import Robot

""" devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
for device in devices:
    print(device.path, device.name, device.phys) """

def scale(val, src, dst):
    """
    Scale the given value from the scale of src to the scale of dst.

    val: float or int
    src: tuple
    dst: tuple

    example: print(scale(99, (0.0, 99.0), (-1.0, +1.0)))
    """
    return (float(val - src[0]) / (src[1] - src[0])) * (dst[1] - dst[0]) + dst[0]

def scale_js_Y(value):
    return scale(value,(0,255),(1,-1))

def scale_js_X(value):
    return scale(value,(255,0),(1,-1))

# process joystick events
async def jsEvent(dev):
    xAxis = 0
    yAxis = 0
    speed = 0
    torque = 0
    midAxis = 128
    leftMotorSpeed = 0
    rightMotorSpeed = 0
    zeroSpeedOffset = 0.25

    robot = Robot()
    
    async for ev in dev.async_read_loop():
        if (ev.type == 3):   # analog
            # get the Axis values from the js.
            if (ev.code == 1):      # Y axis
                yAxis = ev.value    # maintain state
            elif (ev.code == 0):    # X axis
                xAxis = ev.value    # maintain state for both
            
            # Y axis values represent the speed, X the rotation
            # Y scales from 0-255 gamepad coordinates to 1 to-1 motor speed
            # X scales from 0-255 gamepad coordingates to -1 to 1 motor speed
            speed   = round(scale_js_Y(yAxis),2)
            torque  = round(scale_js_X(xAxis),2)

            # stop when speed approx zero
            if (speed > -zeroSpeedOffset and speed < zeroSpeedOffset):
                robot.stop()
                continue

            # combine speed and torque 
            leftMotorSpeed = speed
            rightMotorSpeed = speed

            if (xAxis > midAxis):       # rotate right
                leftMotorSpeed  = round((leftMotorSpeed  + torque), 2)
                rightMotorSpeed = round((rightMotorSpeed - torque), 2)
            else:                           # rotate left
                leftMotorSpeed  =  round((leftMotorSpeed  - torque), 2)
                rightMotorSpeed =  round((rightMotorSpeed + torque), 2)
        
            if   (leftMotorSpeed > 1):  leftMotorSpeed = 1
            elif (leftMotorSpeed < -1): leftMotorSpeed = -1
            elif (rightMotorSpeed > 1): rightMotorSpeed = 1
            elif (rightMotorSpeed < -1): rightMotorSpeed = -1
            
            # set motor speeds
            robot.set_motors(leftMotorSpeed, rightMotorSpeed)

            #print(repr(ev))
            print('x-axis: ', xAxis, '    y-axis:', yAxis, '    speed:',speed, '   torque:',  torque, '     left:', leftMotorSpeed, '    right:', rightMotorSpeed)

# Init
ps3dev = ""
print("Finding ps3 controller...")
devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
for device in devices:
    if (device.name.find('ShanWan') != -1):
        ps3dev = device.fn
print("Found  ", ps3dev)
joystick = evdev.InputDevice(ps3dev)

# Async loop
loop = asyncio.get_event_loop()
loop.run_until_complete(jsEvent(joystick))
