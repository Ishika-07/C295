from controller import Robot, Keyboard, Motion

robot = Robot()
timestep = 32

keyboard = Keyboard()
keyboard.enable(timestep)

wave = Motion('../../motions/wave.motion')
key = -1

while robot.step(timestep) != -1:
    key = keyboard.getKey()
    
    if(key == Keyboard.UP):
        wave.play()