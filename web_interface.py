#!/usr/bin/env python3
"""
Web interface for the Climate Futures Storyteller.

This module provides a simple web interface using Flask for generating
climate change narratives through a browser.
"""

import json
import os

from flask import Flask, jsonify, render_template, request, send_from_directory

from climate_storyteller import ClimateStoryteller

app = Flask(__name__)
storyteller = ClimateStoryteller()


@app.route("/")
def index():
    """Main page with story generation form."""
    return render_template("index.html")


@app.route("/api/locations")
def get_locations():
    """API endpoint to get available locations."""
    return jsonify(storyteller.list_available_locations())


@app.route("/api/impacts")
def get_impacts():
    """API endpoint to get available climate impacts."""
    return jsonify(storyteller.list_available_impacts())


@app.route("/api/characters")
def get_characters():
    """API endpoint to get available character types."""
    return jsonify(storyteller.list_available_characters())


@app.route("/api/generate", methods=["POST"])
def generate_story():
    """API endpoint to generate a story."""
    try:
        data = request.get_json()

        location = data.get("location")
        impact = data.get("impact")
        character = data.get("character")
        length = data.get("length", 1200)

        story = storyteller.generate_story(
            location=location,
            climate_impact=impact,
            character_focus=character,
            story_length=length,
        )

        return jsonify(
            {
                "success": True,
                "story": story,
                "metadata": {
                    "location": location,
                    "impact": impact,
                    "character": character,
                    "length": length,
                },
            }
        )

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/api/random")
def generate_random_story():
    """API endpoint to generate a random story."""
    try:
        story = storyteller.generate_story()
        return jsonify({"success": True, "story": story})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/health")
def health_check():
    """Health check endpoint for monitoring."""
    return jsonify(
        {
            "status": "healthy",
            "service": "Climate Futures Storyteller",
            "version": "1.0.0",
        }
    )


