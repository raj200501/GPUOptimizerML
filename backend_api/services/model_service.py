import os
from flask import jsonify
from models.model import Model
from app import db
from utils.optimization_adapter import optimize_model_compat

class ModelService:
    def upload_model(self, model_file):
        filename = model_file.filename
        storage_dir = os.getenv(
            "MODEL_STORAGE_DIR",
            os.path.join(os.path.dirname(__file__), "..", "model_storage"),
        )
        storage_dir = os.path.abspath(storage_dir)
        os.makedirs(storage_dir, exist_ok=True)
        filepath = os.path.join(storage_dir, filename)
        model_file.save(filepath)

        new_model = Model(name=filename, status='uploaded')
        db.session.add(new_model)
        db.session.commit()

        optimize_model_compat(filepath)

        new_model.status = 'optimized'
        db.session.commit()

        return {'message': 'Model uploaded and optimized successfully'}

    def monitor_models(self):
        models = Model.query.all()
        return [{'id': model.id, 'name': model.name, 'status': model.status} for model in models]
