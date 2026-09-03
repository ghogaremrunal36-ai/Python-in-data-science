import pandas as pd


df = pd.read_csv("movie_ratings.csv")

print("Original Dataset:")
print(df)


print("\n1. Rating in Ascending Order:")
print(df.sort_values(by="Rating", ascending=True))


print("\n2. Rating in Descending Order:")
print(df.sort_values(by="Rating", ascending=False))


print("\n3. Votes in Descending Order:")
print(df.sort_values(by="Votes", ascending=False))

print("\n4. Top 5 Movies based on Rating:")
print(df.sort_values(by="Rating", ascending=False).head(5))


print("\n5. Bottom 3 Movies based on Rating:")
print(df.sort_values(by="Rating", ascending=True).head(3))
print("mrunal ghogare, S084")
