from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/greetings/')
@app.route('/greetings/<season>')
def greetings(season=None):
    if season == 'christmas':
        message = 'Merry Christmas!'
    elif season == 'newyear':
        message = 'Happy New Year!'
    else:
        message = 'Seasons Greetings!'

    return message

if __name__ == '__main__':
    app.run(debug=True)



