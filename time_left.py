age = input("What is your current age?\n")

age_in_days = int(age) * 365
age_in_weeks = int(age) * 52
age_in_months = int(age) * 12

ninety_in_days = 90 * 365
ninety_in_weeks = 90 * 52
ninety_in_months = 90 * 12

days_left = ninety_in_days - age_in_days
weeks_left = ninety_in_weeks - age_in_weeks
months_left = ninety_in_months - age_in_months

print(f"You have {days_left} days, {weeks_left} weeks and {months_left} months left.")
