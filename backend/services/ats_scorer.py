def calculate_ats_score(text, skills):

    score = 0
    feedback = []

    # Skills Score (40 points)
    skill_count = len(skills)

    if skill_count >= 10:
        score += 40
        feedback.append("Excellent technical skill coverage.")
    elif skill_count >= 6:
        score += 30
        feedback.append("Good technical skill coverage.")
    elif skill_count >= 3:
        score += 20
        feedback.append("Consider adding more technical skills.")
    else:
        score += 10
        feedback.append("Very few technical skills detected.")

    # Projects Score (20 points)
    if "\nprojects\n" in text.lower():
        score += 20
        feedback.append("Projects section detected.")
    else:
        feedback.append("Add a projects section.")

    # Education Score (20 points)
    if "education" in text.lower():
        score += 20
        feedback.append("Education section detected.")
    else:
        feedback.append("Education section missing.")

    # Contact Score (20 points)
    if "@" in text:
        score += 20
        feedback.append("Contact information detected.")
    else:
        feedback.append("Add contact information.")

    return {
        "score": score,
        "feedback": feedback
    }