def on_button_pressed_a():
    basic.pause(100)
input.on_button_pressed(Button.A, on_button_pressed_a)

def joystickState(sensor: number):
    global joystickStateResult
    joystickStateResult = "Steady"
    if sensor > 50 and sensor < 150:
        joystickStateResult = "Up"
    elif sensor > 1000:
        joystickStateResult = "Right"
    elif sensor > 450 and sensor < 550:
        joystickStateResult = "Down"
    elif sensor > 250 and sensor < 350:
        joystickStateResult = "Left"
    elif sensor > 150 and sensor < 250:
        joystickStateResult = "Pressed"
    return joystickStateResult


joystick = ""
joystickStateResult = ""
servoGround = 0
servoStep = 3
basic.pause(500)
servoGround = 90
servoHand = 90

def on_forever():
    global joystick, servoHand, servoGround
    joystick = joystickState(pins.analog_read_pin(AnalogReadWritePin.P1))
    if joystick == "Up":
        servoHand += 0 - servoStep
        if servoHand < 0:
            servoHand = 0
        
    elif joystick == "Right":
        servoGround += 0 - servoStep
        if servoGround < 0:
            servoGround = 0
        
    elif joystick == "Down":
        servoHand += servoStep
        if servoHand > 180:
            servoHand = 180
        
    elif joystick == "Left":
        servoGround += servoStep
        if servoGround > 180:
            servoGround = 180
        
    elif joystick == "Pressed":
        pass
    else:
        pass
basic.forever(on_forever)
