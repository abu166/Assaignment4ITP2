from flask import Flask, render_template
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

if __name__ == '__main__':
    app.run(debug=True)