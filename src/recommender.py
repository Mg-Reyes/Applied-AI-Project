import csv
import json
import os
import requests
import numpy as np
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

_HF_API_URL = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"
_CACHE_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "similarity_cache.json")

def _load_cache() -> dict:
    try:
        with open(_CACHE_PATH, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def _save_cache(cache: dict) -> None:
    with open(_CACHE_PATH, "w") as f:
        json.dump(cache, f)

_cache = _load_cache()

def _get_embeddings(texts: List[str]) -> List[List[float]]:
    token = os.environ.get("HF_TOKEN", "")
    response = requests.post(
        _HF_API_URL,
        headers={"Authorization": f"Bearer {token}"},
        json={"inputs": texts},
    )
    response.raise_for_status()
    result = response.json()
    embeddings = []
    for emb in result:
        # Some models return token-level (3D); mean-pool to sentence-level if needed
        arr = np.array(emb)
        embeddings.append(arr.mean(axis=0) if arr.ndim > 1 else arr)
    return embeddings

def _cosine_similarity(a, b) -> float:
    a, b = np.array(a), np.array(b)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

def _similarity(a: str, b: str, kind: str) -> float:
    a, b = a.lower(), b.lower()
    if a == b:
        return 1.0

    key = f"{kind}:{a}:{b}"
    if key in _cache:
        return _cache[key]

    try:
        embeddings = _get_embeddings([a, b])
        score = _cosine_similarity(embeddings[0], embeddings[1])
        score = max(0.0, min(1.0, score))
    except Exception:
        score = 0.1

    _cache[key] = score
    _save_cache(_cache)
    return score

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs: List[Dict] = []
    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            songs.append(
                {
                    "id": int(row["id"]),
                    "title": row["title"],
                    "artist": row["artist"],
                    "genre": row["genre"],
                    "mood": row["mood"],
                    "energy": float(row["energy"]),
                    "tempo_bpm": float(row["tempo_bpm"]),
                    "valence": float(row["valence"]),
                    "danceability": float(row["danceability"]),
                    "acousticness": float(row["acousticness"]),
                }
            )
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons = []

    # Genre and mood similarity via sentence embeddings (40% + 30%)
    user_genre = user_prefs.get('favorite_genre', '')
    user_mood = user_prefs.get('favorite_mood', '')
    song_genre = song.get('genre', '')
    song_mood = song.get('mood', '')

    genre_similarity = _similarity(user_genre, song_genre, "genre")
    mood_similarity = _similarity(user_mood, song_mood, "mood")

    score += genre_similarity * 0.40
    if genre_similarity >= 0.7:
        reasons.append(f"Genre '{song['genre']}' is similar to your preference")

    score += mood_similarity * 0.30
    if mood_similarity >= 0.7:
        reasons.append(f"Mood '{song['mood']}' is similar to your preference")

    # Energy match (20%) - closer to target = higher score
    song_energy = song["energy"]
    target_energy = user_prefs["energy"]
    energy_diff = abs(song_energy - target_energy)
    energy_score = max(0, 1 - energy_diff)  # 1.0 if exact match, 0.0 if diff >= 1
    score += energy_score * 0.20
    if energy_score > 0.5:
        reasons.append(f"Energy level {song_energy:.2f} is close to your target of {target_energy:.2f}")

    # Acousticness match (10%)
    song_acousticness = song["acousticness"]
    likes_acoustic = user_prefs.get("likes_acoustic", False)
    if (likes_acoustic and song_acousticness >= 0.4):
        score += song_acousticness * .1
        reasons.append("Acousticness matches your preference")
    else:
        if (not likes_acoustic and song_acousticness <= 0.4):
            score += song_acousticness * .1
            reasons.append("Acousticness matches your preference")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored_songs = []
    
    for i, song in enumerate(songs):
        #print(f"Scoring song {i + 1}/{len(songs)}: {song['title']}")
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons) if reasons else "No specific match found"
        scored_songs.append((song, score, explanation))
    
    # Sort by score in descending order
    scored_songs.sort(key=lambda x: x[1], reverse=True)
    
    # Return top k songs
    return scored_songs[:k]
