"""
datetime is used to get the current year
"""
import datetime
name = str(input("Enter your name: "))

age= int(input("Enter your age: "))


def calculateYear(age):
    """
    This function calculates the year when the person will turn 100 years old
    """
    diff= 100 - age
    result = datetime.date.today().year + diff
    return result



while type(age) == int and type(name) == str:
    year = calculateYear(age)
    print(year)
    break

else:
    print("Please enter a valid type")
