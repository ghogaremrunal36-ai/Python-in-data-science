from datetime import datetime

today = datetime.now()

print("a. YYYY-MM-DD :", today.strftime("%Y-%m-%d"))
print("b. DD-MM-YYYY :", today.strftime("%d-%m-%Y"))
print("c. Month Day, Year :", today.strftime("%B %d, %Y"))
print("d. Weekday, Month Day, Year :", today.strftime("%A, %B %d, %Y"))
