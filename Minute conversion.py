Input2 = input("what would you like to convert 1. minutes 2. hours ")

if Input2.__contains__("minutes"):
    Input1 = input("How many minutes would you like to convert into seconds ")
    Minutes = Input1
    MinutesCalculation = float(Minutes) * 60
    print(str(MinutesCalculation) + " seconds!")
else:
    Input = input("How many Hours would you like to convert into seconds ")
    Hours = Input
    # calculate Minutes and hours to seconds
    HoursCalculation = float(Hours) * 60 * 60
    print(str(HoursCalculation) + " seconds!")
