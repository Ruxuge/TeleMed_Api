import os
from flask import Flask, flash, request, render_template, url_for
from flask_restful import Resource, Api
import templates

import diagnose

UPLOAD_FOLDER = '/home/ruxuge/PycharmProjects/TeleMed_Api/uploads'
ALLOWED_EXTENSIONS = {'jpeg'}

app = Flask(__name__.split('.')[0])
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["DEBUG"] = True

api = Api(app)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if request.files:
            file = request.files['image.jpeg']
            file.save('/home/ruxuge/PycharmProjects/TeleMed_Api/uploads/image.jpeg')
        elif request.method == 'POST':
            return noValue()
        var = diagnose.main('uploads/img1.jpeg')
        return goodResponse(var)
    elif request.method != 'POST':
        return badRequest()


@app.route('/goodResponse')
def goodResponse(var):
    return 'Image is sent'
    # return res


@app.route('/badRequest')
def badRequest():
    return 'Bad Request'


@app.route('/noValue')
def noValue():
    return 'Image is require'


with app.test_request_context():
    print(url_for('goodResponse'))
    print(url_for('noValue'))
    print(url_for('badRequest'))


if __name__ == '__main__':
    app.run(port='5000')
