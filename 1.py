import streamlit as st
import random
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="VibeTunes - Desi Edition",
    page_icon="🎵",
    layout="centered"
)

# --- MOCK DATA DATABASE (Indian/DHH Edition) ---
SONG_DATABASE = [
    # --- HAPPY (Bollywood Dance & Upbeat) ---
    {"title": "Jadugar", "artist": "Paradox", "mood": "Happy", "link": "https://www.youtube.com/results?search_query=Jadugar+Paradox"},
    {"title": "Badtameez Dil", "artist": "Ranbir Kapoor (YJHD)", "mood": "Happy", "link": "https://www.youtube.com/results?search_query=Badtameez+Dil"},
    {"title": "Gallan Goodiyaan", "artist": "Dil Dhadakne Do", "mood": "Happy", "link": "https://www.youtube.com/results?search_query=Gallan+Goodiyaan"},
    {"title": "London Thumakda", "artist": "Queen", "mood": "Happy", "link": "https://www.youtube.com/results?search_query=London+Thumakda"},
    {"title": "Coca Cola", "artist": "Luka Chuppi", "mood": "Happy", "link": "https://www.youtube.com/results?search_query=Coca+Cola+Song"},
    {"title": "Param Sundari", "artist": "Mimi (A.R. Rahman)", "mood": "Happy", "link": "https://www.youtube.com/results?search_query=Param+Sundari"},
    {"title": "Kar Gayi Chull", "artist": "Kapoor & Sons", "mood": "Happy", "link": "https://www.youtube.com/results?search_query=Kar+Gayi+Chull"},
    {"title": "Bijlee Bijlee", "artist": "Harrdy Sandhu", "mood": "Happy", "link": "https://www.youtube.com/results?search_query=Bijlee+Bijlee"},

    # --- SAD (Heartbreak & Melancholy) ---
    {"title": "Channa Mereya", "artist": "Arijit Singh", "mood": "Sad", "link": "https://www.youtube.com/results?search_query=Channa+Mereya"},
    {"title": "Agar Tum Saath Ho", "artist": "Tamasha", "mood": "Sad", "link": "https://www.youtube.com/results?search_query=Agar+Tum+Saath+Ho"},
    {"title": "Apna Bana Le", "artist": "Bhediya (Arijit Singh)", "mood": "Sad", "link": "https://www.youtube.com/results?search_query=Apna+Bana+Le"},
    {"title": "Wish You Were Here", "artist": "Frappe Ash (DHH)", "mood": "Sad", "link": "https://www.youtube.com/results?search_query=Wish+You+Were+Here+Frappe+Ash"},
    {"title": "Luka Chuppi", "artist": "Rang De Basanti", "mood": "Sad", "link": "https://www.youtube.com/results?search_query=Luka+Chuppi+Rang+De+Basanti"},
    {"title": "Main Dhoondne Ko Zamaane", "artist": "Arijit Singh", "mood": "Sad", "link": "https://www.youtube.com/results?search_query=Main+Dhoondne+Ko+Zamaane"},
    {"title": "Kabira", "artist": "Yeh Jawaani Hai Deewani", "mood": "Sad", "link": "https://www.youtube.com/results?search_query=Kabira+Song"},

    # --- ENERGETIC (DHH Rap & Gym Mode) ---
    {"title": "Namastute", "artist": "Seedhe Maut", "mood": "Energetic", "link": "https://www.youtube.com/results?search_query=Namastute+Seedhe+Maut"},
    {"title": "Nanchaku", "artist": "Seedhe Maut ft. MC Stan", "mood": "Energetic", "link": "https://www.youtube.com/results?search_query=Nanchaku+Seedhe+Maut"},
    {"title": "Saza-E-Maut", "artist": "KR$NA ft. Raftaar", "mood": "Energetic", "link": "https://www.youtube.com/results?search_query=Saza+E+Maut+Krsna"},
    {"title": "Apna Time Aayega", "artist": "Gully Boy", "mood": "Energetic", "link": "https://www.youtube.com/results?search_query=Apna+Time+Aayega"},
    {"title": "Babam Bam", "artist": "Paradox (Hustle)", "mood": "Energetic", "link": "https://www.youtube.com/results?search_query=Babam+Bam+Paradox"},
    {"title": "Sher Aaya Sher", "artist": "Divine", "mood": "Energetic", "link": "https://www.youtube.com/results?search_query=Sher+Aaya+Sher"},
    {"title": "Hola Amigo", "artist": "KR$NA x Seedhe Maut", "mood": "Energetic", "link": "https://www.youtube.com/results?search_query=Hola+Amigo+Krsna"},

    # --- RELAXED (Old Bollywood, Indie, Lo-fi) ---
    {"title": "Kho Gaye Hum Kahan", "artist": "Prateek Kuhad", "mood": "Relaxed", "link": "https://www.youtube.com/results?search_query=Kho+Gaye+Hum+Kahan"},
    {"title": "Iktara", "artist": "Wake Up Sid", "mood": "Relaxed", "link": "https://www.youtube.com/results?search_query=Iktara+Wake+Up+Sid"},
    {"title": "Kun Faya Kun", "artist": "Rockstar", "mood": "Relaxed", "link": "https://www.youtube.com/results?search_query=Kun+Faya+Kun"},
    {"title": "Lag Jaa Gale", "artist": "Lata Mangeshkar (Classic)", "mood": "Relaxed", "link": "https://www.youtube.com/results?search_query=Lag+Jaa+Gale"},
    {"title": "Kasoor", "artist": "Prateek Kuhad", "mood": "Relaxed", "link": "https://www.youtube.com/results?search_query=Kasoor+Prateek+Kuhad"},
    {"title": "Sham", "artist": "Aisha (Amit Trivedi)", "mood": "Relaxed", "link": "https://www.youtube.com/results?search_query=Sham+Aisha"},
    {"title": "Baarishein", "artist": "Anuv Jain", "mood": "Relaxed", "link": "https://www.youtube.com/results?search_query=Baarishein+Anuv+Jain"},

    # --- ROMANTIC (Love Songs) ---
    {"title": "Maan Meri Jaan", "artist": "King", "mood": "Romantic", "link": "https://www.youtube.com/results?search_query=Maan+Meri+Jaan+King"},
    {"title": "Raataan Lambiyan", "artist": "Shershaah", "mood": "Romantic", "link": "https://www.youtube.com/results?search_query=Raataan+Lambiyan"},
    {"title": "Kesariya", "artist": "Brahmastra (Arijit Singh)", "mood": "Romantic", "link": "https://www.youtube.com/results?search_query=Kesariya+Brahmastra"},
    {"title": "Tum Se Hi", "artist": "Jab We Met", "mood": "Romantic", "link": "https://www.youtube.com/results?search_query=Tum+Se+Hi+Jab+We+Met"},
    {"title": "Pehla Nasha", "artist": "Jo Jeeta Wohi Sikandar", "mood": "Romantic", "link": "https://www.youtube.com/results?search_query=Pehla+Nasha"},
    {"title": "Tera Hone Laga Hoon", "artist": "Atif Aslam", "mood": "Romantic", "link": "https://www.youtube.com/results?search_query=Tera+Hone+Laga+Hoon"},
    {"title": "Apna Bana Le", "artist": "Bhediya", "mood": "Romantic", "link": "https://www.youtube.com/results?search_query=Apna+Bana+Le"},

    # --- ANGRY (Aggressive Rap & Rock) ---
    {"title": "Say My Name", "artist": "KR$NA", "mood": "Angry", "link": "https://www.youtube.com/results?search_query=Say+My+Name+Krsna"},
    {"title": "Sheikh Chilli", "artist": "Raftaar", "mood": "Angry", "link": "https://www.youtube.com/results?search_query=Sheikh+Chilli+Raftaar"},
    {"title": "Ghatotkach", "artist": "Paradox", "mood": "Angry", "link": "https://www.youtube.com/results?search_query=Ghatotkach+Paradox"},
    {"title": "Jungli Kutta", "artist": "Sacred Games", "mood": "Angry", "link": "https://www.youtube.com/results?search_query=Jungli+Kutta+Song"},
    {"title": "Bitch I'm Back", "artist": "Sidhu Moose Wala", "mood": "Angry", "link": "https://www.youtube.com/results?search_query=Bitch+Im+Back+Sidhu"},
    {"title": "Aarambh Hai Prachand", "artist": "Piyush Mishra", "mood": "Angry", "link": "https://www.youtube.com/results?search_query=Aarambh+Hai+Prachand"},
    {"title": "Khatam", "artist": "Emiway Bantai", "mood": "Angry", "link": "https://www.youtube.com/results?search_query=Khatam+Emiway"}
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
    st.title("🎵 VibeTunes: Desi Edition")
    st.write("From **Bollywood Classics** to **Seedhe Maut**, we got you.")
    
    # --- CLEAN UNIFIED UI ---
    st.subheader("How are you feeling today?")
    st.write("Select a mood from the dropdown **OR** describe it in the box below.")

    # Layout: Dropdown first, then text input (No "Option 1" labels)
    selected_mood = st.selectbox("Select Vibe:", ["Select...", "Happy", "Sad", "Energetic", "Relaxed", "Romantic", "Angry"])
    
    st.markdown("**— OR —**")
    
    user_text = st.text_input("Describe it in your own words:", placeholder="e.g., I need some hardcore rap for the gym...")

    if st.button("Play Music"):
        final_mood = None
        
        # Logic: Priority given to Dropdown. If Dropdown is "Select...", check text.
        if selected_mood != "Select...":
            final_mood = selected_mood
        elif user_text:
            with st.spinner("Scanning vibes..."):
                time.sleep(1)
                analyzer = MoodAnalyzer()
                final_mood = analyzer.analyze(user_text)
        
        # Display Results
        if final_mood:
            st.success(f"Vibe Detected: **{final_mood}**")
            recommendations = [song for song in SONG_DATABASE if song['mood'] == final_mood]
            
            if recommendations:
                st.markdown("---")
                st.markdown(f"### 🎧 {final_mood} Playlist")
                # Show 5 random songs to keep it fresh every time
                display_songs = random.sample(recommendations, min(len(recommendations), 5))
                
                for song in display_songs:
                    col1, col2 = st.columns([1, 4])
                    with col1:
                        st.write("💿")
                    with col2:
                        st.markdown(f"**{song['title']}** — *{song['artist']}*")
                        st.markdown(f"[▶ Listen on YouTube]({song['link']})")
            else:
                st.warning("No songs found for this mood yet!")
        else:
            st.error("Please select a mood or type something!")

if __name__ == "__main__":
    main()
