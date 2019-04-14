from flask import Flask, render_template
from flask_cors import CORS

from controllers.clipboard_history_controller import clipboard_history_controller

PREFIX = '/api/v1'

app = Flask(__name__, template_folder='templates', static_folder='static')

app.config['JSON_SORT_KEYS'] = False
app.secret_key = 'clipboard'

app.register_blueprint(clipboard_history_controller, url_prefix=PREFIX)

CORS(app)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
