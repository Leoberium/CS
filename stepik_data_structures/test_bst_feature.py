from bst_feature import check_feature


def test_traversals():
    assert check_feature([]) == "CORRECT"
    assert check_feature([
        (2, 1, 2),
        (1, -1, -1),
        (3, -1, -1)
    ]) == "CORRECT"
    assert check_feature([
        (1, 1, 2),
        (2, -1, -1),
        (3, -1, -1)
    ]) == "INCORRECT"
    assert check_feature([
        (1, -1, 1),
        (2, -1, 2),
        (3, -1, 3),
        (4, -1, 4),
        (5, -1, -1)
    ]) == "CORRECT"
    assert check_feature([
        (4, 1, 2),
        (2, 3, 4),
        (6, 5, 6),
        (1, -1, -1),
        (3, -1, -1),
        (5, -1, -1),
        (7, -1, -1)
    ]) == "CORRECT"
    assert check_feature([
        (4, 1, -1),
        (2, 2, 3),
        (1, -1, -1),
        (5, -1, -1)
    ]) == "INCORRECT"
