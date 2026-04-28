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
    user_prefs0 = {"favorite_genre": "pop", "favorite_mood": "happy", "energy": 0.7, "likes_acoustic": True}
    user_prefs1 = {"favorite_genre": "lofi", "favorite_mood": "chill", "energy": 0.3, "likes_acoustic": False}
    user_perfect_song = {"favorite_genre": "lofi", "favorite_mood": "focused", "energy": 0.5, "likes_acoustic": True}
    lst = []
    lst.append(user_prefs0)
    lst.append(user_prefs1)
    lst.append(user_perfect_song)
    count = 1
    for i in lst:
        recommendations = recommend_songs(i, songs, k=5)
        print("========================================================================================================")
        print(f"\nTop recommendations for user #{count}: " + str(i) + "\n")
        count += 1
        song_count = 1
        for rec in recommendations:
            
            # You decide the structure of each returned item.
            # A common pattern is: (song, score, explanation)
            song, score, explanation = rec
            print(f"{song_count}. {song['title']} - Score: {score:.2f}")
            print(f"Reason: Because: {explanation}")
            print()
            song_count += 1

if __name__ == "__main__":
    main()
