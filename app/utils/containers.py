import os
import sys
import dash_bootstrap_components as dbc

from dash import Dash, html, dcc, Input, Output

from utils.helpers import (
    remove_file_ext,
    get_books
)

breadcrumb_nav_bar = dbc.Breadcrumb(
    items=[
        {
            "label": "Books",
            "href": "/Books",
            "external_link": True,
            "active": True
        }
    ]
)

add_new_book = dbc.Row(
    dbc.Col(
        dbc.InputGroup(
            [
                dbc.InputGroupText("Title"),
                dbc.Input(placeholder="Enter book title here...", id="input-new-book"),
                dbc.Button("Add new book", id="input-new-book-button")
            ],
            className="mb-3",
        ),
        width=6
    )
)

select_book = dbc.Form(
    dbc.Row(
        [
            dbc.Col(
                get_books(),
                width=2,
                id="book-list"
            ),
            dbc.Col(
                dbc.Button("Select book", id="input-select-book-button"),
            )
        ]
    )
)
