import os
from flask import jsonify
from models.model import Model
from app import db
from utils.optimization import optimize_model

class ModelService:
    def upload_model(self, model_file):
        filename = model_file.filename
        filepath = os.path.join('/models', filename)
        model_file.save(filepath)

        new_model = Model(name=filename, status='uploaded')
        db.session.add(new_model)
        db.session.commit()

        optimize_model(filepath)

        new_model.status = 'optimized'
        db.session.commit()

        return {'message': 'Model uploaded and optimized successfully'}

    def monitor_models(self):
        models = Model.query.all()
        return [{'id': model.id, 'name': model.name, 'status': model.status} for model in models]
