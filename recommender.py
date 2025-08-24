import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
jobs_df = pd.read_csv("data/cleaned_jobs.csv")


# Simple synonyms dictionary
synonyms = {
    "carpenter": ["carpentry", "woodworking", "carpenter assistant"],
    "plumber": ["plumbing", "pipe fitting", "water repair"],
    "electrician": ["electrical", "wiring", "electrical repair"],
    "driver": ["driving", "chauffeur", "vehicle operator"],
    "tailor": ["sewing", "stitching", "fabric cutting", "dressmaking"],
    "data entry": ["typing", "excel", "ms office", "clerical work"]
}

def expand_skills(user_input):
    words = [w.strip().lower() for w in user_input.split(",")]
    expanded = []
    for word in words:
        expanded.append(word)
        for key, values in synonyms.items():
            if word in key or word in values:
                expanded.extend(values)
    return " ".join(set(expanded))  

def get_recommendations(user_skills, location=None, top_n=5):
  
    user_skills_expanded = expand_skills(user_skills)

    vectorizer = TfidfVectorizer(stop_words="english")
    job_skill_matrix = vectorizer.fit_transform(jobs_df["skills"].astype(str))
    user_vector = vectorizer.transform([user_skills_expanded])

    similarity_scores = cosine_similarity(user_vector, job_skill_matrix).flatten()
    jobs_df["match_score"] = (similarity_scores * 100).round(2)

    # Filter by location 
    filtered_jobs = jobs_df.copy()
    if location and location.strip():
        filtered_jobs = filtered_jobs[filtered_jobs["location"].str.contains(location, case=False, na=False)]

    recommended = filtered_jobs.sort_values(by="match_score", ascending=False).head(top_n)
    return recommended[["title", "company", "location", "salary", "match_score"]]
