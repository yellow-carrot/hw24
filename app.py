from flask import Flask

from db import db
from views import main_bp, test_bp
from config import Config


def create_app(config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    app.register_blueprint(main_bp)
    app.register_blueprint(test_bp)
    return app


if __name__ == '__main__':
    app = create_app(Config)
    app.run(host='0.0.0.0', port=12345)
