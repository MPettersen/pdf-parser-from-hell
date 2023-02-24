from parsers.utils import (
    remove_newlines
)
from parsers.common import (
    entry_not_empty,
    starts_with_number,
    get_first_sentence,
    is_text_capitalized
)


def split_list(txt: str, delim: str) -> list[str]:
    """Split a list from text."""
    temp = [remove_newlines(i).strip() for i in txt.split(delim)]
    return [i for i in temp if entry_not_empty(i)]


def parse_dot_list(txt: str, delim: str = '•') -> list[str | dict[str, str]]:
    """Parse dot lists from text."""
    temp = split_list(txt, delim)
    #temp.pop(0)
    return temp


def parse_meta_list(txt: str, delim: str) -> dict[str, str]:
    """Parse meta lists from text."""
    temp = split_list(txt, delim)
    return {temp[0].strip(): temp[1].strip()}


def is_meta_list(txt: str, delim: str) -> bool:
    """Check if a list is a meta list."""
    return txt.count(delim) > 0


def line_start_with_number_dot(txt: str) -> bool:
    """Check if a line starts with a number and a dot."""
    temp = split_list(txt, "\n")
    return sum([
        starts_with_number(line)
        for line in temp if entry_not_empty(line)
    ]) > 0


def parse_number_list(txt: str) -> list[str]:
    """Parse number lists from text."""
    temp = split_list(txt, "\n")
    start_with_number = [
        starts_with_number(line)
        for line in temp if entry_not_empty(line)
    ]
    buffer = ""
    l = list()
    for t, b in zip(temp, start_with_number):
        if b:
            if entry_not_empty(buffer):
                l.append(buffer)
            buffer = t
        else:
            buffer += f" {t}"
    if entry_not_empty(buffer):
        l.append(buffer)
    return l


def is_single_word_sentence(txt: str) -> bool:
    """Check if a sentence is a single word sentence."""
    if txt is None:
        return False
    temp = txt.split(" ")
    return len(temp) == 1 and is_text_capitalized(temp[0])


def line_starts_with_single_word_sentence(txt: str) -> bool:
    """Check if a line starts with a single word sentence."""
    return is_single_word_sentence(get_first_sentence(txt))


def parse_single_word_sentence_list(txt: str) -> str:
    """Parse single word sentences from text."""
    temp = split_list(txt, "\n")
    starts_with_single_word = [
        line_starts_with_single_word_sentence(line)
        for line in temp if entry_not_empty(line)
    ]
    buffer = ""
    l = dict()
    key = ""
    for t, b in zip(temp, starts_with_single_word):
        if b:
            if entry_not_empty(buffer):
                l[key] = buffer
            t1 = t.split(".")
            key = t1[0]
            buffer = '. '.join(t1[1:]).strip()
        else:
            buffer += f" {t}"
    else:
        if entry_not_empty(buffer):
            l[key] = buffer
    return l
