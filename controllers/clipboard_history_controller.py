from flask import Blueprint, jsonify

from services.clipboard_service import ClipboardService

clipboard_history_controller = Blueprint('clipboard_history_controller', __name__)

clipboard_history_service = ClipboardService()
clipboard_history_service.start()


@clipboard_history_controller.route('/history', methods=['GET'])
def get_clipboard_history():
    return jsonify({'history': clipboard_history_service.get_clipboard_history()}), 200


@clipboard_history_controller.route('/history/<int:index>', methods=['GET'])
def set_clipboard(index):
    return jsonify({'clipboard': clipboard_history_service.set_clipboard(index)}), 200
