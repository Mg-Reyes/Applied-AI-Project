# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

RightSound 1.0

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

My recommender is designed to score songs with similar features to the users preferences and recommend them. These songs get ranked and the the k songs get recommende with reasons for their recommendations.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

The features of the songs that are used for the scores are genre, energy, mood and acoustics. Each one has a different weight and it all gets added into a final score used for the ranking.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

I used a list of 15 songs all with differing genres, energy, tempo, etc...
There are genres like lofi, rock, jazz, pop, focused, indie pop and more.
The user has 4 preferences that they provide to the recommender these are genre, energy, mood, and acoustics.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

The songs that are recommended are either in the same genre or have a lot of the other preferences the user provided.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

My recommender values the genre more than most of the other features combined, so if there is a perfect energy or mood match for a different song the one with a genre match will come on top. The recommender also prioritizes songs with acoustics, so users who say they like acoustics might get more songs that include it, and users that say they don't like it might still get some songs with a lot of acoustics. The mood comparasons are also very limited, the recommender only gives points for an exact match and not similar ones.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

I added users with different genres like lofi, rock, jazz, and pop. For every one of these users they were recommended songs with that genre. The ranking would be determined by the other features like energy.

What surprised me was that some songs that were not the same genre were in first place because of a really close match to the other features. I think this is a good thing and helps introduce new genres with similar sounds to users.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

I want to make the genre matching a little more complex so it awards points for similar genres.
Compare many more features like tempo and danceability.
Have a larger list of songs to recommend from.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

My biggest learning moment was getting the ranking and scoring system done. Using a list of dictionaries to store all of the songs and comparing them to the users preferences was challenging.

AI helped implement my logic and double checked that it was correct. I had to double check the way that the scoring logic was implemented. There were lines of code which were comparing the wrong values making the scores incorrect.

I would try to implement the use of AI to continually grow the data set and make better recommendations.