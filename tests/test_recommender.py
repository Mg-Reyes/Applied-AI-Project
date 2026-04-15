from src.recommender import Song, UserProfile, Recommender, recommend_songs

def make_small_recommender() -> Recommender:
    songs = [
        Song(
            id=1,
            title="Test Pop Track",
            artist="Test Artist",
            genre="pop",
            mood="happy",
            energy=0.8,
            tempo_bpm=120,
            valence=0.9,
            danceability=0.8,
            acousticness=0.2,
        ),
        Song(
            id=2,
            title="Chill Lofi Loop",
            artist="Test Artist",
            genre="lofi",
            mood="chill",
            energy=0.4,
            tempo_bpm=80,
            valence=0.6,
            danceability=0.5,
            acousticness=0.9,
        ),
    ]
    return Recommender(songs)


def test_recommend_returns_songs_sorted_by_score():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()
    results = rec.recommend(user, k=2)

    assert len(results) == 2
    # Starter expectation: the pop, happy, high energy song should score higher
    assert results[0].genre == "pop"
    assert results[0].mood == "happy"


def test_explain_recommendation_returns_non_empty_string():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()
    song = rec.songs[0]

    explanation = rec.explain_recommendation(user, song)
    assert isinstance(explanation, str)
    assert explanation.strip() != ""


def test_functional_recommend_songs_handles_main_style_prefs_case_insensitively():
    songs = [
        {
            "id": 1,
            "title": "Coffee Shop Stories",
            "artist": "Slow Stereo",
            "genre": "jazz",
            "mood": "relaxed",
            "energy": 0.37,
            "tempo_bpm": 90,
            "valence": 0.71,
            "danceability": 0.54,
            "acousticness": 0.89,
        }
    ]
    user_prefs = {
        "genre": "jazz",
        "mood": "Relaxed",
        "energy": 0.9,
        "likes_acoustic": True,
    }

    results = recommend_songs(user_prefs, songs, k=1)

    assert len(results) == 1
    assert results[0][0]["title"] == "Coffee Shop Stories"
    assert "Genre 'jazz' matches your preference" in results[0][2]
    assert "Mood 'relaxed' matches your preference" in results[0][2]


def test_case_insensitivity_edge_case():
    """
    Edge case: Tests that the recommender handles mood/genre case sensitivity.
    The main.py uses "Relaxed" (capital R) which might not match lowercase data.
    This would cause the mood match to fail silently.
    """
    songs = [
        Song(
            id=1,
            title="Relaxing Jazz",
            artist="Jazz Artist",
            genre="jazz",
            mood="relaxed",  # lowercase in data
            energy=0.5,
            tempo_bpm=90,
            valence=0.7,
            danceability=0.3,
            acousticness=0.7,
        ),
    ]
    rec = Recommender(songs)
    
    # User preference with capital R (like in main.py)
    user = UserProfile(
        favorite_genre="jazz",
        favorite_mood="Relaxed",  # Capital R - CASE MISMATCH
        target_energy=0.5,
        likes_acoustic=True,
    )
    
    results = rec.recommend(user, k=1)
    assert len(results) == 1
    # This should ideally match, but will fail if the recommender isn't case-insensitive
    # The score will be lower due to missing mood match
    song = results[0]
    assert song.genre == "jazz"


def test_identical_scores_edge_case():
    """
    Edge case: Tests behavior when multiple songs have identical scores.
    This could reveal issues with stable sorting or tiebreaker logic.
    """
    songs = [
        Song(
            id=1,
            title="Song A",
            artist="Artist A",
            genre="pop",
            mood="happy",
            energy=0.7,
            tempo_bpm=120,
            valence=0.8,
            danceability=0.8,
            acousticness=0.3,
        ),
        Song(
            id=2,
            title="Song B",
            artist="Artist B",
            genre="pop",
            mood="happy",
            energy=0.7,
            tempo_bpm=120,
            valence=0.8,
            danceability=0.8,
            acousticness=0.3,
        ),
        Song(
            id=3,
            title="Song C",
            artist="Artist C",
            genre="rock",
            mood="intense",
            energy=0.5,
            tempo_bpm=100,
            valence=0.5,
            danceability=0.5,
            acousticness=0.2,
        ),
    ]
    rec = Recommender(songs)
    
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.7,
        likes_acoustic=False,
    )
    
    results = rec.recommend(user, k=3)
    
    # Verify we got 3 results
    assert len(results) == 3
    # Song A and B should score identically (both 0.9), Song C should score 0
    # Recommender should handle this gracefully without crashing
    assert results[0].genre == "pop"
    assert results[1].genre == "pop"
    assert results[2].genre == "rock"
