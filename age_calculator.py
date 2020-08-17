from datetime import datetime

def check_birthdate(year, month, day):
    today=datetime.now()
    Date=datetime(year, month, day)
    return Date<today
def calculate_age(year, month, day):
    Date=datetime(year, month, day)
    age=datetime.now() - Date
    print ("you are %s years old" % (age.days/365))


def main():
    year=int(input("Enter year of birth: "))
    month=int(input("Enter month of birth: "))
    day=int(input("Enter day of birth: "))

    if check_birthdate(year, month, day):
      calculate_age(year, month, day)
    else:
      print("invalid date")


if __name__ == '__main__':
	main()
