from flask import Flask, render_template

app = Flask(__name__, static_folder='assets', template_folder='.')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
