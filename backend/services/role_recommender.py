from data.roles import ROLE_SKILLS


def recommend_roles(skills):

    recommendations = []

    for role, required_skills in ROLE_SKILLS.items():

        matched = 0

        for skill in required_skills:

            if skill in skills:
                matched += 1

        match_percentage = int(
            (matched / len(required_skills)) * 100
        )

        if match_percentage >= 50:

            recommendations.append({
                "role": role,
                "match_percentage": match_percentage
            })

    recommendations.sort(
        key=lambda x: x["match_percentage"],
        reverse=True
    )

    return recommendations