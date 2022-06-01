from flask import Flask, render_template, request, redirect, url_for



from search import twt,get_input
from util import process,predict

# uname=""
# rname=""
# age=""
# fr_count=""
# fo_count=""

def requestResults(name):
    data=twt(name)
    data=process(data)
    pred=predict(data)

    return pred

def format_pred(name):
    pred=requestResults(name)
    if pred==1:
        return "Real"
    else:
        return "Fake"


app = Flask(__name__)

# render default webpage
@app.route('/')
def home():
    return render_template('home.html')

# when the post method detect, then redirect to success function
@app.route('/', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        user = request.form['search']
        return redirect(url_for('success', name=user))


# get the data for the requested query
@app.route('/success/<name>')

# @app.route('/success/<name>', methods=['POST', 'GET'])
def success(name):
    if request.method=='GET':
        [uname,rname,age,fr_count,fo_count]=get_input(name)
        return render_template('pred.html',uname=uname,pred=(format_pred(name)),rname=rname,age=age,fr_count=fr_count,fo_count=fo_count) 
    # elif request.method=='POST':
    #     return redirect('/')

app.run(debug=True)