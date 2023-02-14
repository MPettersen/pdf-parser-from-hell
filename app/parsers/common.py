def entry_not_empty(entry: str) -> bool:
    """Check if an entry is not empty."""
    return len(entry) > 0


def remove_empty_entries(entries: list[str]) -> list[str]:
    """Remove empty entries from a list."""
    return [i for i in entries if entry_not_empty(i)]


def starts_with_number(txt: str) -> bool:
    """Check if a line starts with a number."""
    return txt[0].isdigit() and txt[1] == '.'


def get_first_sentence(txt: str) -> str:
    """Get the first sentence from text."""
    line = remove_empty_entries(txt.split("."))
    return line[0] if len(line) > 1 else None


def is_text_capitalized(txt: str) -> bool:
    """Check if a text is capitalized."""
    return txt[0].isupper()
