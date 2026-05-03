let joystickStateResult = ""
function joystickState (sensor: number) {
    joystickStateResult = "Steady"
    if (sensor > 50 && sensor < 150) {
        joystickStateResult = "Up"
    } else if (sensor > 1000) {
        joystickStateResult = "Right"
    } else if (sensor > 450 && sensor < 550) {
        joystickStateResult = "Down"
    } else if (sensor > 250 && sensor < 350) {
        joystickStateResult = "Left"
    } else if (sensor > 150 && sensor < 250) {
        joystickStateResult = "Pressed"
    }
    return joystickStateResult
}
