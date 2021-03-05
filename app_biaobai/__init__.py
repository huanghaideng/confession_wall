from flask import Flask

def app_wsgi():
    app = Flask(__name__)

    from app_biaobai.main import bp as main_bp
    app.register_blueprint(main_bp)
    return app