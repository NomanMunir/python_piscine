
def ft_tqdm(lst) -> None:
    """Decorate an iterable object, returning an iterator which acts exactly
like the original iterable, but prints a dynamically updating
progressbar every time a value is requested.
"""
    total = len(lst)
    for i, elem in enumerate(lst, 1):
        percent = int((i / total) * 100)
        bar_len = 104
        filled = int(bar_len * i / total)
        bar = '=' * filled + '>' + ' ' * (bar_len - filled - 1)
        print(f"\r{percent:3}%|{bar}| {i}/{total}", end="")
        yield elem
    print()
