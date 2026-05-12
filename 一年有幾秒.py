def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def seconds_in_year(year):
    days = 366 if is_leap_year(year) else 365
    return days * 24 * 3600

# 測試
year = int(input("Enter a year: "))
print(f"There are {seconds_in_year(year)} seconds in {year}.")