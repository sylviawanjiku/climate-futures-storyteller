# Climate Futures Storyteller - Deployment Guide

This guide covers deploying the Climate Futures Storyteller to various free hosting platforms.

## 🚀 Quick Deploy Options

### 1. Render (Recommended - Free Tier)

**Steps:**

1. Push your code to GitHub
2. Go to [render.com](https://render.com) and sign up
3. Click "New +" → "Web Service"
4. Connect your GitHub repository
5. Use these settings:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python web_interface.py`
   - **Environment:** Python 3
6. Click "Create Web Service"

**Features:**

- ✅ Free tier available
- ✅ Automatic deployments from GitHub
- ✅ Custom domain support
- ✅ SSL certificates included

### 2. Railway

**Steps:**

1. Push your code to GitHub
2. Go to [railway.app](https://railway.app) and sign up
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repository
5. Railway will auto-detect Python and deploy

**Features:**

- ✅ Free tier available
- ✅ Automatic deployments
- ✅ Built-in database support
- ✅ Easy environment variables

### 3. Heroku

**Steps:**

1. Install Heroku CLI
2. Login: `heroku login`
3. Create app: `heroku create your-app-name`
4. Deploy: `git push heroku main`

**Features:**

- ✅ Free tier (with limitations)
- ✅ Easy deployment
- ✅ Add-ons available

### 4. PythonAnywhere

**Steps:**

1. Sign up at [pythonanywhere.com](https://pythonanywhere.com)
2. Upload your code via Files tab
3. Create a new Web App
4. Configure WSGI file to point to your app

**Features:**

- ✅ Free tier available
- ✅ Python-focused hosting
- ✅ Easy file management

## 📁 Required Files

Make sure these files are in your repository:

- ✅ `web_interface.py` - Main web application
- ✅ `climate_storyteller.py` - Core AI agent
- ✅ `regional_data.py` - Climate data
- ✅ `requirements.txt` - Python dependencies
- ✅ `Procfile` - Heroku deployment
- ✅ `render.yaml` - Render deployment config
- ✅ `railway.json` - Railway deployment config

## 🔧 Environment Variables

No environment variables are required for basic functionality, but you can set:

- `PORT` - Port number (auto-detected by most platforms)
- `FLASK_ENV` - Set to "production" for production deployments

## 🐛 Troubleshooting

### Common Issues:

1. **Port binding errors:** Make sure your app uses `os.environ.get("PORT", 5001)`
2. **Template not found:** Ensure `templates/` directory is created
3. **Import errors:** Check all dependencies are in `requirements.txt`

### Debug Mode:

For local development, you can enable debug mode by changing:

```python
app.run(debug=True, host="0.0.0.0", port=port)
```

## 📊 Monitoring

Most platforms provide:

- Application logs
- Performance metrics
- Error tracking
- Uptime monitoring

## 🔄 Continuous Deployment

All platforms support automatic deployments when you push to your main branch.

## 💰 Cost

All recommended platforms offer free tiers suitable for this application:

- **Render:** Free tier with 750 hours/month
- **Railway:** Free tier with usage limits
- **Heroku:** Free tier (sleeps after inactivity)
- **PythonAnywhere:** Free tier with limited CPU seconds

## 🎯 Production Tips

1. **Disable debug mode** in production
2. **Set up monitoring** for uptime
3. **Use environment variables** for configuration
4. **Enable HTTPS** (most platforms do this automatically)
5. **Set up backups** if storing data

## 📞 Support

If you encounter issues:

1. Check the platform's documentation
2. Review application logs
3. Test locally first
4. Check all dependencies are installed
