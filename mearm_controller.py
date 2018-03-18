import serial

CNTR = 'M09508.004.00\n'
TOPR = 'M05508.009.00\n'
TOPL = 'M11508.009.00\n'
BOTR = 'M05508.000.00\n'
BOTL = 'M11508.000.00\n'
CLAP = 'M09510.006.01\n'
dance = [TOPR, CNTR, TOPR, CNTR,
          TOPL, CNTR, TOPL, CNTR,
          BOTR, CNTR ,BOTR, CNTR,
          BOTL, CNTR, BOTL, CNTR,
          TOPR, CNTR, TOPL, CNTR,
          BOTR, CNTR, BOTL, CNTR,
          CLAP, CNTR, CLAP, CNTR]

danceTopR = [TOPR, CNTR]
danceBotL = [BOTL, CNTR]

class MeArm:
  port = '';
  serial = None;
  __halt__ = False;
  messages = [CNTR];
  def __init__(self, port, baud):
    self.port = port;
    self.serial = serial.Serial(port, baud);
  def halt(self):
    self.__halt__ = True;
  def resume(self):
    self.__halt__ = False;
  def write(self):
    if self.__halt__: return;
    self.serial.write(self.messages[0])
    self.messages.append(self.messages[0])
    self.messages = self.messages[1:]
  def close(self):
    self.serial.close();
  def setMessages(self, messages):
    self.messages = messages;