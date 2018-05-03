from flask import Flask, render_template, send_file
from os.path import join, dirname, realpath
app = Flask(__name__)


@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/contact/')
def contact_page():
    return render_template('contact.html')


@app.route('/about/')
def about_page():
    return render_template('about.html')


@app.route('/photos/')
def photos_page():
    return render_template('photos.html')


@app.route('/resume.pdf')
def show_static_pdf():
    path = join(dirname(realpath(__file__)), 'static/resume.pdf')
    return send_file(path, attachment_filename='resume.pdf')


if __name__ == "__main__":
    app.run()
