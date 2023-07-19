month = int(input())
year = int(input())

def is_leap(n):

    if n % 4 == 0:
        if n % 100 == 0:
            if n % 400 == 0:
                return True
            return False
        return True

is_leap(year)

days_in_month = 0
if month != 2:
  if month == 4 or month == 6 or month == 9 or month == 11:
      days_in_month = 30
  else:
      days_in_month = 31
else:
  if is_leap(year):
      days_in_month = 29
  elif not is_leap(year):
      days_in_month = 28

print(days_in_month)
