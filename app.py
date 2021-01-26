import os
from flask import Flask, flash, request, render_template, url_for
from flask_restful import Resource, Api
import templates

import diagnose

UPLOAD_FOLDER = '/home/ruxuge/PycharmProjects/TeleMed_Api/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__.split('.')[0])
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["DEBUG"] = True

api = Api(app)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if request.files:
            file = request.files['img1.jpeg']
            file.save('/home/ruxuge/PycharmProjects/TeleMed_Api/uploads/img1.jpeg')
        elif request.path:
            return print("bad value")
        var = diagnose.main('uploads/img1.jpeg')
        return goodResponse(var)
    else:
        return badResponse()


@app.route('/goodResponse')
def goodResponse(var):
    return 'Image is sent and result is '
    # return res


@app.route('/badResponse')
def badResponse():
    return 'Fail'


with app.test_request_context():
    print(url_for('goodResponse'))
    print(url_for('badResponse'))

# api.add_resource(upload_file, '/', '/upload_file')

if __name__ == '__main__':
    app.run(port='5000')
