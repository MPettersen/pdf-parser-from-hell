import os
import os.path
import markdown

from joblib import load, dump
import dash_bootstrap_components as dbc


def openfile(filename: str):
    filepath = os.path.join("app/pages/", filename)
    with open(filepath, "r", encoding="utf-8") as input_file:
        text = input_file.read()
    
    html = markdown.markdown(text)
    data = {
        "text": html
    }
    return data


def remove_file_extensions(files: list[str]):
    return [remove_file_ext(file) for file in files]


def remove_file_ext(filename: str):
    return ''.join(filename.split('.')[:-1])


def load_book(title: str, folder: str):
    return load(f"{folder}/{title}.joblib")


def save_book(book, folder: str):
    dump(book, f"{folder}/{book.title}.joblib")


def get_books():
    return dbc.RadioItems(
        options=[
            {
                "label": remove_file_ext(book),
                "value": remove_file_ext(book)
            }
            for book in os.listdir("books")
        ],
        value=1,
        id="input-select-book"
    )
