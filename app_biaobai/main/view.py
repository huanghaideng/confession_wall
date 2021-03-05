from app_biaobai.main import bp
from flask import render_template

@bp.route('/')
@bp.route('/biaobai')
def index():
    return render_template('index.html')