# pico_lcd

A lightweight MicroPython library for Raspberry Pi Pico that simplifies the use of I2C character LCDs (2x16 or 4x20).  
Includes support for text display, page/line scrolling, and interactive menus with button navigation.

---

## Features

- ✅ Easy initialization for I2C LCDs
- ✅ Line and full screen writing
- ✅ `TextScroller`: Scroll long text files by line or page
- ✅ `Menu`: Create interactive text menus with callback functions
- ✅ Word-wrapped scrolling that respects line breaks
- ✅ Fully compatible with buttons via `picozero.Button`

---

## Hardware Requirements

- Raspberry Pi Pico
- I2C LCD Display (16x2 or 20x4)
- 3 push buttons (for up, down, select)
- Proper wiring on GPIO (ex: SDA on GP0, SCL on GP1)

---

## Installation

Copy the following to your Pico:

```
/main.py (or example.py)
/page1.txt
/page2.txt
/lib/pico_lcd/
```

Make sure to include the internal `drivers/` folder inside `pico_lcd`.

---

## Example: Display menu and open text files

```python
from pico_lcd import LCDDisplay, TextScroller, Menu
from picozero import Button

lcd = LCDDisplay(rows=4, cols=20)

def show_page(filename):
    scroller = TextScroller(lcd, filename, mode='page')
    scroller.show()
    btn_up.when_pressed = scroller.scroll_up
    btn_down.when_pressed = scroller.scroll_down

def menu_callback(selected):
    if selected == "Page 1":
        show_page("page1.txt")
    elif selected == "Page 2":
        show_page("page2.txt")
    elif selected == "Credits":
        lcd.write_full(["Created by", "Your Name"])
    elif selected == "Exit":
        lcd.write_full(["Exiting..."])

menu_items = ["Page 1", "Page 2", "Credits", "Exit"]
menu = Menu(lcd, menu_items, callback=menu_callback)

btn_up = Button(10)
btn_down = Button(11)
btn_sel = Button(12)

btn_up.when_pressed = menu.scroll_up
btn_down.when_pressed = menu.scroll_down
btn_sel.when_pressed = menu.select
```

---

## File structure

```
/main.py
/page1.txt
/page2.txt
/lib/
  └── pico_lcd/
      ├── __init__.py
      ├── display.py
      ├── menu.py
      ├── scroller.py
      └── drivers/
          ├── I2C_LCD.py
          └── LCD_API.py
```

---
