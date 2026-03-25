# Cloud Run Lab: Random Fun Facts App

A simple Python Flask application designed to be containerized with Docker and deployed to **Google Cloud Run**. This project is part of a Google Cloud Run basic lab.

**Changes made:** Used a "Random Facts" app instead of the basic "Hello World" app described in the lab instructions.

## Live Demo
🔗 **[https://random-facts-892604212498.us-central1.run.app](https://random-facts-892604212498.us-central1.run.app)**

## Features
- **32 Fun Facts** across 4 categories: Science 🔬, History 📜, Technology 💻, and Nature 🌿
- **Modern Glassmorphism UI** with smooth fade-in animations and an interactive "New Fact ✨" button
- **JSON API Endpoints** for programmatic access to the facts

## API Endpoints
| HTTP Method | Route | Description |
|-----------|-------|-------------|
| `GET` | `/` | Returns the styled HTML frontend with a random fact |
| `GET` | `/api/fact` | Returns a random fact from any category as JSON |
| `GET` | `/api/fact/<category>` | Returns a random fact from a specific category (`science`, `history`, `technology`, `nature`) as JSON |

## Local Development
To run this application locally without Docker:

1. Install requirements:
   ```bash
   pip install flask
   ```
2. Run the application:
   ```bash
   python app.py
   ```
3. Open `http://localhost:8080` in your browser.

## Docker & Cloud Run Deployment

### 1. Build the Docker Image
*(Note: Use `--platform linux/amd64` when building on an Apple Silicon Mac to ensure compatibility with Cloud Run)*
```bash
docker build --platform linux/amd64 -t gcr.io/YOUR_PROJECT_ID/random-facts .
```

### 2. Push to Google Container Registry
```bash
gcloud auth configure-docker
docker push gcr.io/YOUR_PROJECT_ID/random-facts
```

### 3. Deploy to Cloud Run
```bash
gcloud run deploy random-facts \
  --image gcr.io/YOUR_PROJECT_ID/random-facts \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```
