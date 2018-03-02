import keyboard

def readHaltSignal():
  return keyboard.is_pressed('h');
def readResumeSignal():
  return keyboard.is_pressed('r');