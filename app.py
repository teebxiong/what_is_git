from flask import Flask, render_template
import data

app = Flask(__name__)

@app.route('/')
def index():
    message = data.get_message()
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
