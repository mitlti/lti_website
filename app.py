import os
# import sys

# Append all packages in ./lib to path
cur_dir = os.path.dirname(os.path.abspath(__file__))
main_dir = os.path.dirname(cur_dir)
# lib_dir = os.path.join(main_dir, 'lib')
# for pkg in os.listdir(lib_dir):
#     sys.path.insert(0, os.path.join(lib_dir, pkg))

from flask import Flask
from flask import render_template

app = Flask(__name__, static_folder='assets', static_url_path='/assets')
app.config.update(
    DEBUG=True,
)

##### Import bios
import csv
from collections import namedtuple

def read_bios():
    mapping = {
        "Athena": "athena",
        "Timestamp": "timestamp",
        "First Name": "first",
        "Last Name": "last",
        "Executive Position": "position",
        "Course": "course",
        "Year": "year",
        "Activities": "activities",
        "Short (Max. 200 word) biography about yourself.": "bio",
        "WIll you email Phu a picture of yourself?": "phu",
        "Interests": "interests",
        "Hometown": "hometown",
        "Why did you join LTI?": "why"
    }

    bio_fields = ['athena', 'first', 'last', 'position', 'bio']
    Bio = namedtuple('Bio', bio_fields)

    bios = []
    with open('lti-bios.csv') as bios_csv:
        bios_reader = csv.DictReader(bios_csv)
        for bio_row in bios_reader:
            fields = {}
            for k, v in bio_row.iteritems():
                if k is not None and mapping[k] in bio_fields:
                    fields[mapping[k]] = unicode(v)
            bio = Bio(**fields)
            bios.append(bio)
        return bios

bios = read_bios()
#####



@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/people')
def people():
    return render_template('people.html', bios=bios)

@app.route('/join')
def join():
    return render_template('join.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/for_students')
def for_students():
    return render_template('for_students.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/donate')
def donate():
    return render_template('donate.html')


if __name__ == "__main__":
    app.debug = True
    app.run()