def create_html_template():
    """Create the HTML template for the web interface."""
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Climate Futures Storyteller</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .header {
            text-align: center;
            color: white;
            margin-bottom: 30px;
        }
        
        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        .header p {
            font-size: 1.2em;
            opacity: 0.9;
        }
        
        .main-content {
            display: grid;
            grid-template-columns: 1fr 2fr;
            gap: 30px;
            margin-bottom: 30px;
        }
        
        .form-panel {
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        .form-group label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
            color: #555;
        }
        
        .form-group select,
        .form-group input {
            width: 100%;
            padding: 12px;
            border: 2px solid #e1e5e9;
            border-radius: 8px;
            font-size: 16px;
            transition: border-color 0.3s ease;
        }
        
        .form-group select:focus,
        .form-group input:focus {
            outline: none;
            border-color: #667eea;
        }
        
        .btn {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 15px 30px;
            border-radius: 8px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            width: 100%;
            margin-bottom: 10px;
        }
        
        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }
        
        .btn:active {
            transform: translateY(0);
        }
        
        .btn-secondary {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        }
        
        .story-panel {
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            max-height: 80vh;
            overflow-y: auto;
        }
        
        .story-content {
            white-space: pre-wrap;
            line-height: 1.8;
            font-size: 16px;
        }
        
        .loading {
            text-align: center;
            color: #666;
            font-style: italic;
        }
        
        .error {
            color: #e74c3c;
            background: #fdf2f2;
            padding: 15px;
            border-radius: 8px;
            border-left: 4px solid #e74c3c;
            margin-bottom: 20px;
        }
        
        .success {
            color: #27ae60;
            background: #f0f9f0;
            padding: 15px;
            border-radius: 8px;
            border-left: 4px solid #27ae60;
            margin-bottom: 20px;
        }
        
        .metadata {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
            font-size: 14px;
            color: #666;
        }
        
        .metadata strong {
            color: #333;
        }
        
        @media (max-width: 768px) {
            .main-content {
                grid-template-columns: 1fr;
            }
            
            .header h1 {
                font-size: 2em;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Climate Futures Storyteller</h1>
            <p>Generate compelling narratives about how climate change transforms daily life</p>
        </div>
        
        <div class="main-content">
            <div class="form-panel">
                <h2>Story Parameters</h2>
                
                <div class="form-group">
                    <label for="location">Location (Optional)</label>
                    <select id="location" name="location">
                        <option value="">Random Location</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label for="impact">Climate Impact (Optional)</label>
                    <select id="impact" name="impact">
                        <option value="">Random Impact</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label for="character">Character Focus (Optional)</label>
                    <select id="character" name="character">
                        <option value="">Random Character</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label for="length">Story Length (words)</label>
                    <input type="number" id="length" name="length" value="1200" min="500" max="2000">
                </div>
                
                <button class="btn" onclick="generateStory()">Generate Story</button>
                <button class="btn btn-secondary" onclick="generateRandomStory()">Random Story</button>
            </div>
            
            <div class="story-panel">
                <h2>Generated Story</h2>
                <div id="story-content">
                    <p class="loading">Click "Generate Story" to create a climate futures narrative...</p>
                </div>
            </div>
        </div>
    </div>

    <script>
        // Load available options when page loads
        document.addEventListener('DOMContentLoaded', function() {
            loadLocations();
            loadImpacts();
            loadCharacters();
        });
        
        async function loadLocations() {
            try {
                const response = await fetch('/api/locations');
                const locations = await response.json();
                const select = document.getElementById('location');
                
                locations.forEach(location => {
                    const option = document.createElement('option');
                    option.value = location;
                    option.textContent = location.replace('_', ' ').replace(/\b\w/g, l => l.toUpperCase());
                    select.appendChild(option);
                });
            } catch (error) {
                console.error('Error loading locations:', error);
            }
        }
        
        async function loadImpacts() {
            try {
                const response = await fetch('/api/impacts');
                const impacts = await response.json();
                const select = document.getElementById('impact');
                
                impacts.forEach(impact => {
                    const option = document.createElement('option');
                    option.value = impact;
                    option.textContent = impact.replace('_', ' ').replace(/\b\w/g, l => l.toUpperCase());
                    select.appendChild(option);
                });
            } catch (error) {
                console.error('Error loading impacts:', error);
            }
        }
        
        async function loadCharacters() {
            try {
                const response = await fetch('/api/characters');
                const characters = await response.json();
                const select = document.getElementById('character');
                
                characters.forEach(character => {
                    const option = document.createElement('option');
                    option.value = character;
                    option.textContent = character.replace('_', ' ').replace(/\b\w/g, l => l.toUpperCase());
                    select.appendChild(option);
                });
            } catch (error) {
                console.error('Error loading characters:', error);
            }
        }
        
        async function generateStory() {
            const location = document.getElementById('location').value;
            const impact = document.getElementById('impact').value;
            const character = document.getElementById('character').value;
            const length = document.getElementById('length').value;
            
            const storyContent = document.getElementById('story-content');
            storyContent.innerHTML = '<p class="loading">Generating story...</p>';
            
            try {
                const response = await fetch('/api/generate', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        location: location || null,
                        impact: impact || null,
                        character: character || null,
                        length: parseInt(length)
                    })
                });
                
                const data = await response.json();
                
                if (data.success) {
                    let content = '';
                    
                    if (data.metadata) {
                        content += '<div class="metadata">';
                        content += '<strong>Story Details:</strong><br>';
                        if (data.metadata.location) content += `Location: ${data.metadata.location}<br>`;
                        if (data.metadata.impact) content += `Impact: ${data.metadata.impact}<br>`;
                        if (data.metadata.character) content += `Character: ${data.metadata.character}<br>`;
                        content += `Length: ${data.metadata.length} words`;
                        content += '</div>';
                    }
                    
                    content += '<div class="story-content">' + data.story + '</div>';
                    storyContent.innerHTML = content;
                } else {
                    storyContent.innerHTML = '<div class="error">Error: ' + data.error + '</div>';
                }
            } catch (error) {
                storyContent.innerHTML = '<div class="error">Error generating story: ' + error.message + '</div>';
            }
        }
        
        async function generateRandomStory() {
            const storyContent = document.getElementById('story-content');
            storyContent.innerHTML = '<p class="loading">Generating random story...</p>';
            
            try {
                const response = await fetch('/api/random');
                const data = await response.json();
                
                if (data.success) {
                    storyContent.innerHTML = '<div class="story-content">' + data.story + '</div>';
                } else {
                    storyContent.innerHTML = '<div class="error">Error: ' + data.error + '</div>';
                }
            } catch (error) {
                storyContent.innerHTML = '<div class="error">Error generating story: ' + error.message + '</div>';
            }
        }
    </script>
</body>
</html>"""

    with open("templates/index.html", "w", encoding="utf-8") as f:
        f.write(html_content)


if __name__ == "__main__":
    # Create templates directory if it doesn't exist
    os.makedirs("templates", exist_ok=True)

    # Create the HTML template
    create_html_template()

    # Get port from environment variable (for deployment) or use default
    port = int(os.environ.get("PORT", 5001))

    print("Starting Climate Futures Storyteller web interface...")
    print(f"Open your browser to http://localhost:{port}")
    app.run(debug=False, host="0.0.0.0", port=port)
