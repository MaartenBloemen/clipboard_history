import os
import sys

try:
    base_path = sys._MEIPASS
except Exception:
    base_path = os.path.abspath('.')

from flask import Flask, render_template
from flask_cors import CORS

from controllers.clipboard_history_controller import clipboard_history_controller

PREFIX = '/api/v1'

template_folder = os.path.join(base_path, 'templates')
static_folder = os.path.join(base_path, 'static')

app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)

app.config['JSON_SORT_KEYS'] = False
app.secret_key = 'clipboard'

app.register_blueprint(clipboard_history_controller, url_prefix=PREFIX)

CORS(app)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='localhost', port=8001)
