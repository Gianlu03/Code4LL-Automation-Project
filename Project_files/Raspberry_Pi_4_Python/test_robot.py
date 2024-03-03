import linetracking as lntr
import move
import servo
import time
import ultra
import robot
import threading as thread
import mysql.connector
from mysql.connector import Error


'''
count=-4
while(count<5):
    servo.arm_pos(count)
    count+=1
    time.sleep(1)
    
servo.hand(-180)
time.sleep(1)
servo.hand(180)
time.sleep(1)

servo.wrist(-15)
time.sleep(1)
servo.wrist(15)
time.sleep(1)

move.moveArcade(50,10)

linetracking.status_left()
ultra.checkdist()

for e in range(10):
  print(ultra.checkdist())
  time.sleep(.2)
'''
    
'''
comando = input("Inserisci:")


while comando != "stop":

  if comando == "d":
    robot.turn_right_forward(90)
    
  if comando == "a":
    robot.turn_left_forward(90)
    
  if comando == "w":
    robot.move_forward(2)
    move.motorStop()
    
  if comando == "s":
    robot.move_backwards(2)
    move.motorStop()
    
  comando = input("Inserisci:")

'''

def trackingRight():
  print(lntr.status_right())
  return lntr.status_right()
   
def trackingMiddle():
  print(lntr.status_middle())
  return lntr.status_middle()
  
def trackingLeft():
  print(lntr.status_left())
  return lntr.status_left()
  
'''
t1 = thread.Thread(trackingRight())
t2 = thread.Thread(trackingMiddle())
t3 = thread.Thread(trackingLeft())

comando = " ";

while comando != "stop":
  comando = input("Inserisci");
  
while True:
    print("Left: %d, Middle: %d, Right %d" % (lntr.status_left(), lntr.status_middle(), lntr.status_right()))

t_moveForward = thread.Thread(target=robot.move_forward(1000))
t_trackingMiddle = thread.Thread(trackingMiddle())

while True:
  t_moveForward.start()
  Sleep(2)
  t_moveForward.start()
  
'''

class moveBackwardThread(thread.Thread):
  check = 0
  
  def __init__(self):
    thread.Thread.__init__(self)
    check = 0

  def run(self):
    while True:
      if self.check == 1:
        move.motorStop()
        break
      robot.move_backwards_slow(0.05)
  
  def stop(self):
    self.check = 1

class moveForwardThread(thread.Thread):
  check = 0
  
  def __init__(self):
    thread.Thread.__init__(self)
    check = 0

  def run(self):
    while True:
      if self.check == 1:
        move.motorStop()
        break
      robot.move_forward(0.05)
  
  def stop(self):
    self.check = 1
  ''' 
class correctForwardThread(thread.Thread):
  check = 0
  
  def __init__(self):
    thread.Thread.__init__(self)
    check = 0
  
  def run(self):
    while True:
      if self.check == 1:
          move.motorStop()
          break
      if (lntr.status_middle() == 1 and lntr.status_right() == 1) or (lntr.status_middle() == 0 and lntr.status_right() == 1):
        print("correzione a sinistra")
        robot.turn_left_forward(10)
      if (lntr.status_middle() == 1 and lntr.status_left() == 1) or (lntr.status_middle() == 0 and lntr.status_left() == 1):
        print("correzione a destra")
        robot.turn_right_forward(10)
      
        
  def stop(self):
    self.check = 1 
'''   
class correctForwardThread(thread.Thread):
  check = 0
  
  def __init__(self):
    thread.Thread.__init__(self)
    check = 0
  
  def run(self):
    while True:
      if self.check == 1:
          move.motorStop()
          break
      if (lntr.status_left() == 0 and lntr.status_middle() == 1 and lntr.status_right() == 0) or (lntr.status_left() == 1 and lntr.status_middle() == 1 and lntr.status_right() == 1) or (lntr.status_left() == 0 and lntr.status_middle() == 0 and lntr.status_right() == 0):
        robot.move_forward(0.05)
      elif (lntr.status_middle() == 1 and lntr.status_right() == 1) or (lntr.status_middle() == 0 and lntr.status_right() == 1):
        move.motorStop()
        print("correzione a sinistra")
        robot.turn_left_forward(10)
      elif (lntr.status_middle() == 1 and lntr.status_left() == 1) or (lntr.status_middle() == 0 and lntr.status_left() == 1):
        move.motorStop()
        print("correzione a destra")
        robot.turn_right_forward(10)
      
        
  def stop(self):
    self.check = 1 



