#!/usr/bin/env python3
"""
Deployment script for Climate Futures Storyteller.
This script helps prepare and deploy the application to various platforms.
"""

import os
import subprocess
import sys
from pathlib import Path


def check_requirements():
    """Check if all required files exist."""
    required_files = [
        "web_interface.py",
        "climate_storyteller.py",
        "regional_data.py",
        "requirements.txt",
        "Procfile",
        "render.yaml",
        "railway.json",
        "wsgi.py",
        "Dockerfile",
    ]

    missing_files = []
    for file in required_files:
        if not Path(file).exists():
            missing_files.append(file)

    if missing_files:
        print(f"❌ Missing required files: {', '.join(missing_files)}")
        return False

    print("✅ All required files present")
    return True


def test_application():
    """Test the application locally."""
    print("🧪 Testing application...")

    try:
        # Test imports
        subprocess.run(
            [
                sys.executable,
                "-c",
                "from climate_storyteller import ClimateStoryteller",
            ],
            check=True,
            capture_output=True,
        )
        subprocess.run(
            [sys.executable, "-c", "from web_interface import app"],
            check=True,
            capture_output=True,
        )

        print("✅ Application imports successful")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Application test failed: {e}")
        return False


def create_gitignore():
    """Create .gitignore file if it doesn't exist."""
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Flask
instance/
.webassets-cache

# Environment variables
.env
.env.local
.env.production

# Logs
*.log

# Templates (will be generated)
templates/index.html
"""

    if not Path(".gitignore").exists():
        with open(".gitignore", "w") as f:
            f.write(gitignore_content)
        print("✅ Created .gitignore file")
    else:
        print("✅ .gitignore already exists")


def show_deployment_instructions():
    """Show deployment instructions for different platforms."""
    print("\n🚀 DEPLOYMENT INSTRUCTIONS")
    print("=" * 50)

    print("\n1. RENDER (Recommended)")
    print("-" * 20)
    print("1. Push code to GitHub")
    print("2. Go to https://render.com")
    print("3. Connect GitHub repository")
    print("4. Use these settings:")
    print("   - Build Command: pip install -r requirements.txt")
    print("   - Start Command: python web_interface.py")
    print("   - Environment: Python 3")

    print("\n2. RAILWAY")
    print("-" * 15)
    print("1. Push code to GitHub")
    print("2. Go to https://railway.app")
    print("3. Deploy from GitHub repo")
    print("4. Railway auto-detects Python")

    print("\n3. HEROKU")
    print("-" * 12)
    print("1. Install Heroku CLI")
    print("2. heroku login")
    print("3. heroku create your-app-name")
    print("4. git push heroku main")

    print("\n4. DOCKER")
    print("-" * 12)
    print("1. docker build -t climate-storyteller .")
    print("2. docker run -p 5000:5000 climate-storyteller")
    print("3. Deploy to any Docker-compatible platform")


def main():
    """Main deployment preparation function."""
    print("🌍 Climate Futures Storyteller - Deployment Preparation")
    print("=" * 60)

    # Check requirements
    if not check_requirements():
        print("\n❌ Please ensure all required files are present before deploying")
        return False

    # Test application
    if not test_application():
        print("\n❌ Please fix application issues before deploying")
        return False

    # Create gitignore
    create_gitignore()

    # Show deployment instructions
    show_deployment_instructions()

    print("\n✅ Deployment preparation complete!")
    print("\nNext steps:")
    print("1. Initialize git repository: git init")
    print("2. Add files: git add .")
    print("3. Commit: git commit -m 'Initial commit'")
    print("4. Create GitHub repository and push")
    print("5. Deploy using one of the platforms above")

    return True


if __name__ == "__main__":
    main()
