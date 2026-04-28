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

1. Create virtual environment (Optional):
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

I tested the output with 3 different users with different preferences. These were their preferences and the output from the program:

User 1. "favorite_genre": "pop", "favorite_mood": "happy", "energy": 0.7, "likes_acoustic": True

1. Sunrise City - Score: 0.88
Reason: Because: Genre 'pop' is similar to your preference; Mood 'happy' is similar to your preference; Energy level 0.82 is close to your target of 0.70

2. Gym Hero - Score: 0.58
Reason: Because: Genre 'pop' is similar to your preference; Energy level 0.93 is close to your target of 0.70

3. Rooftop Lights - Score: 0.53
Reason: Because: Mood 'happy' is similar to your preference; Energy level 0.76 is close to your target of 0.70

4. Afterglow Drive - Score: 0.51
Reason: Because: Genre 'synthwave' is similar to your preference; Energy level 0.68 is close to your target of 0.70

5. Pixel Sunset - Score: 0.50
Reason: Because: Mood 'happy' is similar to your preference; Energy level 0.88 is close to your target of 0.70

User #2. "favorite_genre": "lofi", "favorite_mood": "chill", "energy": 0.3, "likes_acoustic": False

1. Library Rain - Score: 0.89
Reason: Because: Genre 'lofi' is similar to your preference; Mood 'chill' is similar to your preference; Energy level 0.35 is close to your target of 0.30

2. Midnight Coding - Score: 0.88
Reason: Because: Genre 'lofi' is similar to your preference; Mood 'chill' is similar to your preference; Energy level 0.42 is close to your target of 0.30

3. Spacewalk Thoughts - Score: 0.78
Reason: Because: Genre 'ambient' is similar to your preference; Mood 'chill' is similar to your preference; Energy level 0.28 is close to your target of 0.30

4. Quiet Harbor - Score: 0.77
Reason: Because: Genre 'ambient' is similar to your preference; Mood 'chill' is similar to your preference; Energy level 0.33 is close to your target of 0.30

5. Focus Flow - Score: 0.59
Reason: Because: Genre 'lofi' is similar to your preference; Energy level 0.50 is close to your target of 0.30

User #3: "favorite_genre": "lofi", "favorite_mood": "focused", "energy": 0.5, "likes_acoustic": True

1. Focus Flow - Score: 1.00
Reason: Because: Genre 'lofi' is similar to your preference; Mood 'focused' is similar to your preference; Energy level 0.50 is close to your target of 0.50; Acousticness matches your preference

2. Library Rain - Score: 0.69
Reason: Because: Genre 'lofi' is similar to your preference; Energy level 0.35 is close to your target of 0.50; Acousticness matches your preference

3. Midnight Coding - Score: 0.69
Reason: Because: Genre 'lofi' is similar to your preference; Energy level 0.42 is close to your target of 0.50; Acousticness matches your preference

4. Quiet Harbor - Score: 0.57
Reason: Because: Genre 'ambient' is similar to your preference; Energy level 0.33 is close to your target of 0.50; Acousticness matches your preference

5. Spacewalk Thoughts - Score: 0.56
Reason: Because: Genre 'ambient' is similar to your preference; Energy level 0.28 is close to your target of 0.50; Acousticness matches your preference

These outputs match the users preferences and making the recommendations very accurate.

## Design Decisions

At first I wanted to make an API call using the Gemini API, but the free tier had a quota limit of 0 for my account. I then tried `sentence_transformers` (a local ML model) but it had compatibility issues with Python 3.12 and 3.14. The final solution was a predefined similarity map, it runs instantly with no external dependencies while still providing smarter-than-exact-match scoring for genre and mood.

## Testing Summary

The Gemini API calls did not work due to quota limitations. The `sentence_transformers` library had compatibility issues with the available Python versions. Tests were written to verify that similar genres and moods score higher than unrelated ones using the similarity map.

Before the recommender would only give points if the genre matching was a perfect match. Now all the genres are grouped based on how similar they are. If the genre is not the same, but is in the same group, points will be awarded to the song.

## Reflection

AI was helpful with the implementation of a better scoring system for the recommender. It was able to help me try out and decide on what the best approach would be. In the end I went with the similarity mapping, this only works because of the small 15 song list. 

One error that the AI made was trying to access the value in the user preferences dictionary by the wrong key. This meant that nothing was being returned and the genre wasn't being considered. 