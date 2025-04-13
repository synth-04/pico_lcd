from pico_lcd import LCDDisplay, TextScroller, Menu
from picozero import Button

# Initialize LCD with the correct size (change to rows=2, cols=16 if needed)
lcd = LCDDisplay(rows=4, cols=20)

# Function to load and scroll a text file
def show_page(filename):
    scroller = TextScroller(lcd, filename, mode='page')
    scroller.show()

    # Reassign buttons to scroll through the text
    btn_up.when_pressed = scroller.scroll_up
    btn_down.when_pressed = scroller.scroll_down

# Callback to handle menu selection
def menu_callback(selected):
    if selected == "Page 1":
        show_page("page1.txt")
    elif selected == "Page 2":
        show_page("page2.txt")
    elif selected == "Credits":
        lcd.write_full(["Created by", "Gabriele Di Pinto"])
    elif selected == "Exit":
        lcd.write_full(["Exiting..."])

# Define menu items
menu_items = ["Page 1", "Page 2", "Credits", "Exit"]

# Create the menu
menu = Menu(lcd, menu_items, callback=menu_callback)

# Define physical buttons (change pin numbers if needed)
btn_up = Button(16)
btn_down = Button(17)
btn_sel = Button(18)

# Assign button actions to menu navigation
btn_up.when_pressed = menu.scroll_up
btn_down.when_pressed = menu.scroll_down
btn_sel.when_pressed = menu.select
