def calculate_bmi(weight, height):
    # Calculate BMI
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    # Determine the BMI category based on the BMI value
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("Welcome to the BMI Calculator!")
    
    # Get user input
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        
        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)
        
        # Display the result
        print(f"Your BMI is: {bmi:.2f}")
        print(f"BMI Category: {category}")
    except ValueError:
        print("Invalid input. Please enter numerical values for weight and height.")

# Run the BMI Calculator
main()
