"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import *


def main() -> None:
    songs = load_songs("data/songs.csv") 
    print("Songs Loaded: " + str(len(songs)))
    # Starter example profile
    user_prefs0 = {"favorite_genre": "pop", "favorite_mood": "happy", "energy": 0.7}
    user_prefs1 = {"favorite_genre": "lofi", "favorite_mood": "chill", "energy": 0.3}
    lst = []
    lst.append(user_prefs0)
    # lst.append(user_prefs1)

    for i in lst:
        recommendations = recommend_songs(i, songs, k=5)
        print("\nTop recommendations for user: " + str(i) + "\n")
        for rec in recommendations:
            # You decide the structure of each returned item.
            # A common pattern is: (song, score, explanation)
            song, score, explanation = rec
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print("=============================")

if __name__ == "__main__":
    main()
