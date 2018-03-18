from mearm_controller import *
from muse_controller import *
import time

meArm = MeArm('COM6', 115200);
time.sleep(2);
previousTime = time.time();
halt = False;
resume = False;
try:
  while 1:
    if readHaltSignal():
      if not halt: 
        meArm.setMessages(danceTopR[:]);
        if (len(danceTopR) > 2):
          danceTopR = danceTopR[1:]
        print "settingMessage", repr(danceTopR)
      halt = True;
      resume = False;
    if readResumeSignal():
      if not resume: 
        meArm.setMessages(danceBotL[:]);
        print "settingMessage", repr(danceBotL)
        if (len(danceBotL) > 2):
          danceBotL = danceBotL[1:]
        
      resume = True;
      halt = False;
    if (time.time() - previousTime > 1):
      previousTime = time.time();
      print "writing", meArm.messages[0];
      meArm.write();
finally:
  meArm.close();