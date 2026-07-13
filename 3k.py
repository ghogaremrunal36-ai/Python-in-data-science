from datetime import datetime

today = datetime.now()

print("Month Number:", today.month)
print("Month Name:", today.strftime("%B"))
