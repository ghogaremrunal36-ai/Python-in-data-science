subject = ("Python for Data Science", 301)

try:
    subject[1] = 999 
except TypeError as e:
    print("Tuple is immutable! Error:", e)
