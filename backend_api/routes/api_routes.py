from flask import Flask
from controllers.model_controller import model_blueprint
from controllers.gpu_controller import gpu_blueprint

app = Flask(__name__)

app.register_blueprint(model_blueprint, url_prefix='/api/model')
app.register_blueprint(gpu_blueprint, url_prefix='/api/gpu')

if __name__ == "__main__":
    app.run(debug=True)
