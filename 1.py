import streamlit as st
import random
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="VibeTunes - Emotion Music Recommender",
    page_icon="🎵",
    layout="centered"
)

# --- MOCK DATA DATABASE ---
# A list of dictionaries acting as our song database
SONG_DATABASE = [
    {"title": "Happy", "artist": "Pharrell Williams", "mood": "Happy", "link": "https://www.youtube.com/results?search_query=Happy+Pharrell"},
    {"title": "Walking on Sunshine", "artist": "Katrina & The Waves", "mood": "Happy", "link": "https://www.youtube.com/results?search_query=Walking+on+Sunshine"},
    {"title": "Can't Stop the Feeling!", "artist": "Justin Timberlake", "mood": "Happy", "link": "https://www.youtube.com/results?search_query=Cant+Stop+the+Feeling"},
    {"title": "Someone Like You", "artist": "Adele", "mood": "Sad", "link": "https://www.youtube.com/results?search_query=Someone+Like+You+Adele"},
    {"title": "Fix You", "artist": "Coldplay", "mood": "Sad", "link": "https://www.youtube.com/results?search_query=Fix+You+Coldplay"},
    {"title": "The Night We Met", "artist": "Lord Huron", "mood": "Sad", "link": "https://www.youtube.com/results?search_query=The+Night+We+Met"},
    {"title": "Eye of the Tiger", "artist": "Survivor", "mood": "Energetic", "link": "https://www.youtube.com/results?search_query=Eye+of+the+Tiger"},
    {"title": "Stronger", "artist": "Kanye West", "mood": "Energetic", "link": "https://www.youtube.com/results?search_query=Stronger+Kanye"},
    {"title": "Lose Yourself", "artist": "Eminem", "mood": "Energetic", "link": "https://www.youtube.com/results?search_query=Lose+Yourself+Eminem"},
    {"title": "Weightless", "artist": "Marconi Union", "mood": "Relaxed", "link": "https://www.youtube.com/results?search_query=Weightless+Marconi+Union"},
    {"title": "River Flows in You", "artist": "Yiruma", "mood": "Relaxed", "link": "https://www.youtube.com/results?search_query=River+Flows+in+You"},
    {"title": "Lo-Fi Beats", "artist": "Lofi Girl", "mood": "Relaxed", "link": "https://www.youtube.com/watch?v=jfKfPfyJRdk"},
    {"title": "Perfect", "artist": "Ed Sheeran", "mood": "Romantic", "link": "https://www.youtube.com/results?search_query=Perfect+Ed+Sheeran"},
    {"title": "All of Me", "artist": "John Legend", "mood": "Romantic", "link": "https://www.youtube.com/results?search_query=All+of+Me+John+Legend"}
]

# --- ALGORITHM SECTION ---
class MoodAnalyzer:
    """
    A simple rule-based NLP engine to detect emotions from text.
    """
    def __init__(self):
        self.keywords = {
            'Happy': ['happy', 'good', 'great', 'excited', 'joy', 'awesome', 'party', 'dance', 'fun', 'smile'],
            'Sad': ['sad', 'depressed', 'cry', 'lonely', 'heartbroken', 'down', 'upset', 'grief', 'pain', 'blue'],
            'Energetic': ['energy', 'pumped', 'workout', 'gym', 'run', 'fast', 'strong', 'power', 'fight', 'win'],
            'Relaxed': ['calm', 'chill', 'sleep', 'study', 'peace', 'quiet', 'relax', 'stress', 'breathe', 'zen'],
            'Romantic': ['love', 'date', 'crush', 'heart', 'kiss', 'romance', 'soulmate', 'beautiful', 'cute']
        }

    def analyze(self, text):
        text = text.lower()
        scores = {mood: 0 for mood in self.keywords}

        # Scoring algorithm
        for mood, words in self.keywords.items():
            for word in words:
                if word in text:
                    scores[mood] += 1
        
        # Find the highest score
        max_mood = max(scores, key=scores.get)
        
        # Return None if no keywords found
        if scores[max_mood] == 0:
            return None
        return max_mood

# --- UI SECTION ---
def main():
    st.title("🎵 VibeTunes: AI Music Recommender")
    st.markdown("### Tell us how you are feeling, and we'll pick the songs.")

    # Input Area
    user_input = st.text_input("How are you feeling right now?", placeholder="e.g., I am feeling stressed about exams but I want to keep pushing...")

    if st.button("Analyze Vibe"):
        if user_input:
            with st.spinner("Analyzing your emotional state..."):
                # Simulate processing time for effect
                time.sleep(1)
                
                analyzer = MoodAnalyzer()
                detected_mood = analyzer.analyze(user_input)

                if detected_mood:
                    st.success(f"Mood Detected: **{detected_mood}**")
                    
                    # Filter songs
                    recommendations = [song for song in SONG_DATABASE if song['mood'] == detected_mood]
                    
                    st.markdown("---")
                    st.subheader(f"Here is a {detected_mood} playlist for you:")
                    
                    for song in recommendations:
                        # Creating a nice card-like layout
                        col1, col2 = st.columns([1, 4])
                        with col1:
                            st.write("💿")
                        with col2:
                            st.markdown(f"**{song['title']}** by *{song['artist']}*")
                            st.markdown(f"[Listen on YouTube]({song['link']})")
                else:
                    st.warning("We couldn't detect a specific mood. Try using words like 'happy', 'sad', 'gym', or 'chill'.")
                    st.info("Here is a random song while you think:")
                    random_song = random.choice(SONG_DATABASE)
                    st.markdown(f"**{random_song['title']}** - [Listen]({random_song['link']})")
        else:
            st.error("Please enter some text first!")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    main()

# streamlit run "IRL PROJECTS/1.py"