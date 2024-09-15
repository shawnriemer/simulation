from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import plotly.express as px
import random

def update_fig(fig):
    pass

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
    lose_prob = 1 - win_prob - bjack_prob - draw_prob
    cashflow_list = []

    for i in range(n):
        cash = cash
        cashflow = [cash]
        while cash >= bet:
            cash += random.choices([bet, 1.5 * bet, 0, -1 * bet], weights=[win_prob, bjack_prob, draw_prob, lose_prob])[
                0]
            cashflow.append(cash)
        cashflow_list.append(cashflow)

    dfi = pd.DataFrame(cashflow_list)
    dfi = dfi.transpose().reset_index()

    print(len(cashflow_list[0])-1)
    tickmark_list = create_tickmarks(len(cashflow_list[0])-1)
    print(tickmark_list)

    y = [int(x) for x in np.arange(0, n)]
    fig = px.line(
        dfi,
        x='index',
        y=y,
        # height=1100,
        # width=500  # 983 makes my phone have scrollbar
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
        margin=dict(l=0, r=0, t=100, b=0),
        xaxis_tickfont_size=50,
        yaxis_tickfont_size=50,
        xaxis_range=[0, tickmark_list[-1]+1],
        xaxis_type='category',
        yaxis_rangemode='tozero',
        xaxis_title='Hands',
        xaxis_title_font_size=50,
        yaxis_title=None,
        xaxis_zeroline=True,
        yaxis_zeroline=False,
        yaxis_tickprefix='$ ',
        yaxis_ticksuffix=' ',
        xaxis_tickvals=tickmark_list,
        plot_bgcolor='rgb(0, 0, 0, 0)',
        paper_bgcolor='rgb(0, 0, 0, 0)',
        showlegend=False,
        title=f'Blackjack - ${bet} Bets',
        title_x=.5,
        title_font_size=50,
        font_color='white',
        font_family='Arial Black'
    )
    fig_html = fig.to_html(full_html=False, config={'displayModeBar': False})
    return fig_html


def create_tickmarks(n):
    # max of 7 xaxis tick marks, not including 0

    if n <= 6:
        counter = 1
    elif n <= 12:
        counter = 2
    elif n <= 30:
        counter = 5
    elif n <= 60:
        counter = 10
    elif n <= 90:
        counter = 15
    else:
        counter = 20

    ticks = list(np.arange(counter, n, counter))
    if n % counter == 0:
        ticks.append(n)
    if n % counter != 0:
        ticks.append(((n//counter)+1)*counter)

    return ticks


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
    fig_html = fig.to_html(full_html=False, config={'displayModeBar': False})
    return fig_html


def roulette_none():
    n = 1
    bet = 20
    cash = 100
    win_prob = .474
    lose_prob = 1 - win_prob
    cashflow_list = []

    for i in range(n):
        cash = 100
        cashflow = [cash]
        while cash >= bet:
            cash += random.choices([bet, -1 * bet], weights=[win_prob, lose_prob])[
                0]
            cashflow.append(cash)
        cashflow_list.append(cashflow)

    dfi = pd.DataFrame(cashflow_list)
    dfi = dfi.transpose().reset_index()

    print(len(cashflow_list[0]) - 1)
    tickmark_list = create_tickmarks(len(cashflow_list[0]) - 1)
    print(tickmark_list)

    y = [int(x) for x in np.arange(0, n)]
    fig = px.line(
        dfi,
        x='index',
        y=y,
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
        margin=dict(l=0, r=0, t=100, b=0),
        xaxis_tickfont_size=50,
        yaxis_tickfont_size=50,
        xaxis_range=[0, tickmark_list[-1] + 1],
        xaxis_type='category',
        yaxis_rangemode='tozero',
        xaxis_title='Hands',
        xaxis_title_font_size=50,
        yaxis_title=None,
        xaxis_zeroline=True,
        yaxis_zeroline=False,
        yaxis_tickprefix='$ ',
        yaxis_ticksuffix=' ',
        xaxis_tickvals=tickmark_list,
        plot_bgcolor='rgb(0, 0, 0, 0)',
        paper_bgcolor='rgb(0, 0, 0, 0)',
        showlegend=False,
        title=f'Roulette - ${bet} Bets',
        title_x=.5,
        title_font_size=50,
        font_color='white',
        font_family='Arial Black'
    )
    fig_html = fig.to_html(full_html=False, config={'displayModeBar': False})
    return fig_html

def roulette_martingale():
    n = 1
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
            else:
                bet = start_bet
            cashflow.append(cash)
        t = [x + 1 for x in range(len(cashflow))]
        cashflow_list.append(cashflow)

    dfi = pd.DataFrame(cashflow_list)
    dfi = dfi.transpose().reset_index()

    y = [int(x) for x in np.arange(0, n)]
    fig = px.line(
        dfi,
        x='index',
        y=y
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
        margin=dict(l=0, r=0, t=100, b=0),
        xaxis_tickfont_size=50,
        yaxis_tickfont_size=50,
        # xaxis_range=[0, tickmark_list[-1]+1],
        xaxis_type='category',
        yaxis_rangemode='tozero',
        xaxis_title='Hands',
        xaxis_title_font_size=50,
        yaxis_title=None,
        xaxis_zeroline=True,
        yaxis_zeroline=False,
        yaxis_tickprefix='$ ',
        yaxis_ticksuffix=' ',
        # xaxis_tickvals=tickmark_list,
        plot_bgcolor='rgb(0, 0, 0, 0)',
        paper_bgcolor='rgb(0, 0, 0, 0)',
        showlegend=False,
        title=f'Roulette - ${start_bet} Unit',
        title_x=.5,
        title_font_size=50,
        font_color='white',
        font_family='Arial Black'
    )
    fig_html = fig.to_html(full_html=False, config={'displayModeBar': False})
    return fig_html


