import streamlit as st
import random
import time

st.set_page_config(
    page_title="VibeTunes - Desi Edition",
    page_icon="🎵",
    layout="centered"
)

INDIAN_SONGS = [
    {"title": "Jadugar", "artist": "Paradox", "mood": "Happy", "link": "https://www.youtube.com/results?search_query=Jadugar+Paradox"},
    # Add all other songs from your original SONG_DATABASE here
]

class MoodDetector:
    def __init__(self):
        self.mood_words = {
            'Happy': ['happy', 'good', 'great', 'excited', 'joy', 'awesome', 'fun', 'smile', 'party', 'dance', 'mast', 'badhiya'],
            'Sad': ['sad', 'depressed', 'cry', 'lonely', 'heartbroken', 'grief', 'pain', 'blue', 'miss', 'upset', 'dukh', 'bura'],
            'Energetic': ['energy', 'pumped', 'gym', 'run', 'fast', 'power', 'win', 'workout', 'hype', 'strong', 'josh', 'hard'],
            'Relaxed': ['calm', 'chill', 'sleep', 'peace', 'quiet', 'relax', 'breathe', 'zen', 'tired', 'sukoon'],
            'Romantic': ['love', 'date', 'crush', 'heart', 'kiss', 'romance', 'beautiful', 'partner', 'pyar', 'ishq'],
            'Angry': ['angry', 'mad', 'furious', 'hate', 'rage', 'annoyed', 'irritated', 'fight', 'mood off', 'gussa']
        }

    def detect(self, user_input):
        text = user_input.lower()
        match_scores = {mood: 0 for mood in self.mood_words}
        for mood, keywords in self.mood_words.items():
            for word in keywords:
                if word in text:
                    match_scores[mood] += 1
        best_mood = max(match_scores, key=match_scores.get)
        if match_scores[best_mood] == 0:
            return None
        return best_mood

def vibe_recommender():
    st.title("🎵 VibeTunes: Desi Edition")
    st.subheader("How are you feeling today?")
    st.write("Pick your vibe from the dropdown, or describe how you're feeling.")

    mood_choice = st.selectbox("Choose your vibe:", ["Select...", "Happy", "Sad", "Energetic", "Relaxed", "Romantic", "Angry"])
    st.markdown("**— OR —**")
    mood_text = st.text_input("Describe your mood:", placeholder="e.g., Feeling energetic for a gym session!")

    if st.button("Play Music"):
        chosen_mood = None
        if mood_choice != "Select...":
            chosen_mood = mood_choice
        elif mood_text:
            with st.spinner("Matching your vibe..."):
                time.sleep(1)
                detector = MoodDetector()
                chosen_mood = detector.detect(mood_text)

        if chosen_mood:
            st.success(f"Detected Mood: **{chosen_mood}**")
            playlist = [song for song in INDIAN_SONGS if song['mood'] == chosen_mood]
            if playlist:
                st.markdown("---")
                st.markdown(f"### 🎧 {chosen_mood} Playlist")
                song_choices = random.sample(playlist, min(len(playlist), 5))
                for track in song_choices:
                    col1, col2 = st.columns([1, 4])
                    with col1:
                        st.write("💿")
                    with col2:
                        st.markdown(f"**{track['title']}** — *{track['artist']}*")
                        st.markdown(f"[▶ Listen on YouTube]({track['link']})")
            else:
                st.warning("Sorry, couldn’t find songs for this vibe yet!")
        else:
            st.error("Please pick a mood or describe it!")

if __name__ == "__main__":
    vibe_recommender()
# streamlit run "IRL PROJECTS/1.py"