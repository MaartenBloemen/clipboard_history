import datetime
import threading

import pyperclip


class ClipboardService(threading.Thread):
    def __init__(self):
        self.running = True
        self.clipboard_history = []
        self.__last_clipboard_text = ''

        threading.Thread.__init__(self)

    def get_clipboard_history(self):
        return self.clipboard_history

    def set_clipboard(self, clipboard_history_index):
        clipboard_dict = self.clipboard_history[clipboard_history_index]
        pyperclip.copy(clipboard_dict.get('text'))
        return clipboard_dict.get('text')

    def clear_clipboard_history(self):
        self.clipboard_history = []

    def stop(self):
        self.running = False
        threading.Thread.join(self, 1)

    def run(self):
        while self.running:
            clipboard_text = pyperclip.paste()
            time = datetime.datetime.now().time()
            if self.__last_clipboard_text != clipboard_text and clipboard_text:
                self.clipboard_history.insert(0, {'text': clipboard_text, 'time': time.strftime('%H:%M:%S'),
                                                  'date': time.strftime('%d/%m/%Y')})
                self.__last_clipboard_text = clipboard_text