class correctBackwardThread(thread.Thread):
  check = 0
  
  def __init__(self):
    thread.Thread.__init__(self)
    check = 0
  
  def run(self):
    while True:
      if self.check == 1:
          move.motorStop()
          break
      if (lntr.status_middle() == 1 and lntr.status_right() == 1) or (lntr.status_middle() == 0 and lntr.status_right() == 1):
        print("correzione a sinistra")
        robot.turn_left_backward(10)
      if (lntr.status_middle() == 1 and lntr.status_left() == 1) or (lntr.status_middle() == 0 and lntr.status_left() == 1):
        print("correzione a destra")
        robot.turn_right_backward(10)
        
  def stop(self):
    self.check = 1 




'''
class trackingRightThread(thread.Thread):

  check = 0

  def __init__(self):
    thread.Thread.__init__(self)
    
  def run(self):
    print("start tracking right")
    while True:
      trackingRight()
      time.sleep(2)
      if self.check == 1:
        break
    print("Stop tracking right")
  
  def stopRun(self, checkPass):
    self.check = checkPass

  
  
tr = trackingRightThread()
print("ciao")
tr.start()
check = input("inserisci:")
tr.stopRun(int(check))

tr1 = moveForwardThread()
tr1.start()
time.sleep(2)
tr1.stop()
'''
def intersection():
  print("Arrivo all'incrocio in avanti")
  #tr1 = moveForwardThread()
  tr3 = correctForwardThread()
  #tr1.start()
  tr3.start()
  while True:
    #print("Left: %d, Middle: %d, Right %d" % (lntr.status_left(), lntr.status_middle(), lntr.status_right()))
    if lntr.status_left() == 1 and (lntr.status_middle() == 1 and lntr.status_right() == 1):
      #tr1.stop()
      tr3.stop()
      break
  #robot.move_forward(0.02)
  print("Left: %d, Middle: %d, Right %d" % (lntr.status_left(), lntr.status_middle(), lntr.status_right()))
  print("Arrivoto!")
  time.sleep(1)

def returnToRowLine():
  print("Arrivo all'incrocio all'indietro")
  tr1 = moveBackwardThread()
  #tr3 = correctBackwardThread()
  tr1.start()
  #tr3.start()
  time.sleep(0.5)
  while True:
    #print("Left: %d, Middle: %d, Right %d" % (lntr.status_left(), lntr.status_middle(), lntr.status_right()))
    if lntr.status_left() == 1 and (lntr.status_middle() == 1 and lntr.status_right() == 1):
      tr1.stop()
      #tr3.stop()
      break
      
  print("Arrivoto!")
  print("Left: %d, Middle: %d, Right %d" % (lntr.status_left(), lntr.status_middle(), lntr.status_right()))
  time.sleep(1)

'''
intersection()
time.sleep(2)
print("incrocio")
robot.move_forward(0.1)
robot.turn_left_forward(90)


robot.move_forward(0.1)
robot.turn_right_forward(90)

time.sleep(2)
intersection()

'''

