from flask import Flask , render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def ind():
    try: 
        session["count"] +=1
    except KeyError:
        session["count"]= 1
    return render_template("index.html", counter = session['count'])
@app.route("/inc", methods = ["POST"])
def inc():
    session["count"] +=1
    return redirect('/')
@app.route("/clear", methods = ["POST"])
def clear():
    session["count"] = 0
    return redirect('/')
app.run(debug= True)
    