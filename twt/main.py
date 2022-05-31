from flask import Flask, render_template, request, redirect, url_for



from search import twt
from util import process,predict,get_input


def requestResults(name):
    data=twt(name)
    data=process(data)
    pred=predict(data)

    return pred

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
def success(name):
    return "<xmp>" + str(requestResults(name)) + " </xmp> "

app.run(debug=True)