#!/usr/bin/env python3
"""
WSGI entry point for the Climate Futures Storyteller web application.
This file is used by production WSGI servers like Gunicorn.
"""

import os

from web_interface import app, create_html_template

# Create templates directory if it doesn't exist
os.makedirs("templates", exist_ok=True)

# Create the HTML template
create_html_template()

if __name__ == "__main__":
    app.run()
