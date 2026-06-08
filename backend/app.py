from flask import Flask, jsonify, request

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

    return jsonify({
        "message": "File received successfully"
    })


if __name__ == '__main__':
    app.run(debug=True)
    