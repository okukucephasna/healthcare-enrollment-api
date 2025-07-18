from flask import Flask, send_from_directory
from client_routes import client_bp
from program_routes import program_bp
from enrollment_routes import enrollment_bp
import os

app = Flask(__name__, static_folder="../frontend/build", static_url_path="/")

# Register API blueprints
app.register_blueprint(client_bp)
app.register_blueprint(program_bp)
app.register_blueprint(enrollment_bp)

# Serve React frontend
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_react(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
