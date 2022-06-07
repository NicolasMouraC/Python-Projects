from flask import Flask, render_template, request
import requests
from datetime import datetime
import smtplib

year = datetime.now().year

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    json_data = requests.get("https://api.npoint.io/e12e4b9d283d42ab8aaf").json()
    return render_template('index.html', blogs=json_data, year=year)

# About page
@app.route('/about.html')
def about():
    return render_template('about.html', year=year)

# Contact page with a form
@app.route('/contact.html', methods=['POST', 'GET'])
def contact():
    # If the method is a POST, it sends an email to your mail
    if request.method == "POST":
        message = f"Name: {request.form['name']}\n" \
                  f"Email: {request.form['email']}\n" \
                  f"Phone: {request.form['phone']}\n" \
                  f"Message: {request.form['name']}\n"

        # Sends an email using smtplib
        # with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connect:
        #     connect.starttls()
        #     connect.login(user={ EMAIL }, password={ EMAIL_PASSWORD })
        #     connect.sendmail(to_addrs={ EMAIL_TO_RECEIVE_THE_MESSAGE },
        #                      from_addr={ EMAIL_TO_SEND_THE_MESSAGE },
        #                      msg=message)

        # Changes the header to show the user that his form was registered
        return render_template('contact.html', year=year, sent=True)
    return render_template('contact.html', year=year, sent=False)

# Posts info page
@app.route('/post/<int:blog_num>')
def posts(blog_num):
    post = None
    json_data = requests.get("https://api.npoint.io/e12e4b9d283d42ab8aaf").json()

    for blog in json_data:
        if blog['id'] == blog_num:
            post = blog

    return render_template('post.html', blog=post, year=year)

if __name__ == "__main__":
    app.run(debug=True)
