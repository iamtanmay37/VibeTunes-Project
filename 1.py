import streamlit as st
import random
import time

st.set_page_config(
    page_title="VibeTunes",
    page_icon="🎧",
    layout="centered"
)

SONG_DATABASE = [
    {"title": "Badtameez Dil", "artist": "Ranbir Kapoor", "mood": "Happy", "lang": "Hindi", "link": "https://www.youtube.com/results?search_query=Badtameez+Dil"},
    {"title": "Gallan Goodiyaan", "artist": "Dil Dhadakne Do", "mood": "Happy", "lang": "Hindi", "link": "https://www.youtube.com/results?search_query=Gallan+Goodiyaan"},
    {"title": "London Thumakda", "artist": "Queen", "mood": "Happy", "lang": "Hindi", "link": "https://www.youtube.com/results?search_query=London+Thumakda"},
    {"title": "Kar Gayi Chull", "artist": "Kapoor & Sons", "mood": "Happy", "lang": "Hindi", "link": "https://www.youtube.com/results?search_query=Kar+Gayi+Chull"},
    {"title": "Channa Mereya", "artist": "Arijit Singh", "mood": "Sad", "lang": "Hindi", "link": "https://www.youtube.com/results?search_query=Channa+Mereya"},
    {"title": "Agar Tum Saath Ho", "artist": "Arijit Singh", "mood": "Sad", "lang": "Hindi", "link": "https://www.youtube.com/results?search_query=Agar+Tum+Saath+Ho"},
    {"title": "Tujhe Kitna Chahne Lage", "artist": "Kabir Singh", "mood": "Sad", "lang": "Hindi", "link": "https://www.youtube.com/results?search_query=Tujhe+Kitna+Chahne+Lage"},
    {"title": "Apna Time Aayega", "artist": "Gully Boy", "mood": "Energetic", "lang": "Hindi", "link": "https://www.youtube.com/results?search_query=Apna+Time+Aayega"},
    {"title": "Zinda", "artist": "Bhaag Milkha Bhaag", "mood": "Energetic", "lang": "Hindi", "link": "https://www.youtube.com/results?search_query=Zinda+Bhaag+Milkha+Bhaag"},
    {"title": "Malhari", "artist": "Bajirao Mastani", "mood": "Energetic", "lang": "Hindi", "link": "https://www.youtube.com/results?search_query=Malhari+Song"},
    {"title": "Kun Faya Kun", "artist": "Rockstar", "mood": "Relaxed", "lang": "Hindi", "link": "https://www.youtube.com/results?search_query=Kun+Faya+Kun"},
    {"title": "Iktara", "artist": "Wake Up Sid", "mood": "Relaxed", "lang": "Hindi", "link": "https://www.youtube.com/results?search_query=Iktara+Wake+Up+Sid"},
    {"title": "Raataan Lambiyan", "artist": "Shershaah", "mood": "Romantic", "lang": "Hindi", "link": "https://www.youtube.com/results?search_query=Raataan+Lambiyan"},
    {"title": "Kesariya", "artist": "Brahmastra", "mood": "Romantic", "lang": "Hindi", "link": "https://www.youtube.com/results?search_query=Kesariya+Brahmastra"},
    {"title": "Tum Se Hi", "artist": "Jab We Met", "mood": "Romantic", "lang": "Hindi", "link": "https://www.youtube.com/results?search_query=Tum+Se+Hi+Jab+We+Met"},
    {"title": "Aarambh Hai Prachand", "artist": "Piyush Mishra", "mood": "Angry", "lang": "Hindi", "link": "https://www.youtube.com/results?search_query=Aarambh+Hai+Prachand"},
    {"title": "Jungli Kutta", "artist": "Sacred Games", "mood": "Angry", "lang": "Hindi", "link": "https://www.youtube.com/results?search_query=Jungli+Kutta+Song"},

    {"title": "Bijlee Bijlee", "artist": "Harrdy Sandhu", "mood": "Happy", "lang": "Punjabi", "link": "https://www.youtube.com/results?search_query=Bijlee+Bijlee"},
    {"title": "Excuses", "artist": "AP Dhillon", "mood": "Happy", "lang": "Punjabi", "link": "https://www.youtube.com/results?search_query=Excuses+AP+Dhillon"},
    {"title": "Jadugar", "artist": "Paradox", "mood": "Happy", "lang": "Punjabi", "link": "https://www.youtube.com/results?search_query=Jadugar+Paradox"},
    {"title": "Qismat", "artist": "Ammy Virk", "mood": "Sad", "lang": "Punjabi", "link": "https://www.youtube.com/results?search_query=Qismat+Song"},
    {"title": "Mann Bharrya", "artist": "B Praak", "mood": "Sad", "lang": "Punjabi", "link": "https://www.youtube.com/results?search_query=Mann+Bharrya"},
    {"title": "Wish You Were Here", "artist": "Frappe Ash", "mood": "Sad", "lang": "Punjabi", "link": "https://www.youtube.com/results?search_query=Wish+You+Were+Here+Frappe+Ash"},
    {"title": "Namastute", "artist": "Seedhe Maut", "mood": "Energetic", "lang": "Punjabi", "link": "https://www.youtube.com/results?search_query=Namastute+Seedhe+Maut"},
    {"title": "Nanchaku", "artist": "Seedhe Maut", "mood": "Energetic", "lang": "Punjabi", "link": "https://www.youtube.com/results?search_query=Nanchaku+Seedhe+Maut"},
    {"title": "Saza-E-Maut", "artist": "KR$NA", "mood": "Energetic", "lang": "Punjabi", "link": "https://www.youtube.com/results?search_query=Saza+E+Maut+Krsna"},
    {"title": "Old Skool", "artist": "Sidhu Moose Wala", "mood": "Energetic", "lang": "Punjabi", "link": "https://www.youtube.com/results?search_query=Old+Skool+Sidhu"},
    {"title": "Lover", "artist": "Diljit Dosanjh", "mood": "Romantic", "lang": "Punjabi", "link": "https://www.youtube.com/results?search_query=Lover+Diljit"},
    {"title": "MoonChild", "artist": "Diljit Dosanjh", "mood": "Relaxed", "lang": "Punjabi", "link": "https://www.youtube.com/results?search_query=MoonChild+Diljit"},
    {"title": "Say My Name", "artist": "KR$NA", "mood": "Angry", "lang": "Punjabi", "link": "https://www.youtube.com/results?search_query=Say+My+Name+Krsna"},
    {"title": "Sheikh Chilli", "artist": "Raftaar", "mood": "Angry", "lang": "Punjabi", "link": "https://www.youtube.com/results?search_query=Sheikh+Chilli+Raftaar"},
    {"title": "Bitch I'm Back", "artist": "Sidhu Moose Wala", "mood": "Angry", "lang": "Punjabi", "link": "https://www.youtube.com/results?search_query=Bitch+Im+Back+Sidhu"},

    {"title": "Happy", "artist": "Pharrell Williams", "mood": "Happy", "lang": "English", "link": "https://www.youtube.com/results?search_query=Happy+Pharrell"},
    {"title": "Uptown Funk", "artist": "Bruno Mars", "mood": "Happy", "lang": "English", "link": "https://www.youtube.com/results?search_query=Uptown+Funk"},
    {"title": "Someone Like You", "artist": "Adele", "mood": "Sad", "lang": "English", "link": "https://www.youtube.com/results?search_query=Someone+Like+You+Adele"},
    {"title": "Fix You", "artist": "Coldplay", "mood": "Sad", "lang": "English", "link": "https://www.youtube.com/results?search_query=Fix+You+Coldplay"},
    {"title": "Eye of the Tiger", "artist": "Survivor", "mood": "Energetic", "lang": "English", "link": "https://www.youtube.com/results?search_query=Eye+of+the+Tiger"},
    {"title": "Believer", "artist": "Imagine Dragons", "mood": "Energetic", "lang": "English", "link": "https://www.youtube.com/results?search_query=Believer+Imagine+Dragons"},
    {"title": "Perfect", "artist": "Ed Sheeran", "mood": "Romantic", "lang": "English", "link": "https://www.youtube.com/results?search_query=Perfect+Ed+Sheeran"},
    {"title": "Night Changes", "artist": "One Direction", "mood": "Relaxed", "lang": "English", "link": "https://www.youtube.com/results?search_query=Night+Changes"},
    {"title": "In the End", "artist": "Linkin Park", "mood": "Angry", "lang": "English", "link": "https://www.youtube.com/results?search_query=In+the+End+Linkin+Park"},
    {"title": "Break Stuff", "artist": "Limp Bizkit", "mood": "Angry", "lang": "English", "link": "https://www.youtube.com/results?search_query=Break+Stuff+Limp+Bizkit"},

    {"title": "Kho Gaye Hum Kahan", "artist": "Prateek Kuhad", "mood": "Relaxed", "lang": "Indie", "link": "https://www.youtube.com/results?search_query=Kho+Gaye+Hum+Kahan"},
    {"title": "Kasoor", "artist": "Prateek Kuhad", "mood": "Relaxed", "lang": "Indie", "link": "https://www.youtube.com/results?search_query=Kasoor+Prateek+Kuhad"},
    {"title": "Baarishein", "artist": "Anuv Jain", "mood": "Relaxed", "lang": "Indie", "link": "https://www.youtube.com/results?search_query=Baarishein+Anuv+Jain"},
    {"title": "Mishri", "artist": "Anuv Jain", "mood": "Relaxed", "lang": "Indie", "link": "https://www.youtube.com/results?search_query=Mishri+Anuv+Jain"},
    {"title": "Waqt Ki Baatein", "artist": "Dream Note", "mood": "Sad", "lang": "Indie", "link": "https://www.youtube.com/results?search_query=Waqt+Ki+Baatein"},
    {"title": "Choo Lo", "artist": "The Local Train", "mood": "Sad", "lang": "Indie", "link": "https://www.youtube.com/results?search_query=Choo+Lo+The+Local+Train"}
]

