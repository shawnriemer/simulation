from flask import Flask, render_template, request
# import numpy as np
# import pandas as pd
# import plotly.express as px
# import random
from modules.graphs import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    fig_html = blackjack_sim()
    fig_html2 = make_different_plot()
    return render_template('index.html', graph=fig_html, graph2=fig_html2)

# def bruh():
#     if request.method == 'POST':
#         try:
#             bet = int(request.form.get("betSize"))
#         except ValueError:
#             bet = 5
#     else:
#         bet = 5
#
#     n = 1
#     cash = 100
#     win_prob = .38
#     bjack_prob = .04
#     draw_prob = .08
#     rounds = n
#     lose_prob = 1 - win_prob - bjack_prob - draw_prob
#     cashflow_list = []
#
#     for i in range(n):
#         cash = 100
#         cashflow = [cash]
#         while cash >= bet:
#             cash += random.choices([bet, 1.5 * bet, 0, -1 * bet], weights=[win_prob, bjack_prob, draw_prob, lose_prob])[
#                 0]
#             cashflow.append(cash)
#         cashflow_list.append(cashflow)
#
#     dfi = pd.DataFrame(cashflow_list)
#     dfi = dfi.transpose().reset_index()
#
#     y = [int(x) for x in np.arange(0, n)]
#     fig = px.line(dfi, x='index', y=y)#, width=1000, height=600)
#     fig = fig.update_layout(showlegend=False)
#     fig_html = fig.to_html(full_html=False)
#     return fig_html


if __name__ == '__main__':  
   app.run(host="0.0.0.0", debug=True)