class TextScroller:
    def __init__(self, lcd_display, filepath, mode='page'):
        self.lcd = lcd_display
        self.filepath = filepath
        self.mode = mode  # 'page' or 'line'
        self.lines = []

        # Load the file and wrap lines by word while respecting explicit line breaks
        with open(filepath) as f:
            for line in f:
                self.lines.extend(self._wrap_line(line.rstrip()))

        self.index = 0  # Index of the first visible line

    def _wrap_line(self, line):
        # Manually wrap lines at word boundaries
        words = line.split(' ')
        wrapped_lines = []
        current_line = ''

        for word in words:
            if len(current_line) + len(word) + (1 if current_line else 0) <= self.lcd.cols:
                if current_line:
                    current_line += ' '
                current_line += word
            else:
                wrapped_lines.append(current_line)
                current_line = word

        if current_line:
            wrapped_lines.append(current_line)

        return wrapped_lines or ['']

    def show(self):
        # Display a window of lines based on current index and LCD height
        rows = self.lcd.rows
        window = self.lines[self.index:self.index + rows]
        self.lcd.write_full(window)

    def scroll_up(self):
        # Scroll up by one line or one page
        if self.index > 0:
            self.index -= 1 if self.mode == 'line' else self.lcd.rows
            self.show()

    def scroll_down(self):
        # Scroll down by one line or one page
        max_index = len(self.lines) - self.lcd.rows
        if self.index < max_index:
            self.index += 1 if self.mode == 'line' else self.lcd.rows
            self.show()