import tabulate
import csv




def chart():

    list2 = []

    with open("projekt1/BMI__calc/bmi.csv.csv") as file1:
        list1 = csv.reader(file1)
        for line in list1:
            list2.append(line)
        print("Reference chart:\n" + tabulate.tabulate(list2[1:], headers=list2[0], tablefmt="pretty"))







def calculate_bmi(height, weight):

    bmi = round(weight/(height**2), 2)

    return bmi









def interpret_bmi(bmi):

    if bmi < 18.5:
        return f"Your BMI is {bmi}, you are underweight."
    elif bmi < 24.9:
        return f"Your BMI is {bmi}, you are normal."
    elif bmi < 29.9:
        return f"Your BMI is {bmi}, you are overweight."
    elif bmi < 34.9:
        return f"Your BMI is {bmi}, you are obese (Class I)."
    elif bmi < 39.9:
        return f"Your BMI is {bmi}, you are obese (Class II)."
    elif bmi > 39.9:
        return f"Your BMI is {bmi}, you are obese (Class III)."




def main():

    chart()

    height = float(input("Enter your height in meters: "))
    weight = float(input(("Enter your weight in kilograms: ")))

    bmi = calculate_bmi(height, weight)
    result = interpret_bmi(bmi)

    print(result)

main()