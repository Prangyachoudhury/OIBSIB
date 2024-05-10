def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number.")

def calculate_bmi():
    # Get weight and height from user
    weight = get_float_input("Enter your weight in kilograms: ")
    height = get_float_input("Enter your height in meters: ")

    # Calculate BMI: weight (kg) / (height (m))^2
    bmi = weight / (height ** 2)

    # Classify based on BMI
    if bmi < 18.5:
        classification = 'Underweight'
    elif 18.5 <= bmi < 25:
        classification = 'Normal'
    elif 25 <= bmi < 30:
        classification = 'Overweight'
    else:
        classification = 'Obese'

    return bmi, classification

# Test the function
bmi, classification = calculate_bmi()

print(f'BMI: {bmi:.2f}')
print(f'Classification: {classification}')
