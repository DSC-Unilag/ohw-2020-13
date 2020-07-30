from app import __call__,db,migrate
import os

app = __call__('default' or os.getenv('FLASK_CONFIG'))

@app.shell_context_processor
def make_shell_context():
    return dict(app=app,db=db)