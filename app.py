from  flask import Flask, render_template, request, json
app=Flask(__name__)
@app.route("/")
def main():
    return render_template('login.html')
if __name__=="__main__":
    app.run(debug=True)

@app.route('/signup',methods=['POST'])
def signUp():
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
    if _name and _email and _password:
        return json.dumps({'html': '<span>All fields good !!</span>'})
    else:
        return json.dumps({'html': '<span>enter required firlds !!</span>'})
