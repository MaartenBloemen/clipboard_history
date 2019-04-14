import datetime
import threading

import pyperclip


class ClipboardService(threading.Thread):
    def __init__(self):
        self.clipboard_history = []
        self.__last_clipboard_text = ''

        threading.Thread.__init__(self)

    def get_clipboard_history(self):
        return self.clipboard_history

    def set_clipboard(self, clipboard_history_index):
        clipboard_dict = self.clipboard_history[clipboard_history_index]
        print(clipboard_dict)
        pyperclip.copy(clipboard_dict.get('text'))
        return clipboard_dict.get('text')


    def run(self):
        while True:
            clipboard_text = pyperclip.paste()
            time = datetime.datetime.now().time()
            if self.__last_clipboard_text != clipboard_text:
                self.clipboard_history.append({'text': clipboard_text, 'time': time.strftime('%H:%M:%S')})
                self.__last_clipboard_text = clipboard_text
