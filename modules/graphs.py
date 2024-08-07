from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import plotly.express as px
import random

def blackjack_sim():
    if request.method == 'POST':
        try:
            bet = int(request.form.get("betSize"))
        except ValueError:
            bet = 20
    else:
        bet = 20
    n = 1
    cash = 100
    win_prob = .38
    bjack_prob = .04
    draw_prob = .08
    rounds = n
    lose_prob = 1 - win_prob - bjack_prob - draw_prob
    cashflow_list = []

    for i in range(n):
        cash = 100
        cashflow = [cash]
        while cash >= bet:
            cash += random.choices([bet, 1.5 * bet, 0, -1 * bet], weights=[win_prob, bjack_prob, draw_prob, lose_prob])[
                0]
            cashflow.append(cash)
        cashflow_list.append(cashflow)

    dfi = pd.DataFrame(cashflow_list)
    dfi = dfi.transpose().reset_index()

    y = [int(x) for x in np.arange(0, n)]
    fig = px.line(
        dfi,
        x='index',
        y=y,
        height=1000,
        width=1000
    )
    fig = fig.update_traces(
        line_color='#ff0000',
        line_width=6
    )
    fig = fig.update_layout(
        xaxis_fixedrange=True,
        yaxis_fixedrange=True,
        xaxis_griddash='dash',
        yaxis_griddash='dash',
        margin=dict(l=0, r=0, t=30, b=0),
        plot_bgcolor='rgb(0, 0, 0, 0)',
        paper_bgcolor='rgb(0, 0, 0, 0)',
        showlegend=False,
        title=f'${bet}',
        font_color='white',
        font_family='Arial Black'
    )
    fig_html = fig.to_html(full_html=False, config={'displayModeBar':False})
    return fig_html

def make_different_plot():
    n = 100
    start_cash = 100
    start_bet = 5
    win_prob = .47
    lose_prob = 1 - win_prob
    cashflow_list = []

    for i in range(n):
        cash = start_cash
        bet = start_bet
        cashflow = [cash]
        while cash - bet > 0:
            change = random.choices([bet, -1 * bet], weights=[win_prob, lose_prob])[0]
            cash += change
            if change < 0:
                bet *= 2
                bet += start_bet
            else:
                bet = start_bet
            cashflow.append(cash)
        t = [x + 1 for x in range(len(cashflow))]
        cashflow_list.append(cashflow)

    dfi = pd.DataFrame(cashflow_list)
    dfi = dfi.transpose().reset_index()

    y = [int(x) for x in np.arange(0, n)]
    fig = px.line(dfi, x='index', y=y, height=1000, width=1000)
    fig = fig.update_layout(
        xaxis_fixedrange=True,
        yaxis_fixedrange=True,
        xaxis_griddash='dash',
        yaxis_griddash='dash',
        margin=dict(l=0, r=0, t=30, b=0),
        plot_bgcolor='rgb(0, 0, 0, 0)',
        paper_bgcolor='rgb(0, 0, 0, 0)',
        showlegend=False,
        title=f'${bet}',
        font_color='white',
        font_family='Arial Black'
    )
    fig_html = fig.to_html(full_html=False, config={'displayModeBar':False})
    return fig_html
