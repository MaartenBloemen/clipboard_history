import datetime
import threading

from services import pyperclip_fixed as pyperclip


class ClipboardService(threading.Thread):
    def __init__(self, max_length=-1):
        self.running = True
        self.clipboard_history = []
        self.__last_clipboard_text = ''
        self.__max_length = max_length

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
            now = datetime.datetime.now()
            if self.__last_clipboard_text != clipboard_text and clipboard_text:
                self.clipboard_history.insert(0, {'text': clipboard_text, 'time': now.time().strftime('%H:%M:%S'),
                                                  'date': now.date().strftime('%d/%m/%Y')})
                if self.__max_length != -1:
                    self.clipboard_history = self.clipboard_history[:self.__max_length]
                self.__last_clipboard_text = clipboard_text
