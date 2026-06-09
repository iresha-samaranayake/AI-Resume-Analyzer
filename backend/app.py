from flask import Flask, jsonify, request
from services.pdf_reader import extract_text
from services.skill_extractor import extract_skills
from services.ats_scorer import calculate_ats_score
from services.role_recommender import recommend_roles


##
app = Flask(__name__)


## Basic route to test if the server is running
@app.route('/')
def home():
    return jsonify({ ## jsonify is used to reaturn a JSON response same as return {"message": "AI Resume Analyzer Backend Running", "status": "success"}
        "message": "AI Resume Analyzer Backend Running",
        "status": "success"
    })


## Health check endpoint
@app.route('/health')
def health():
    return {
        "status": "healthy",
        "server": "running"
    }

## Endpoint to handle resume uploads
@app.route('/upload', methods=['POST'])
def upload_resume():

    if 'file' not in request.files:
        return jsonify({
            "error": "No file uploaded"
        }), 400

    
    file = request.files['file']
    text = extract_text(file)
    skills = extract_skills(text)
    ats_result = calculate_ats_score(text, skills)
    role_recommendations = recommend_roles(skills)
    return jsonify({
        "ats_score": ats_result["score"],
        "feedback": ats_result["feedback"],
        "skills_Found": skills,
        "extracted_text": text,
        "role_recommendations": role_recommendations
    })


if __name__ == '__main__':
    app.run(debug=True)
    