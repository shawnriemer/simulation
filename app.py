from flask import Flask, render_template, request
from modules.graphs import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    fig_html = blackjack_sim()
    return render_template('index.html', graph=fig_html)

@app.route('/sim', methods=['GET', 'POST'])
def sim():
    graph_none = roulette_none()
    graph_martingale = roulette_martingale()
    return render_template(
        'sim.html',
        graph_none=graph_none,
        graph_martingale=graph_martingale
    )

if __name__ == '__main__':  
   app.run(host="0.0.0.0", debug=True)
