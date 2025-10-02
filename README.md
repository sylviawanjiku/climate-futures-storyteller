# Climate Futures Storyteller

An AI-powered storytelling system that creates compelling, realistic narratives about how climate change is transforming daily life around the world. The system generates 1000-1500 word stories that help readers connect emotionally with climate change beyond abstract statistics.

## Features

- **Realistic Climate Scenarios**: Stories set between present day and 2050 based on latest climate science
- **Regional Specificity**: Tailored climate impacts for different regions and communities
- **Diverse Characters**: Protagonists from various backgrounds, ages, and socioeconomic statuses
- **Balanced Narratives**: Stories that balance challenges with human adaptations and solutions
- **Sensory Details**: First-person perspectives with tangible climate impact descriptions

## Climate Science Base (as of October 2025)

- Global temperatures trending toward 1.5°C above pre-industrial levels
- Increasing frequency of extreme weather events (floods, droughts, heatwaves, wildfires)
- Rising sea levels affecting coastal communities
- Shifting agricultural zones and growing seasons
- Biodiversity loss and ecosystem disruption

## Usage

```python
from climate_storyteller import ClimateStoryteller

# Initialize the storyteller
storyteller = ClimateStoryteller()

# Generate a story for a specific location and climate impact
story = storyteller.generate_story(
    location="Miami, Florida",
    climate_impact="sea_level_rise",
    character_focus="coastal_community"
)

print(story)
```

## Quick Start

### Local Development

```bash
# Clone the repository
git clone <your-repo-url>
cd Stories-Thinking

# Install dependencies
pip install -r requirements.txt

# Start the web interface
python web_interface.py
# Open http://localhost:5001 in your browser
```

### One-Command Start

```bash
./start.sh
```

## Deployment

### Free Hosting Options

1. **Render (Recommended)**

   - Go to [render.com](https://render.com)
   - Connect your GitHub repository
   - Deploy automatically

2. **Railway**

   - Go to [railway.app](https://railway.app)
   - Deploy from GitHub repo

3. **Heroku**

   ```bash
   heroku create your-app-name
   git push heroku main
   ```

4. **Docker**
   ```bash
   docker build -t climate-storyteller .
   docker run -p 5000:5000 climate-storyteller
   ```

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.

## Installation

```bash
pip install -r requirements.txt
```

## Project Structure

- `climate_storyteller.py` - Main AI agent class
- `regional_data.py` - Climate impact data for different regions
- `story_templates.py` - Story structure and narrative templates
- `examples/` - Sample generated stories
- `requirements.txt` - Python dependencies
