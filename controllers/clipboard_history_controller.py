from flask import Blueprint, jsonify, request

from services.clipboard_service import ClipboardService

clipboard_history_controller = Blueprint('clipboard_history_controller', __name__)

clipboard_history_service = ClipboardService()
clipboard_history_service.start()


@clipboard_history_controller.route('/history', methods=['GET'])
def get_clipboard_history():
    if 'search' in request.args:
        return jsonify({'error': 'Search is not yet implemented'}), 501

    return jsonify({'history': clipboard_history_service.get_clipboard_history()}), 200


@clipboard_history_controller.route('/history/<int:index>', methods=['GET'])
def set_clipboard(index):
    return jsonify({'clipboard': clipboard_history_service.set_clipboard(index)}), 200


def shutdown_server():
    clipboard_history_service.stop()
    func = request.environ.get('werkzeug.server.shutdown')
    if not func:
        return jsonify({'error': 'Not running with the Werkzeug Server'}), 500
    func()


@clipboard_history_controller.route('/shutdown', methods=['POST'])
def close_application():
    shutdown_server()
    return jsonify({'success': 'Application stopped, you can now close this browser window.'}), 200
