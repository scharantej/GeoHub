
from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'your_email'
app.config['MAIL_PASSWORD'] = 'your_password'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solutions')
def solutions():
    return render_template('solutions.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/about-us')
def about_us():
    return render_template('about-us.html')

@app.route('/contact-us', methods=['GET', 'POST'])
def contact_us():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        msg = Message('Website Inquiry', sender='your_email', recipients=['your_email'])
        msg.body = f'Name: {name}\nEmail: {email}\nMessage: {message}'

        mail.send(msg)

        return render_template('contact-us.html', success=True)
    return render_template('contact-us.html')

if __name__ == '__main__':
    app.run(debug=True)
