# ML Ops Lab 5: Cloud Run

This is my submission for the Google Cloud Run basic lab. 

**Note on changes:** Instead of deploying the standard "Hello World" app from the lab instructions, I decided to build a simple Random Fun Facts app using Flask just to make it a bit more interesting.

## What it does
It's a basic Python web app that serves random facts. I added a simple frontend with some CSS and also built out a few JSON API endpoints so you can fetch facts programmatically.

Live URL: https://random-facts-892604212498.us-central1.run.app

### API Endpoints
- `/` - The main web UI
- `/api/fact` - Gets a random fact as JSON
- `/api/fact/<category>` - Gets a fact by category (science, history, technology, nature)

## How to run it locally
If you want to test it out:
```
pip install flask
python app.py
```
Then go to `http://localhost:8080`

## Deployment steps used
For the Cloud Run deployment part of the lab, here were the commands I used:

1. Built the container:
```
docker build --platform linux/amd64 -t gcr.io/cloud-run-mlops/random-facts .
```

2. Pushed to Container Registry:
```
gcloud auth configure-docker
docker push gcr.io/cloud-run-mlops/random-facts
```

3. Deployed to Cloud Run:
```
gcloud run deploy random-facts \
  --image gcr.io/cloud-run-mlops/random-facts \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```
