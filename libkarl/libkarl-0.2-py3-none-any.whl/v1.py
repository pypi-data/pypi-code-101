from machine import Pin, PWM, ADC
from time import sleep_ms

LOW = 0

HIGH = 65535

def delay(ms):
    sleep_ms(int(ms))

class Led:
    
    def __init__(self, pin):
        self.pin = Pin(pin)
        self.pwm = PWM(self.pin)
        self.set_value(LOW)

    def set_value(self, value):
        self.value = value
        self.pwm.freq(1000)
        self.pwm.duty_u16(value)

    def get_value(self):
        return self.value

    def off(self):
        self.set_value(LOW)

    def on(self):
        self.set_value(HIGH)

    def toggle(self):
        self.set_value(HIGH - self.value)
        
class Servo:
    
    value = 90
    
    def __init__(self, pin):
        self.pin = Pin(pin)
        self.pwm = PWM(self.pin)
        self.pwm.freq(50)
        self.set_value(90)
        
    def set_value(self, value):
        if value > 180:
            value = 180
        elif value < 0:
            value = 0
        
        self.value = value
        
        maxDuty = 9000
        minDuty = 1000
        newDuty = minDuty + (maxDuty - minDuty) * (value / 180)
        self.pwm.duty_u16(int(newDuty))
        
    def get_value(self):
        return self.value

class Button:
    
    def __init__(self, pin):
        self.pin = Pin(pin, Pin.IN, Pin.PULL_UP)
        
    def get_value(self):
        return 1 - self.pin.value()

    def is_pressed(self):
        if self.get_value() == 1:
            return True
        else:
            return False

class Rotary:

    def __init__(self, pin):
        self.adc = ADC(Pin(pin))
        
    def get_value(self):
        return self.adc.read_u16()

class Speaker:

    def __init__(self, pin):
        self.pin = Pin(pin)
        self.pwm = PWM(self.pin)
        self.no_tone()

    def tone(self, frequency):
        self.pwm.freq(frequency)
        self.pwm.duty_u16(32767)

    def no_tone(self):
        self.pwm.deinit()
        
    def getFrequency(self, octave, note):
        frac = pow(2, 1.0/12.0)
        base = 16.3516 * pow(2, octave - 1)
        freq = base * pow(frac, note)

        return freq
