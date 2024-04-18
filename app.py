from flask import Flask
from app.routes import api_op
from app.db import db

app = Flask(__name__)
app.register_blueprint(api_op)

if __name__ == '__main__':
    app.run(debug=True, port=4000)
