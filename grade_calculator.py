def calculate_grade(score):
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100.")

    if score < 50:
        return "Fail"
    elif score < 60:
        return "Pass"
    elif score < 70:
        return "Credit"
    elif score < 80:
        return "Distinction"
    else:
        return "High Distinction"


def main():
    score = float(input("Enter student score: "))
    grade = calculate_grade(score)
    print(f"Grade: {grade}")


if __name__ == "__main__":
    main()