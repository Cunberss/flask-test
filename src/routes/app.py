from flask import Blueprint, render_template

app_bp = Blueprint(name='app', import_name=__name__, url_prefix='/app/')


@app_bp.get('/')
def app_main():
    return render_template('index.html')