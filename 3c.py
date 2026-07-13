from datetime import datetime


now = datetime.now()

print("DD-MM-YYYY :", now.strftime("%d-%m-%Y"))
print("MM/DD/YYYY :", now.strftime("%m/%d/%Y"))
print("YYYY-MM-DD :", now.strftime("%Y-%m-%d"))
print("Day, Month Date, Year :", now.strftime("%A, %B %d, %Y"))
