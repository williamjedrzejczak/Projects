"""Password Generator

Author: William Jedrzejczak.

Version: 11/04/2023
"""


def finals_calculator():
    try:
        current_grade = float(input("Enter your current grade in the class: "))
        target_grade = float(input("Enter your target grade for the class: "))
        final_weight = float(input("Enter the weight of the final exam (in percentage): "))

        # Ensure the final weight is a valid percentage
        if final_weight < 0 or final_weight > 100:
            raise ValueError("Final weight must be between 0 and 100.")

        # Calculate the required final exam score
        required_final_score = (target_grade - (1 - final_weight / 100) * current_grade) / (final_weight / 100)

        print(f"You need to score at least {required_final_score:.2f}% on the final exam to get a {target_grade}% in the class.")

    except ValueError as e:
        print(f"Error: {e}. Please enter valid numerical values.")

# Run the finals calculator
finals_calculator()