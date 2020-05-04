from flask import Flask, render_template, send_file
from os.path import join, dirname, realpath
app = Flask(__name__)

app.debug = True


@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/v2')
def index_pagev2():
    return render_template('v2/index.html')

@app.route('/v2/about')
def about_pagev2():
    return render_template('v2/about.html')

@app.route('/v2/photos')
def photos_pagev2():
    return render_template('v2/about.html')


@app.route('/about/')
def about_page():
    return render_template('about.html')


@app.route('/photos/')
def photos_page():
    return render_template('photos.html')


@app.route('/resume.pdf')
def show_resume_pdf():
    path = join(dirname(realpath(__file__)), 'static/resume.pdf')
    return send_file(path, attachment_filename='resume.pdf')

@app.route('/unclearballot.pdf')
def show_unclearballot_pdf():
    path = join(dirname(realpath(__file__)), 'static/unclearballot.pdf')
    return send_file(path, attachment_filename='unclearballot.pdf')

@app.route('/resume/')
def resume_page():
    path = join(dirname(realpath(__file__)), 'static/resume.pdf')
    return send_file(path, attachment_filename='resume.pdf')


if __name__ == "__main__":
    app.run()
