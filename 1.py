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
SONG_DATABASE = [
    {"title": "Happy", "artist": "Pharrell Williams", "mood": "Happy", "link": "https://www.youtube.com/results?search_query=Happy+Pharrell"},
    {"title": "Can't Stop the Feeling!", "artist": "Justin Timberlake", "mood": "Happy", "link": "https://www.youtube.com/results?search_query=Cant+Stop+the+Feeling"},
    {"title": "Uptown Funk", "artist": "Bruno Mars", "mood": "Happy", "link": "https://www.youtube.com/results?search_query=Uptown+Funk"},
    {"title": "Someone Like You", "artist": "Adele", "mood": "Sad", "link": "https://www.youtube.com/results?search_query=Someone+Like+You+Adele"},
    {"title": "Fix You", "artist": "Coldplay", "mood": "Sad", "link": "https://www.youtube.com/results?search_query=Fix+You+Coldplay"},
    {"title": "The Night We Met", "artist": "Lord Huron", "mood": "Sad", "link": "https://www.youtube.com/results?search_query=The+Night+We+Met"},
    {"title": "Eye of the Tiger", "artist": "Survivor", "mood": "Energetic", "link": "https://www.youtube.com/results?search_query=Eye+of+the+Tiger"},
    {"title": "Stronger", "artist": "Kanye West", "mood": "Energetic", "link": "https://www.youtube.com/results?search_query=Stronger+Kanye"},
    {"title": "Believer", "artist": "Imagine Dragons", "mood": "Energetic", "link": "https://www.youtube.com/results?search_query=Believer+Imagine+Dragons"},
    {"title": "Weightless", "artist": "Marconi Union", "mood": "Relaxed", "link": "https://www.youtube.com/results?search_query=Weightless+Marconi+Union"},
    {"title": "River Flows in You", "artist": "Yiruma", "mood": "Relaxed", "link": "https://www.youtube.com/results?search_query=River+Flows+in+You"},
    {"title": "Perfect", "artist": "Ed Sheeran", "mood": "Romantic", "link": "https://www.youtube.com/results?search_query=Perfect+Ed+Sheeran"},
    {"title": "All of Me", "artist": "John Legend", "mood": "Romantic", "link": "https://www.youtube.com/results?search_query=All+of+Me+John+Legend"},
    # NEW ANGRY SONGS
    {"title": "In the End", "artist": "Linkin Park", "mood": "Angry", "link": "https://www.youtube.com/results?search_query=In+the+End+Linkin+Park"},
    {"title": "Break Stuff", "artist": "Limp Bizkit", "mood": "Angry", "link": "https://www.youtube.com/results?search_query=Break+Stuff+Limp+Bizkit"},
    {"title": "Killing in the Name", "artist": "Rage Against the Machine", "mood": "Angry", "link": "https://www.youtube.com/results?search_query=Killing+in+the+Name"}
]

class MoodAnalyzer:
    def __init__(self):
        self.keywords = {
            'Happy': ['happy', 'good', 'great', 'excited', 'joy', 'awesome', 'fun', 'smile'],
            'Sad': ['sad', 'depressed', 'cry', 'lonely', 'heartbroken', 'grief', 'pain', 'blue'],
            'Energetic': ['energy', 'pumped', 'gym', 'run', 'fast', 'power', 'win', 'workout'],
            'Relaxed': ['calm', 'chill', 'sleep', 'peace', 'quiet', 'relax', 'breathe', 'zen'],
            'Romantic': ['love', 'date', 'crush', 'heart', 'kiss', 'romance', 'beautiful'],
            'Angry': ['angry', 'mad', 'furious', 'hate', 'rage', 'annoyed', 'irritated']
        }

    def analyze(self, text):
        text = text.lower()
        scores = {mood: 0 for mood in self.keywords}
        for mood, words in self.keywords.items():
            for word in words:
                if word in text:
                    scores[mood] += 1
        max_mood = max(scores, key=scores.get)
        if scores[max_mood] == 0:
            return None
        return max_mood

def main():
    st.title("🎵 VibeTunes: AI Music Recommender")
    st.write("Select your mood from the list, OR type how you feel!")

    # --- INPUT METHOD 1: DROPDOWN (The easy way) ---
    st.subheader("Option 1: Select Mood")
    selected_mood = st.selectbox("Choose a Vibe:", ["Select...", "Happy", "Sad", "Energetic", "Relaxed", "Romantic", "Angry"])

    # --- INPUT METHOD 2: TEXT (The AI way) ---
    st.subheader("Option 2: Type it out")
    user_text = st.text_input("Or tell us how you feel:", placeholder="e.g., I am so furious right now!")

    if st.button("Find Songs"):
        final_mood = None
        
        # Logic: Check Dropdown first, then check Text
        if selected_mood != "Select...":
            final_mood = selected_mood
        elif user_text:
            with st.spinner("Analyzing text..."):
                time.sleep(1)
                analyzer = MoodAnalyzer()
                final_mood = analyzer.analyze(user_text)
        
        # Display Results
        if final_mood:
            st.success(f"Vibe Detected: **{final_mood}**")
            recommendations = [song for song in SONG_DATABASE if song['mood'] == final_mood]
            
            if recommendations:
                st.markdown("---")
                for song in recommendations:
                    col1, col2 = st.columns([1, 4])
                    with col1:
                        st.write("💿")
                    with col2:
                        st.markdown(f"**{song['title']}** - {song['artist']}")
                        st.markdown(f"[▶ Listen on YouTube]({song['link']})")
            else:
                st.warning("No songs found for this specific mood yet!")
        else:
            st.error("Please select a mood or type a sentence with emotion keywords!")

if __name__ == "__main__":
    main()
