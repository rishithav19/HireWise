# Skill2Work — AI Job Recommendation for Low-Income Workers  

Helping workers find suitable jobs using their skills — aligned with **SDG 1: No Poverty**.  

---

## Project Overview  
Millions of semi-skilled and blue-collar workers struggle to find jobs as most portals focus on degree-based roles.  
**Skill2Work** is an **AI-powered job recommender system** that allows workers to enter their skills and instantly discover suitable jobs.  

- Built using **Natural Language Processing (TF-IDF + Cosine Similarity)**.  
- Provides **skill-based job recommendations** instead of degree-based filtering.  
- Frontend powered by **Streamlit** for an easy, interactive demo.  
- Dataset sourced from **Kaggle synthetic job postings** (cleaned version included).  

---

## Tech Stack  
- **Python 3.12**  
- **Streamlit** (frontend)  
- **scikit-learn, pandas, numpy** (ML + data processing)  

---

## Repository Structure  

```
├── app.py                # Streamlit frontend
├── recommender.py        # Core AI recommendation logic
├── clean_jobs.py         # Dataset cleaning script
├── data/
│   ├── jobs.csv          # Original dataset (ignored in git)
│   └── cleaned_jobs.csv  # Cleaned dataset used in demo
├── requirements.txt
└── README.md
```

---

## Setup & Installation  

1. **Clone this repo**  
   ```bash
   git clone https://github.com/<your-username>/skill2work.git
   cd skill2work
   ```

2. **Create virtual environment**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**  
   ```bash
   streamlit run app.py
   ```

---

## Dataset  
- Source: **Kaggle Job Postings Dataset (synthetic)**  
- Columns used: `title, company, location, salary, skills`  
- Cleaned dataset included as `data/cleaned_jobs.csv`.  

---

## Future Scope  
- Integration with **real-world job APIs** (Naukri, LinkedIn, Indeed).  
- Support for **regional languages** for inclusivity.  
- Smarter matching using **word embeddings (BERT, fastText)**.  
- Mobile app for easier worker access.  

---
 
