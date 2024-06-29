from flask import Blueprint, request, jsonify
from services.model_service import ModelService

model_blueprint = Blueprint('model', __name__)
model_service = ModelService()

@model_blueprint.route('/upload', methods=['POST'])
def upload_model():
    model_file = request.files['file']
    response = model_service.upload_model(model_file)
    return jsonify(response)

@model_blueprint.route('/monitor', methods=['GET'])
def monitor_models():
    response = model_service.monitor_models()
    return jsonify(response)
