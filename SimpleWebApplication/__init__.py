from flask import Flask, render_template, request, redirect, url_for
from Forms import CreateUserForms

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contactUs')
def contact_us():
    return render_template('contactUs.html')

@app.route('/createUser', methods = ['GET', 'POST'])
def create_user():
    create_user_form = CreateUserForms(request.form)
    if request.method == 'POST' and create_user_form.validate():
        return redirect(url_for('home'))
    return render_template('createUser.html', for)

if __name__ == '__main__':
    app.run()