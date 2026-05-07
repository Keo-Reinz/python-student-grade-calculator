import pytest
from grade_calculator import calculate_grade


# -------------------------------
# Valid grade boundary tests
# -------------------------------

def test_fail_grade():
    assert calculate_grade(49) == "Fail"


def test_pass_grade():
    assert calculate_grade(50) == "Pass"


def test_credit_grade():
    assert calculate_grade(60) == "Credit"


def test_distinction_grade():
    assert calculate_grade(70) == "Distinction"


def test_high_distinction_grade():
    assert calculate_grade(80) == "High Distinction"


# -------------------------------
# Invalid score tests
# -------------------------------

def test_score_below_zero():
    with pytest.raises(ValueError):
        calculate_grade(-1)


def test_score_above_100():
    with pytest.raises(ValueError):
        calculate_grade(101)


# -------------------------------
# Intentional failing test for CI/CD evidence
# -------------------------------

def test_intentional_failure_for_pipeline_evidence():
    assert calculate_grade(75) == "Credit"