class position():
  wSide = "" #R/L 
  shelfRow = "" #Bottom (B), Center (C), Up(U), Start(S)
  shelfSide = "" #Bottom (B), Up (U)
  rowLine = "" #1 - 8
  
  def __init__(self, wSide, shelfRow, shelfSide, rowLine):
    self.wSide = wSide
    self.shelfRow = shelfRow
    self.shelfSide = shelfSide
    self.rowLine = rowLine
    
  def getWSide(self):
    return self.wSide

  def getShelfRow(self):
    return self.shelfRow
    
  def getShelfSide(self):
    return self.shelfSide
    
  def getRowLine(self):
    return self.rowLine
    
    
    
class moveToPosition():

  robotPosition = None
  packagePosition = None
  ShelfRowPackage = 0
  ShelfRowRobot = 0
  
  def __init__(self, robotPosition, packagePosition):
    self.robotPosition = robotPosition
    self.packagePosition = packagePosition
    self.ShelfRowPackage = 0
    self.ShelfRowRobot = 0

  def convertShelfRow(self):
    if self.robotPosition.getShelfRow() == 'B' :
      self.ShelfRowRobot = 1
    elif self.robotPosition.getShelfRow() == 'C' :
      self.ShelfRowRobot = 3
    elif self.robotPosition.getShelfRow() == 'U' :
      self.ShelfRowRobot = 5
    elif self.robotPosition.getShelfRow() == 'S' :
      self.ShelfRowRobot = 0

    if self.packagePosition.getShelfRow() == 'B' :
      self.ShelfRowPackage = 1
    elif self.packagePosition.getShelfRow() == 'C' :
      self.ShelfRowPackage = 3
    elif self.packagePosition.getShelfRow() == 'U' :
      self.ShelfRowPackage = 5
    elif self.packagePosition.getShelfRow() == 'S' :
      self.ShelfRowPackage = 0

    if self.robotPosition.getShelfSide() == 'U':
      self.ShelfRowRobot = self.ShelfRowRobot + 1

    if self.packagePosition.getShelfSide() == 'U':
      self.ShelfRowPackage = self.ShelfRowPackage + 1
    
  def goto(self):
    self.convertShelfRow()
    if self.robotPosition.getWSide() == "L":
      if self.robotPosition.getShelfSide() == 'B':
        returnToRowLine()
        if self.packagePosition.getShelfRow() == self.robotPosition.getShelfRow() and self.packagePosition.getShelfSide() == self.robotPosition.getShelfSide():#il pacco si trova sulla stessa line in cui è situato il robot
          if self.robotPosition.getRowLine() < self.packagePosition.getRowLine():
            robot.move_forward(0.05)
            time.sleep(1)
            robot.turn_left_forward(90)
            distance = self.packagePosition.getRowLine() - self.robotPosition.getRowLine()
            temp = 0
            while temp < distance:
              temp += 1
              intersection()
            robot.move_forward(0.05)
            robot.turn_right_forward(90)
            intersection()
          else:
            robot.move_forward(0.1)
            robot.turn_right_forward(90)
            distance = self.robotPosition.getRowLine() - self.packagePosition.getRowLine()
            temp = 0
            while temp < distance:
              temp += 1
              intersection()
            robot.move_forward(0.05)
            robot.turn_left_forward(90)
            intersection()
        else:
          robot.move_forward(0.05)
          robot.turn_right_forward(90)
          distance = self.robotPosition.getRowLine()
          temp = 0
          while temp < distance:
            temp += 1
            intersection()
      else:
        returnToRowLine()
        if self.packagePosition.getShelfRow() == self.robotPosition.getShelfRow() and self.packagePosition.getShelfSide() == self.robotPosition.getShelfSide():#il pacco si trova sulla stessa line in cui è situato il robot
          if self.robotPosition.getRowLine() < self.packagePosition.getRowLine():
            robot.move_forward(0.1)
            robot.turn_right_forward(90)
            distance = self.packagePosition.getRowLine() - self.robotPosition.getRowLine()
            temp = 0
            while temp < distance:
              temp += 1
              intersection()
            robot.move_forward(0.1)
            robot.turn_left_forward(90)
            intersection()
          else:
            robot.move_forward(0.1)
            robot.turn_left_forward(90)
            distance = self.robotPosition.getRowLine() - self.packagePosition.getRowLine()
            temp = 0
            while temp < distance:
              temp += 1
              intersection()
            robot.move_forward(0.1)
            robot.turn_right_forward(90)
            intersection()
        else:
          robot.move_forward(0.1)
          robot.turn_left_forward(90)
          distance = self.robotPosition.getRowLine()
          temp = 0
          while temp < distance:
            temp += 1
            intersection()
    elif self.robotPosition.getWSide() == "R":
      if self.robotPosition.getShelfSide() == 'B':
        returnToRowLine()
        if self.packagePosition.getShelfRow() == self.robotPosition.getShelfRow() and self.packagePosition.getShelfSide() == self.robotPosition.getShelfSide():  # il pacco si trova sulla stessa line in cui è situato il robot
          if self.robotPosition.getRowLine() < self.packagePosition.getRowLine():
            robot.move_forward(0.1)
            robot.turn_right_forward(90)
            distance = self.robotPosition.getRowLine() - self.packagePosition.getRowLine()
            temp = 0
            while temp < distance:
              temp += 1
              intersection()
            robot.move_forward(0.1)
            robot.turn_left_forward(90)
            intersection()
          else:
            robot.move_forward(0.1)
            robot.turn_left_forward(90)
            distance = self.packagePosition.getRowLine() - self.robotPosition.getRowLine()
            temp = 0
            while temp < distance:
              temp += 1
              intersection()
            robot.move_forward(0.1)
            robot.turn_right_forward(90)
            intersection()
        else:
          robot.move_forward(0.1)
          robot.turn_right_forward(90)
          distance = self.robotPosition.getRowLine() - 4
          temp = 0
          while temp < distance:
            temp += 1
            intersection()
      else:
        returnToRowLine()
        if self.packagePosition.getShelfRow() == self.robotPosition.getShelfRow() and self.packagePosition.getShelfSide() == self.robotPosition.getShelfSide():  # il pacco si trova sulla stessa line in cui è situato il robot
          if self.robotPosition.getRowLine() < self.packagePosition.getRowLine():
            robot.move_forward(0.1)
            robot.turn_left_forward(90)
            distance = self.packagePosition.getRowLine() - self.robotPosition.getRowLine()
            temp = 0
            while temp < distance:
              temp += 1
              intersection()
            robot.move_forward(0.1)
            robot.turn_right_forward(90)
            intersection()
          else:
            robot.move_forward(0.1)
            robot.turn_right_forward(90)
            distance = self.robotPosition.getRowLine() - self.packagePosition.getRowLine()
            temp = 0
            while temp < distance:
              temp += 1
              intersection()
            robot.move_forward(0.1)
            robot.turn_left_forward(90)
            intersection()
        else:
          robot.move_forward(0.1)
          robot.turn_right_forward(90)
          distance = self.robotPosition.getRowLine() - 4
          temp = 0
        while temp < distance:
          temp += 1
          intersection()


    if self.packagePosition.getShelfRow() != self.robotPosition.getShelfRow() :
      if self.robotPosition.getWSide() == "L":
        if self.ShelfRowRobot < self.ShelfRowPackage:
          robot.move_forward(0.1)
          robot.turn_left_forward(90)
          distance = self.ShelfRowPackage - self.ShelfRowRobot
          temp = 0
          while temp < distance:
            temp += 1
            intersection()
          if self.packagePosition.getWSide() == "L":
            robot.move_forward(0.1)
            robot.turn_left_forward(90)
          elif self.packagePosition.getWSide() == "R":
            robot.move_forward(0.1)
            robot.turn_right_forward(90)
        elif self.ShelfRowRobot > self.ShelfRowPackage:
          robot.move_forward(0.1)
          robot.turn_right_forward(90)
          distance = self.ShelfRowRobot - self.ShelfRowPackage
          temp = 0
          while temp < distance:
            temp += 1
            intersection()
          if self.packagePosition.getWSide() == "L":
            robot.move_forward(0.1)
            robot.turn_right_forward(90)
          elif self.packagePosition.getWSide() == "R":
            robot.move_forward(0.1)
            robot.turn_left_forward(90)
      elif self.robotPosition.getWSide() == "R":
        if self.ShelfRowRobot < self.ShelfRowPackage:
          robot.move_forward(0.1)
          robot.turn_right_forward(90)
          distance = self.ShelfRowRobot - self.ShelfRowPackage
          temp = 0
          while temp < distance:
            temp += 1
            intersection()
          if self.packagePosition.getWSide() == "L":
            robot.move_forward(0.1)
            robot.turn_left_forward(90)
          elif self.packagePosition.getWSide() == "R":
            robot.move_forward(0.1)
            robot.turn_right_forward(90)
        elif self.ShelfRowRobot > self.ShelfRowPackage:
          robot.move_forward(0.1)
          robot.turn_left_forward(90)
          distance = self.ShelfRowRobot - self.ShelfRowPackage
          temp = 0
          while temp < distance:
            temp += 1
            intersection()
          if self.packagePosition.getWSide() == "L":
            robot.move_forward(0.1)
            robot.turn_right_forward(90)
          elif self.packagePosition.getWSide() == "R":
            robot.move_forward(0.1)
            robot.turn_left_forward(90)
      elif self.robotPosition.getWSide() == "S":
        distance = self.ShelfRowRobot - self.ShelfRowPackage
        temp = 0
        while temp < distance:
          temp += 1
          intersection()
        if self.packagePosition.getWSide() == "L":
          robot.move_forward(0.1)
          robot.turn_left_forward(90)
        elif self.packagePosition.getWSide() == "R":
          robot.move_forward(0.1)
          robot.turn_right_forward(90)

      if self.packagePosition.getWSide() == "L":
        distance = self.packagePosition.getRowLine()
      else:
        distance = self.packagePosition.getRowLine() - 4

      temp = 0
      while temp < distance:
        temp += 1
        intersection()

      if (self.packagePosition.getWSide() == "L" and self.robotPosition.getShelfSide() == 'U') or (self.packagePosition.getWSide() == "R" and self.robotPosition.getShelfSide() == 'B'):
        robot.move_forward(0.1)
        robot.turn_left_forward(90)
      else:
        robot.move_forward(0.1)
        robot.turn_right_forward(90)

      intersection()

