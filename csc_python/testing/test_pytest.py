import itertools


def rle(iterable):
    """Applies run-length encoding to an iterable.
    >>> list(rle(""))
    []
    >>> list(rle("mississippi"))
    ... # doctest: +NORMALIZE_WHITESPACE
    [('m', 1), ('i', 1), ('s', 2), ('i', 1),
     ('s', 2), ('i', 1), ('p', 2), ('i', 1)]    
    """
    for item, g in itertools.groupby(iterable):
        yield item, sum(1 for _ in g)


def test_rle():
    assert rle("mississippi") == [
        ('m', 1), ('i', 1), ('s', 2), ('i', 1),
        ('s', 2), ('i', 1), ('p', 2), ('i', 1)
    ]
    
def test_rle_empty():
    assert not list(rle(""))