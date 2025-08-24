import pandas as pd

# Raw dataset
df = pd.read_csv("data/job.csv")

print("Original columns:", df.columns)

rename_map = {
    "Job Title": "title",
    "Company": "company",
    "location": "location",
    "Salary Range": "salary",
    "skills": "skills"
}

df = df[list(rename_map.keys())].rename(columns=rename_map)

df = df.fillna("")

df = df[(df["title"].str.strip() != "") & (df["skills"].str.strip() != "")]

if len(df) > 5000:
    df = df.sample(5000, random_state=42)

df.to_csv("data/cleaned_jobs.csv", index=False)

print("Cleaned dataset saved as data/cleaned_jobs.csv")
print("Total rows after cleaning:", len(df))
print(df.head())
