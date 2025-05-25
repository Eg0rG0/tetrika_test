import pytest

from task3.solution import appearance

tetrika_tests = [
    {
        "intervals": {
            "lesson": [1594663200, 1594666800],
            "pupil": [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
            "tutor": [1594663290, 1594663430, 1594663443, 1594666473]
        },
        "answer": 3117
    },
    {
        "intervals": {
            "lesson": [1594702800, 1594706400],
            "pupil": [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150,
                      1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480,
                      1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
                      1594706524, 1594706524, 1594706579, 1594706641],
            "tutor": [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]
        },
        "answer": 3577
    },
    {
        "intervals": {
            "lesson": [1594692000, 1594695600],
            "pupil": [1594692033, 1594696347],
            "tutor": [1594692017, 1594692066, 1594692068, 1594696341]
        },
        "answer": 3565
    }
]

my_tests = [
    {
        "intervals": {
            "lesson": [100, 200],
            "pupil": [100, 200],
            "tutor": [100, 200]
        },
        "answer": 100
    },
    {
        "intervals": {
            "lesson": [100, 200],
            "pupil": [150, 180],
            "tutor": [160, 190]
        },
        "answer": 20
    },
    {
        "intervals": {
            "lesson": [100, 200],
            "pupil": [50, 70, 210, 220],
            "tutor": [100, 200]
        },
        "answer": 0
    },
    {
        "intervals": {
            "lesson": [100, 200],
            "pupil": [100, 150, 160, 200],
            "tutor": [100, 120, 180, 200]
        },
        "answer": 40
    },
    {
        "intervals": {
            "lesson": [100, 200],
            "pupil": [110, 190],
            "tutor": [90, 105, 195, 210]
        },
        "answer": 0
    },
    {
        "intervals": {
            "lesson": [100, 200],
            "pupil": [120, 160],
            "tutor": [110, 130, 150, 170]
        },
        "answer": 20
    }
]


@pytest.mark.parametrize("test_case", tetrika_tests)
def test_provided_cases(test_case):
    assert appearance(test_case["intervals"]) == test_case["answer"]


@pytest.mark.parametrize("test_case", my_tests)
def test_my_cases(test_case):
    assert appearance(test_case["intervals"]) == test_case["answer"]
