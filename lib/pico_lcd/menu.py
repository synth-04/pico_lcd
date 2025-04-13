# pico_lcd/menu.py - Simple interactive menu with navigation and selection
class Menu:
    def __init__(self, lcd_display, items, callback=None):
        self.lcd = lcd_display
        self.items = items
        self.index = 0      # Index of currently selected item
        self.offset = 0     # Index of topmost visible item on screen
        self.callback = callback  # Function to call on selection
        self.show()

    def show(self):
        # Render the visible portion of the menu
        lines = []
        for i in range(self.lcd.rows):
            pos = self.offset + i
            if pos < len(self.items):
                prefix = "> " if pos == self.index else "  "
                lines.append(prefix + self.items[pos])
        self.lcd.write_full(lines)

    def scroll_up(self):
        # Move selection up
        if self.index > 0:
            self.index -= 1
            if self.index < self.offset:
                self.offset -= 1
            self.show()

    def scroll_down(self):
        # Move selection down
        if self.index < len(self.items) - 1:
            self.index += 1
            if self.index >= self.offset + self.lcd.rows:
                self.offset += 1
            self.show()

    def select(self):
        # Call the associated callback with the selected item
        if self.callback:
            self.callback(self.items[self.index])

