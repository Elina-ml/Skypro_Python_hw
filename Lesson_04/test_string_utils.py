import string

import pytest
from string_utils import StringUtils


string_utils = StringUtils()

@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("homework", "Homework"),
        ("homework.", "Homework."),
        ("my homework.", "My homework."),
    ],
)
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.xfail
@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, expected",
    [
    ("PROF", "PROF"),
    ("😀", "😀"),
    ("", ""),
    ("_", "_")
    ],
)
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, expected",
    [
        (" homework", "homework"),
        (" Homework.", "Homework."),
        ("  Homework", "Homework"),
        (" my homework ", "my homework "),
        (" - My homework.", "- My homework."),
    ],
)
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, expected",
    [
    ("   ", ""),
    ("", ""),
    ("        ", ""),
    (".  sky.", ".  sky."),
    ],
)
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("SkyPro", "P", True),
        ("HomeWork", "Home", True),
        ("my homework", "my", True),
        ("SkyPro SkyPro SkyPro", "Pro", True),
    ],
)
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.xfail
@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("SkyPro", "pro", False),
        ("HomeWork", "", False),
        ("", "pro", False),
        ("  ", "", False),
        ("135", "13 5", False),
    ],
)
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("Homework", "H", "omework"),
        ("HomeWork", "Home", "Work"),
        ("my homework", "my", " homework"),
        ("1475 46", "4", "175 6"),
    ],
)
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("Homework", "Work", "Homework"),
        ("", "", ""),
        ("homework", "", "homework"),
        ("1698", "16 9", "1698"),
    ],
)
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected
