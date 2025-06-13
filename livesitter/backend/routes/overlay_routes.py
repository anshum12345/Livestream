from flask import Blueprint, request, jsonify
from models.overlay import Overlay
from bson import ObjectId
from bson.json_util import dumps

overlay_bp = Blueprint('overlay', __name__)

@overlay_bp.route('/overlays', methods=['POST'])
def create_overlay():
    data = request.get_json()
    result = Overlay.create_overlay(mongo.db, data)
    return jsonify({"id": str(result.inserted_id)}), 201

@overlay_bp.route('/overlays', methods=['GET'])
def get_all_overlays():
    overlays = Overlay.get_all_overlays(mongo.db)
    return dumps(overlays), 200

@overlay_bp.route('/overlays/<overlay_id>', methods=['GET'])
def get_overlay(overlay_id):
    overlay = Overlay.get_overlay(mongo.db, overlay_id)
    if overlay:
        return dumps(overlay), 200
    return jsonify({"error": "Overlay not found"}), 404

@overlay_bp.route('/overlays/<overlay_id>', methods=['PUT'])
def update_overlay(overlay_id):
    data = request.get_json()
    result = Overlay.update_overlay(mongo.db, overlay_id, data)
    if result.modified_count > 0:
        return jsonify({"message": "Overlay updated"}), 200
    return jsonify({"error": "Overlay not found"}), 404

@overlay_bp.route('/overlays/<overlay_id>', methods=['DELETE'])
def delete_overlay(overlay_id):
    result = Overlay.delete_overlay(mongo.db, overlay_id)
    if result.deleted_count > 0:
        return jsonify({"message": "Overlay deleted"}), 200
    return jsonify({"error": "Overlay not found"}), 404