from flask import Flask
import os

from blueprints.main_blueprint import main_blueprint

os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

app = Flask(__name__)
SECRET_KEY = os.urandom(32)

app.register_blueprint(main_blueprint)

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SECRET_KEY'] = SECRET_KEY

if __name__ == '__main__':
    app.run()
