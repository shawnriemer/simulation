from flask import Flask, render_template, request
from modules.graphs import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    fig_html = blackjack_sim()
    # fig_html2 = make_different_plot()
    return render_template('index.html', graph=fig_html)#, graph2=fig_html2)



if __name__ == '__main__':  
   app.run(host="0.0.0.0", debug=True)