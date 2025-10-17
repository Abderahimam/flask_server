from flask import Flask, render_template, request

app = Flask(_name_)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    return f"""
        <h2>Thank you, {name}!</h2>
        <p>Your message has been received.</p>
        <p><strong>Email:</strong> {email}</p>
        <p><strong>Message:</strong> {message}</p>
        <br><a href='/'>Go back</a>
    """

if _name_ == '_main_':
    app.run(debug=True)
