from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def brivie_suni():
    return 'Brīvie Suņi'


@app.route('/macibas')
def macibas():
    return render_template('macibas.html')


@app.route('/parbaude')
def parbaude():
    return render_template('parbaude.html')


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
