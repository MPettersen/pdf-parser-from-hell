def collaps_paragraph(s):
    return ' '.join(s.splitlines()).strip()


def add(c, id, **kwargs):
    c(parent_id=id, **kwargs)
