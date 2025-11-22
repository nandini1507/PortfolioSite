from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    return f"Thanks {name}, your message has been received!"

if __name__ == '__main__':
    print("Flask app is starting...")
    app.run(debug=True)
