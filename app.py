from flask import Flask, render_template, request
from modules.graphs import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    fig_html = blackjack_sim()
    return render_template('index.html', graph=fig_html)

@app.route('/sim', methods=['GET', 'POST'])
def sim():
    if request.method == "POST":
        n = int(request.form.get("none_n"))
        bet = int(request.form.get("none_bet"))
        start = int(request.form.get("none_start"))
    else:
        n=1
        bet=20
        start=100
    graph_none = roulette_none(n=n, bet=bet, start_cash=start)
    graph_martingale = roulette_martingale(n=n, start_bet=bet, start_cash=start)
    graph_grandmartingale = roulette_grandmartingale(n=n, start_bet=bet, start_cash=start)
    return render_template(
        'sim.html',
        graph_none=graph_none,
        graph_martingale=graph_martingale,
        graph_grandmartingale=graph_grandmartingale
    )

if __name__ == '__main__':  
   app.run(host="0.0.0.0", debug=True)
