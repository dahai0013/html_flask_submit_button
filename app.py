from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/send', methods=['GET','POST'])
def send():
    if request.method == 'POST':
        age = request.form['age']

        return render_template('age.html', age=age)

    return render_template('index.html')

if __name__ == "__name__":
    app.run()