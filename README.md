# 🎵 Original: Music Recommender Simulation

The original project will take in some user preferences for song genre, mood, energy, and acousticness. It will then read a list of songs and rank them based on these preferences.

# 🎵 Applied AI: Music Recommender Simulation

This project takes in user preferences for song genre, mood, energy, and acousticness, then reads a list of songs and ranks them based on those preferences.

The AI addition replaces the original all-or-nothing genre and mood matching with a **predefined similarity map**. The new things it can do before making a recommendation:

- Differentiate between similar genres, for example "lofi" and "ambient", and give it a similarity score
- Do the same for mood comparison, for example "chill" and "relaxed"

The original project only had an all-or-nothing approach to scoring the mood and genre.
This addition allows the recommender to make more accurate and realistic recommendations.

## System Diagram

The program will college the users preferences and load in all of the songs from the .csv file. These will be sent to the recommender which will then use the preferences and song list to compare and score each song. These songs will then get ranked based on the final score they recieved.

## Setup Requirements

1. Create virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
python3 src/main.py
```

## Sample interactions



## Design Decisions

At first I wanted to make an API call using the Gemini API, but the free tier had a quota limit of 0 for my account. I then tried `sentence_transformers` (a local ML model) but it had compatibility issues with Python 3.12 and 3.14. The final solution was a predefined similarity map, it runs instantly with no external dependencies while still providing smarter-than-exact-match scoring for genre and mood.

## Testing Summary

The Gemini API calls did not work due to quota limitations. The `sentence_transformers` library had compatibility issues with the available Python versions. Tests were written to verify that similar genres and moods score higher than unrelated ones using the similarity map.

## Reflection

