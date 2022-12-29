import os
import sys
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

from joblib import dump, load
from dotenv import load_dotenv
from dash import Dash, html, dcc, Input, Output, State
from dash_utils.containers import (
    add_new_book,
    breadcrumb_nav_bar,
    select_book,
    get_books
)
from dash_utils.helpers import (
    get_books
)
from models import (
    Book
)

load_dotenv()

app = Dash(__name__, external_stylesheets=[dbc.themes.COSMO])

app.layout = dbc.Container(
    [
        dcc.Location(id='url'),
        breadcrumb_nav_bar,
        add_new_book,
        select_book
    ]
)

@app.callback(
    Output("book-list", "children"),
    Input("input-new-book-button", "n_clicks"),
    State("input-new-book", "value")
)
def add_book(n_clicks, title):
    if title is not None and title != '':
        book = Book(
            title=title,
            chapters=[]
        )
        dump(book, f"books/{title}.joblib")
    return get_books()


if __name__ == '__main__':
    app.run_server(debug=True)
