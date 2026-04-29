# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

RightSound 1.0

---

## 2. Intended Use  

My recommender is designed to score songs with similar features to the users preferences and recommend them. These songs get ranked and the the k songs get recommende with reasons for their recommendations.

---

## 3. How the Model Works  

The features of the songs that are used for the scores are genre, energy, mood and acoustics. Each one has a different weight and it all gets added into a final score used for the ranking.

The AI addition uses a pre-trained language model (via the HuggingFace Inference API) to measure how semantically similar two genre or mood labels are. For example, "lofi" and "ambient" are recognized as related even though they are not the same word. This gives the recommender a more nuanced understanding of musical similarity instead of only rewarding exact matches.

---

## 4. Data  

I used a list of 15 songs all with differing genres, energy, tempo, etc...
There are genres like lofi, rock, jazz, pop, focused, indie pop and more.
The user has 4 preferences that they provide to the recommender these are genre, energy, mood, and acoustics.

---

## 5. Strengths  

The songs that are recommended are either in the same genre or have a lot of the other preferences the user provided.

---

## 6. Limitations and Bias 

My recommender values the genre more than most of the other features combined, so if there is a perfect energy or mood match for a different song the one with a genre match will come on top. The recommender also prioritizes songs with acoustics, so users who say they like acoustics might get more songs that include it, and users that say they don't like it might still get some songs with a lot of acoustics. The dataset is also small at only 15 songs, so some genre and mood preferences may have very few close matches to choose from.

---

## 7. Evaluation  

I added users with different genres like lofi, rock, jazz, and pop. For every one of these users they were recommended songs with that genre. The ranking would be determined by the other features like energy.

What surprised me was that some songs that were not the same genre were in first place because of a really close match to the other features. I think this is a good thing and helps introduce new genres with similar sounds to users.

---

## 8. Future Work  

Something that I can implement in future updates is being able to compare many more features like tempo and danceability.
Have a larger list of songs to recommend from.
Cache similarity scores for more genre and mood combinations so the recommender works well for any user input, not just the ones already tested.

---

## 9. Personal Reflection  

My biggest learning moment was getting the ranking and scoring system done. Using a list of dictionaries to store all of the songs and comparing them to the users preferences was challenging.

AI helped implement my logic and double checked that it was correct. I had to double check the way that the scoring logic was implemented. There were lines of code which were comparing the wrong values making the scores incorrect.

I would try to implement the use of AI to continually grow the data set and make better recommendations.