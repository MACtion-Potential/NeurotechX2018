from mearm_controller import MeArm
from muse_controller import *
import time

meArm = MeArm('COM6', 115200);
time.sleep(2);
previousTime = time.time();
try:
  while 1:
    if readHaltSignal():
      meArm.halt();
    if readResumeSignal():
      meArm.resume();
    if (time.time() - previousTime > 1):
      previousTime = time.time();
      meArm.write();
finally:
  meArm.close();