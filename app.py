from flask import Flask, jsonify, render_template_string
import random

app = Flask(__name__)

FACTS = {
    "science": [
        "A teaspoon of a neutron star would weigh about 6 billion tons.",
        "Octopuses have three hearts and blue blood.",
        "Bananas are naturally radioactive due to their potassium content.",
        "Honey never spoils — archaeologists have found 3,000-year-old honey that was still edible.",
        "There are more stars in the universe than grains of sand on all of Earth's beaches.",
        "Water can boil and freeze at the same time — it's called the triple point.",
        "Your body contains about 0.2 mg of gold, mostly in your blood.",
        "A day on Venus is longer than a year on Venus.",
    ],
    "history": [
        "Cleopatra lived closer in time to the Moon landing than to the construction of the Great Pyramid.",
        "Oxford University is older than the Aztec Empire.",
        "The shortest war in history lasted 38 minutes (Britain vs. Zanzibar, 1896).",
        "Ancient Romans used crushed mouse brains as toothpaste.",
        "Napoleon was once attacked by a horde of rabbits during a hunting trip.",
        "The first computer programmer was Ada Lovelace, in the 1840s.",
        "Vikings used to give kittens to new brides as essential household gifts.",
        "The Great Fire of London in 1666 destroyed 13,200 houses but only 6 verified deaths were recorded.",
    ],
    "technology": [
        "The first 1 GB hard drive (1980) weighed about 550 pounds and cost $40,000.",
        "About 90% of the world's currency exists only in digital form.",
        "The first website ever made is still online: info.cern.ch.",
        "There are more devices connected to the internet than people on Earth.",
        "The QWERTY keyboard was designed to slow typists down to prevent typewriter jams.",
        "The first computer virus was created in 1983 as a university experiment.",
        "NASA's entire Apollo 11 guidance computer had less processing power than a modern calculator.",
        "Email existed before the World Wide Web.",
    ],
    "nature": [
        "A group of flamingos is called a 'flamboyance.'",
        "Trees can communicate with each other through an underground fungal network called the 'Wood Wide Web.'",
        "The Amazon Rainforest produces about 20% of the world's oxygen.",
        "Crows can recognize and remember human faces for years.",
        "Sea otters hold hands while sleeping so they don't drift apart.",
        "A single bolt of lightning contains enough energy to toast 100,000 slices of bread.",
        "Dolphins have names for each other and can call out to specific individuals.",
        "The oldest known living tree is over 5,000 years old.",
    ],
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Random Fun Facts</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Inter', sans-serif;
            min-height: 100vh;
            display: flex; align-items: center; justify-content: center;
            background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
            color: #fff;
            padding: 20px;
        }
        .card {
            max-width: 560px; width: 100%;
            background: rgba(255,255,255,0.07);
            backdrop-filter: blur(16px);
            border: 1px solid rgba(255,255,255,0.12);
            border-radius: 24px;
            padding: 48px 36px;
            text-align: center;
            box-shadow: 0 8px 32px rgba(0,0,0,0.4);
            animation: fadeIn 0.6s ease;
        }
        @keyframes fadeIn { from { opacity:0; transform: translateY(20px); } to { opacity:1; transform: translateY(0); } }
        .emoji { font-size: 56px; margin-bottom: 16px; }
        .category {
            display: inline-block;
            background: linear-gradient(135deg, #667eea, #764ba2);
            padding: 4px 16px; border-radius: 20px;
            font-size: 12px; font-weight: 600;
            text-transform: uppercase; letter-spacing: 1.5px;
            margin-bottom: 24px;
        }
        .fact {
            font-size: 20px; line-height: 1.6;
            font-weight: 400; color: rgba(255,255,255,0.9);
            margin-bottom: 32px;
        }
        .btn {
            display: inline-block; padding: 14px 36px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: #fff; border: none; border-radius: 14px;
            font-size: 16px; font-weight: 600;
            cursor: pointer; text-decoration: none;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .btn:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(102,126,234,0.5); }
        .btn:active { transform: translateY(0); }
        .footer { margin-top: 28px; font-size: 12px; color: rgba(255,255,255,0.35); }
    </style>
</head>
<body>
    <div class="card">
        <div class="emoji">{{ emoji }}</div>
        <div class="category">{{ category }}</div>
        <p class="fact">{{ fact }}</p>
        <a class="btn" href="/">New Fact ✨</a>
        <p class="footer">Deployed on Google Cloud Run</p>
    </div>
</body>
</html>
"""

CATEGORY_EMOJIS = {
    "science": "🔬",
    "history": "📜",
    "technology": "💻",
    "nature": "🌿",
}


@app.route("/")
def index():
    category = random.choice(list(FACTS.keys()))
    fact = random.choice(FACTS[category])
    emoji = CATEGORY_EMOJIS[category]
    return render_template_string(HTML_TEMPLATE, category=category, fact=fact, emoji=emoji)


@app.route("/api/fact")
def api_fact():
    category = random.choice(list(FACTS.keys()))
    fact = random.choice(FACTS[category])
    return jsonify({"category": category, "fact": fact})


@app.route("/api/fact/<category>")
def api_fact_by_category(category):
    category = category.lower()
    if category not in FACTS:
        return jsonify({"error": f"Unknown category. Choose from: {', '.join(FACTS.keys())}"}), 404
    fact = random.choice(FACTS[category])
    return jsonify({"category": category, "fact": fact})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
