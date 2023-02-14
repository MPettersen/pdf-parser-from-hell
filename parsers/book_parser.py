import pandas as pd

from io import StringIO
from uuid import UUID

from utils import (
    remove_newlines
)
from models import (
    Book,
    Chapter,
    ParagraphsMetadata,
    List,
    Table
)
from parsers.list import (
    parse_dot_list,
    line_start_with_number_dot,
    parse_number_list,
    line_starts_with_single_word_sentence,
    parse_single_word_sentence_list,
    split_list,
    is_meta_list,
    parse_meta_list
)


def parse_paragraphs(txt: str) -> list[str | dict[str, str]]:
    """Parse paragraphs from text."""
    return [remove_newlines(i) for i in txt.strip().split("\n\n")]


def parse_list(txt: str) -> list[str | dict[str, str]]:
    """Parse lists from text."""
    dot_delim = '•'
    newline_delim = "\n\n"
    if txt.count(dot_delim) > 1:
        return parse_dot_list(txt, dot_delim)
    elif line_start_with_number_dot(txt):
        return parse_number_list(txt)
    elif line_starts_with_single_word_sentence(txt):
        return parse_single_word_sentence_list(txt)
    elif txt.count(newline_delim) > 0:
        temp = split_list(txt, newline_delim)
        delim = ":"
        if all(is_meta_list(i, delim) for i in temp):
            return [parse_meta_list(i, delim) for i in temp]
        else:
            return temp


def parse_table(txt: str, sep: str = "|", **kwargs) -> list[list[str]]:
    """Parse tables from text."""
    return pd.read_csv(StringIO(txt), sep=sep, **kwargs)
