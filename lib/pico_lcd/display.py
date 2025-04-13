# Module: display.py - LCD handling (initialization, line/page writing)

from machine import I2C, Pin
from pico_lcd.drivers.I2C_LCD import I2CLcd  # Import from internal drivers

class LCDDisplay:
    def __init__(self, i2c_id=0, sda_pin=0, scl_pin=1, address=0x27, rows=4, cols=20):
        # Constructor: Initialize LCD with given I2C parameters and dimensions
        self.i2c = I2C(i2c_id, sda=Pin(sda_pin), scl=Pin(scl_pin), freq=400000)
        self.lcd = I2CLcd(self.i2c, address, rows, cols)
        self.rows = rows
        self.cols = cols
        self.clear()

    def clear(self):
        # Clear the LCD screen
        self.lcd.clear()

    def write_line(self, row, text):
        # Write a single line to the LCD
        if row < self.rows:
            self.lcd.move_to(0, row)
            text = str(text)
            if len(text) < self.cols:
                text = text + ' ' * (self.cols - len(text))
            else:
                text = text[:self.cols]
            self.lcd.move_to(0, row)
            self.lcd.putstr(text)

    def write_full(self, lines):
        # Write multiple lines to the LCD
        self.clear()
        for i, line in enumerate(lines):
            if i < self.rows:
                self.write_line(i, line)
