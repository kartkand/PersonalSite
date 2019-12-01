from flask import Flask, render_template
import os
app = Flask(__name__)



if __name__ == "__main__":
    for filename in os.listdir('templates'):
        if filename.endswith(".html"):
            with app.app_context():
                rendered_page = render_template(filename).encode('utf-8')
                fh = open(filename, "wb")
                fh.write(rendered_page)
                fh.close()
