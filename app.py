from flask import Flask, render_template, send_file
from os.path import join, dirname, realpath
app = Flask(__name__)

app.debug = True


@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/about/')
def about_page():
    return render_template('about.html')


@app.route('/work/')
def work_page():
    return render_template('work.html')


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
