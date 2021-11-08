import sys, time

def type(text, speed=0.3):
    for character in text:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(speed)
