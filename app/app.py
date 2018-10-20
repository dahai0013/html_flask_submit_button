from flask import Flask, render_template, request
app = Flask(__name__)

#browsing http:127.0.0.1 will senbd back index.html
@app.route('/', methods=['GET', 'POST'])
def index():
    # index.html must be under ./templates dir
    return render_template('index.html')

#when the html page send the GET IP@/send, if will be capture by this one
@app.route('/send', methods=['GET','POST'])
def send():
    if request.method == 'POST':
        age = request.form['age']
        return render_template('age.html', age=var)

    return render_template('index.html')


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
    #app.run(debug=True,port=8080)