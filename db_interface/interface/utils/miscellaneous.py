


def merge(a, b, path=None):
    """merges nested dictionary b into dictionary a.
    b has priority into the hierarchy
    A represent the stored data, while B represents the data updated pulled from
    the html form."""
    if path is None: path = []
    for key in b:
        if key in a:
            if isinstance(a[key], dict) and isinstance(b[key], dict):
                merge(a[key], b[key], path + [str(key)])
            elif a[key] == b[key]:
                pass # same leaf value
            else:
                a[key] = b[key]  # force to update the value in a from value in b
        else:
            a[key] = b[key]
    return a