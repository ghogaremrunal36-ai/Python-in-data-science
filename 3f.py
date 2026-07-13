from datetime import datetime

date1 = datetime(2026, 7, 10)
date2 = datetime(2026, 7, 15)

if date1 > date2:
    print("Date1 is later than Date2")
elif date1 < date2:
    print("Date1 is earlier than Date2")
else:
    print("Both dates are the same")
