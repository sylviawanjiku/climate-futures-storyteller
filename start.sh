#!/bin/bash

# Climate Futures Storyteller - Quick Start Script

echo "🌍 Climate Futures Storyteller - Quick Start"
echo "============================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip."
    exit 1
fi

# Install dependencies
echo "📦 Installing dependencies..."
pip3 install -r requirements.txt

# Test the application
echo "🧪 Testing application..."
python3 -c "from climate_storyteller import ClimateStoryteller; print('✅ Core module working')"
python3 -c "from web_interface import app; print('✅ Web interface working')"

# Start the web interface
echo "🚀 Starting web interface..."
echo "Open your browser to http://localhost:5001"
echo "Press Ctrl+C to stop the server"
echo ""

python3 web_interface.py