class MoodAnalyzer:
    def __init__(self):
        self.keywords = {
            'Happy': ['happy', 'good', 'great', 'excited', 'joy', 'awesome', 'fun', 'smile', 'party', 'dance', 'mast', 'badhiya'],
            'Sad': ['sad', 'depressed', 'cry', 'lonely', 'heartbroken', 'grief', 'pain', 'blue', 'miss', 'upset', 'dukh', 'bura'],
            'Energetic': ['energy', 'pumped', 'gym', 'run', 'fast', 'power', 'win', 'workout', 'hype', 'strong', 'josh', 'hard'],
            'Relaxed': ['calm', 'chill', 'sleep', 'peace', 'quiet', 'relax', 'breathe', 'zen', 'tired', 'sukoon'],
            'Romantic': ['love', 'date', 'crush', 'heart', 'kiss', 'romance', 'beautiful', 'partner', 'pyar', 'ishq'],
            'Angry': ['angry', 'mad', 'furious', 'hate', 'rage', 'annoyed', 'irritated', 'fight', 'mood off', 'gussa']
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
    st.title("🎧 VibeTunes: Ultimate Edition")
    st.markdown("### The smartest way to find music.")
    st.markdown("---")

    st.subheader("Step 1: What do you want to listen to?")
    genre_filter = st.radio(
        "Select Language / Style:",
        ["Hindi (Bollywood)", "Punjabi / DHH", "English (Pop/Rock)", "Indie (Chill)", "All Languages"],
        horizontal=True
    )

    lang_map = {
        "Hindi (Bollywood)": "Hindi",
        "Punjabi / DHH": "Punjabi",
        "English (Pop/Rock)": "English",
        "Indie (Chill)": "Indie",
        "All Languages": "All"
    }
    selected_lang = lang_map[genre_filter]

    st.markdown("---")

    st.subheader("Step 2: How are you feeling?")
    
    col1, col2 = st.columns(2)
    with col1:
        selected_mood = st.selectbox("Select Mood:", ["Select...", "Happy", "Sad", "Energetic", "Relaxed", "Romantic", "Angry"])
    with col2:
        user_text = st.text_input("OR Describe it:", placeholder="e.g., I am feeling heartbroken...")

    if st.button("Get Recommendations"):
        final_mood = None
        
        if selected_mood != "Select...":
            final_mood = selected_mood
        elif user_text:
            with st.spinner("Analyzing vibes..."):
                time.sleep(0.5)
                analyzer = MoodAnalyzer()
                final_mood = analyzer.analyze(user_text)
        
        if final_mood:
            mood_songs = [song for song in SONG_DATABASE if song['mood'] == final_mood]
            
            if selected_lang != "All":
                final_recommendations = [song for song in mood_songs if song['lang'] == selected_lang]
            else:
                final_recommendations = mood_songs
            
            if final_recommendations:
                st.success(f"Found {len(final_recommendations)} {selected_lang if selected_lang != 'All' else ''} songs for a **{final_mood}** vibe!")
                st.markdown("---")
                
                display_songs = random.sample(final_recommendations, min(len(final_recommendations), 10))
                
                for song in display_songs:
                    with st.container():
                        c1, c2 = st.columns([1, 10])
                        with c1:
                            st.write("🎵")
                        with c2:
                            st.markdown(f"**{song['title']}** — {song['artist']}")
                            st.caption(f"Genre: {song['lang']} | Mood: {song['mood']}")
                            st.markdown(f"[▶ Play on YouTube]({song['link']})")
                            st.divider()
            else:
                st.warning(f"Oops! We don't have any **{selected_lang}** songs for a **{final_mood}** vibe yet. Try choosing 'All Languages'!")
        else:
            st.error("Please select a mood or type how you feel!")

if __name__ == "__main__":
    main()
