from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/python_projects')
def python_projects():
    return render_template('python_projects.html')

@app.route('/discord_projects')
def discord_projects():
    return render_template('discord_projects.html')

@app.route('/html_projects')
def html_projects():
    return render_template('html_projects.html')

@app.route('/db_projects')
def db_projects():
    return render_template('db_projects.html')

@app.route('/about_me')
def about_me():
    return render_template('about_me.html')

if __name__ == '__main__':
    app.run(debug=True)