'''
Package = position("L","B","B",1)
Robot = position("L","B","B",3)


Move = moveToPosition(Robot,Package)
Move.goto()

Package = position("L","B","B",2)
Robot = position("L","B","B",1)

Move = moveToPosition(Robot,Package)
Move.goto()

'''

Robot = position("L","B","B",3)

while True:
  try:
      connection = mysql.connector.connect(host='192.168.34.36',
                                           database='code4ll',
                                           user='Remote',
                                           password='rasp')
      if connection.is_connected():
          cursor = connection.cursor()
          cursor.execute("select * from operation where IdOperation >= 0;")
          record = cursor.fetchone()
          print(record)
          if record:
            cursor.execute("delete from operation where IdOperation >= 0;")
            connection.commit()
            Package = position(record[1],record[2],record[3],record[4])
            print("Package: " + Package.getWSide() + " " + Package.getShelfRow() + " " + Package.getShelfSide() + " " + str(Package.getRowLine()))
            #Move = moveToPosition(Robot,Package)
            #Move.goto()
            #Robot = Package
            break
            print("nuovo valore")
  except Error as e:
      print("Error while connecting to MySQL", e)
  finally:
      if connection.is_connected():
          cursor.close()
          connection.close()
          print("MySQL connection is closed")
  time.sleep(5)