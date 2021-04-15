from flask import Flask 
from flask import render_template 

app = Flask(__name__)

@app.route('/mainpage/<name>/<surname>', methods=['GET', 'POST'])
def f1(name, surname):
    return render_template('temp1.html', nm=name, sn=surname)


if __name__ =="__main__":
    app.run(debug = True)