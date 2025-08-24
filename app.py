import streamlit as st
import pandas as pd
from recommender import get_recommendations

st.set_page_config(page_title="AI Job Recommendation", layout="wide")

st.title("AI Job Recommendation for Low-Income Workers")
st.write("Helping workers find suitable jobs using their skills – aligned with **SDG 1: No Poverty**.")


skills = st.text_area("Enter your skills (comma-separated):", placeholder="e.g., marketing, data entry, electrical repair")

location = st.text_input("📍 Preferred Location (optional):", placeholder="e.g., Havana")

if st.button("🔍 Find Jobs"):
    if skills.strip() == "":
        st.warning("Please enter at least one skill.")
    else:
        results = get_recommendations(skills, location)

        if results.empty:
            st.error("No matching jobs found. Try different skills.")
        else:
            st.success(f"Found {len(results)} matching jobs!")
            for _, row in results.iterrows():
                st.markdown(
                    f"""
                    ### {row['title']} ({row['match_score']}% match)  
                     - **Company:** {row['company']}  
                     - **Location:** {row['location']}  
                     - **Salary:** {row['salary']}  
                    ---
                    """
                )
