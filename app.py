from flask import Flask,render_template, request, redirect,url_for
from wtforms import Form,StringField
import os
import time

class params(Form):
    input = StringField('input')
    output = StringField('output')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def long_load():
    time.sleep(10) #just simulating the waiting period
    return "Your Tracking is in progress "

@app.route('/upload', methods=['POST'])
def upload():
    form = params(request.form)
    src=form.input.data
    print(src)
    if src == '':
        src='0'
        op=form.output.data
    else:
        op=src.split('.')
        op=op[0]+'.avi'
    
    if src == '0':
        call = "python object_tracker.py --video " + src + " --output ./data/video/output/" + op
    else:
        call = "python object_tracker.py --video ./data/video/input/" + src + " --output ./data/video/output/" + op 
    
    os.system(call)
    
    return redirect('/')
    

if __name__ == '__main__':
    app.run()

    

