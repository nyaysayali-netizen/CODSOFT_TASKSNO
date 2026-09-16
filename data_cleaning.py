import pandas as pd

df = pd.read_csv("students.csv")

print("Original Data:")
print(df)


print("\nMissing Values:")
print(df.isnull().sum())


df = df.drop_duplicates()


df["Age"] = df["Age"].fillna(df["Age"].mean())


df["Marks"] = df["Marks"].fillna(df["Marks"].mean())


df["City"] = df["City"].str.title()

print("\nCleaned Data:")
print(df)


df.to_csv("cleaned_students.csv", index=False)

print("\nCleaned data saved successfully!")
df.to_csv("cleaned_dataset.csv", index=False)

print("Cleaned dataset saved as cleaned_dataset.csv")