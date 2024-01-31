from flask import Flask, render_template, request
from read_csv import read_fruits

app = Flask(__name__)

@app.route('/')
def home():
    fruits = read_fruits()
    return render_template('integrate.html', fruits=fruits)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')


    with open('contacts.txt', 'a') as file:
        file.write(f"Name: {name}, Email: {email}, Message: {message}\n")
    
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)