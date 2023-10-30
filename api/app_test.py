from app import process_query


def test_knows_about_dinosaurs():
    assert (
        process_query("dinosaurs")
        == "Dinosaurs ruled the Earth 200 million years ago"
    )


def test_does_not_know_about_asteroids():
    assert process_query("asteroids") == "Unknown"

def test_knows_name():
    assert process_query("What is your name?") == "james_ankur"

def test_largest_number():
    assert process_query("Which of the following numbers is the largest: {nums[0]}, {nums[1]}, {nums[2]}") == max(nums)
