from flask import Flask
from todo import main as todo_routes


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.register_blueprint(todo_routes)


if __name__ == '__main__':
    config = dict(
        debug=True,
        host='',
        port=3000,
    )
    app.run(**config)
