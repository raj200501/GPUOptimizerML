from flask import Blueprint, jsonify
from services.gpu_service import GpuService

gpu_blueprint = Blueprint('gpu', __name__)
gpu_service = GpuService()

@gpu_blueprint.route('/stats', methods=['GET'])
def get_gpu_stats():
    response = gpu_service.get_gpu_stats()
    return jsonify(response)
