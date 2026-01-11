def initialize_hub():
    print("Initializing the talent hub...")

def load_candidates():
    print("Loading candidate profiles...")
    candidates = [
        {"name": "Alice", "skills": ["Python", "Data Analysis"]},
        {"name": "Bob", "skills": ["JavaScript", "Web Development"]},
        {"name": "Charlie", "skills": ["Project Management", "Leadership"]}
    ]
    print(f"Loaded {len(candidates)} candidates.")
    return candidates

def load_jobs():
    print("Loading job listings...")
    jobs = [
        {"title": "Data Scientist", "requirements": ["Python", "Machine Learning"]},
        {"title": "Frontend Developer", "requirements": ["JavaScript", "React"]},
        {"title": "Project Manager", "requirements": ["Leadership", "Agile"]}
    ]
    print(f"Loaded {len(jobs)} job listings.")
    return jobs

def match_talent(candidates, jobs):
    print("Matching talent to opportunities...")
    matches = []
    for candidate in candidates:
        for job in jobs:
            if any(skill in candidate["skills"] for skill in job["requirements"]):
                matches.append((candidate["name"], job["title"]))
    print(f"Found {len(matches)} matches.")
    return matches

def run_hub():
    initialize_hub()
    candidates = load_candidates()
    jobs = load_jobs()
    matches = match_talent(candidates, jobs)
    print("Matches:")
    for match in matches:
        print(f"Candidate: {match[0]} -> Job: {match[1]}")

if __name__ == "__main__":
    run_hub()
