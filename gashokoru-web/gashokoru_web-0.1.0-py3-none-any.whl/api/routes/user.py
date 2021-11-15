from flask import render_template, request
from . import *

# User homepage
def index():

    data = {
        'title': "Home | Gashokoru"
    }

    return render_template("index.html", **data), 200

# Document generating form
def generate(id):
    
    data = {
        'style_dir' : style_dir,
        'id'        : id
    }

    mapping = {
        1: 'user/generate_training.html'
    } 

    if id in mapping:
        return render_template(mapping[id], **data), 200
    else:
        return {'content':'Parameter <id> is out of bounds'}, 400

# POST receive for generate
# linked to generate(id)
def out_generate():
    ret = request.form
    return {'form': ret}