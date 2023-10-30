from app import process_query


def test_knows_about_dinosaurs():
    assert (
        process_query("dinosaurs") == "Dinosaurs ruled the Earth 200 million years ago"
    )


def test_does_not_know_about_asteroids():
    assert process_query("asteroids") == "Unknown"


def test_knows_name():
    assert process_query("What is your name?") == "james_ankur"


def test_sum():
    query = "What is 42 plus 76?"
    expected = str(118)
    assert process_query(query) == expected


def test_largest():
    query = "Which of the following numbers is the largest: 53, 1, 35"
    expected = str(53)
    assert process_query(query) == expected


def test_sq_cube():
    query = "Which of the following numbers is both a square and a cube: 216, \
    891, 256, 2201, 1285, 4395, 4096?"
    expected = str(4096)
    assert process_query(query) == expected

def test_minus():
    query = "What is 60 minus 30?"
    expected = str(30)
    assert process_query(query) == expected