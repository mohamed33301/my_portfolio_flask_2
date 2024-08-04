import os
from flask import Flask, render_template, request
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'))

def send_email(first_name, last_name, email, phone, subject, message):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_user = 'mohame3330@gmail.com'
    smtp_password = 'mnru lklq kwvi eupy'

    to_email = 'mohame3330@gmail.com'
    email_subject = f'Contact Form: {subject}'
    email_body = f"""
    First Name: {first_name}
    Last Name: {last_name}
    Email: {email}
    Phone: {phone}

    Message:
    {message}
    """

    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = to_email
    msg['Subject'] = email_subject
    msg.attach(MIMEText(email_body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.send_message(msg)
        server.quit()
        return "Message sent successfully!"
    except Exception as e:
        return f"Failed to send message. Error: {str(e)}"

@app.route('/')
@app.route("/index.html")
def index():
    return render_template('index.html')

@app.route("/about.html")
def about():
    return render_template('about.html')
@app.route('/contact.html', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone = request.form['phone']
        subject = request.form['subject']
        message = request.form['message']
        result = send_email(first_name, last_name, email, phone, subject, message)

        if "Message sent successfully!" in result:
            message_type = 'success'
            icon = 'fa-check'
            bg_color = '#d4edda'  # Light green background
            text_color = '#155724' # Dark green text
        else:
            message_type = 'error'
            icon = 'fa-times'
            bg_color = '#f8d7da'  # Light red background
            text_color = '#721c24' # Dark red text

        return f"""
        <html>
        <head>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css"
                integrity="sha512-Fo3rlrZj/k7ujTnHg4CGR2D7kSs0v4LLanw2qksYuRlEzO+tcaEPQogQ0KaoGN26/zrn20ImR1DfuLWnOo7aBA=="
                crossorigin="anonymous" referrerpolicy="no-referrer" />
        </head>
        <body>
            <div style="display: flex; align-items: center; justify-content: center; height: 100vh;">
                <div style="padding: 20px; border-radius: 5px; background-color: {bg_color}; color: {text_color}; text-align: center;">
                    <i class="fa {icon}" style="font-size: 24px; margin-right: 10px;"></i>
                    {result}
                </div>
            </div>
            <script>
                setTimeout(function() {{
                    window.location.href = '/contact.html';
                }}, 2000);
            </script>
        </body>
        </html>
        """

    return render_template('contact.html')


@app.route("/project.html")
def project():
    return render_template('project.html')

@app.route("/resume.html")
def resume():
    return render_template('resume.html')

@app.route("/services.html")
def services():
    return render_template('services.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
