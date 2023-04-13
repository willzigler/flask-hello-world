import os
from flask import Flask, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base

Base = automap_base()

engine = create_engine(os.getenv('DATABASE_URI_E'))

Base.prepare(engine, reflect=True)


Test = Base.classes.test

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello, world'

@app.route('/api')
def test():
    cols = ['id', 'val']
    data = Test.query.all()
    result = [{col: getattr(d, col) for col in cols} for d in data]
    return jsonify(result=result)
