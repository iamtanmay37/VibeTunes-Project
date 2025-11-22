# Project Report: VibeTunes 

**Name:** Tanmay Tiwari


**Project:** Emotion-Based Music Recommendation System

---

## 1. Introduction
Music is something everyone enjoys, but sometimes it is difficult to decide what to listen to based on how we are feeling. Most apps just show popular songs, but they don't always match our mood. My project, "VibeTunes," is a web application that solves this problem. It asks the user how they are feeling and suggests a playlist that matches their vibe. I made a special "Desi Edition" that includes Indian artists like Seedhe Maut, Arijit Singh, and old Bollywood classics.

## 2. Problem Statement
Current music players require us to manually search for songs or skip through random playlists to find the right track. This takes time and can be annoying. There is a need for a simple system that understands basic emotions (like "Happy" or "Sad") and gives immediate song suggestions without searching.

## 3. How it Works (Methodology)
I built this project using Python because it is good for handling logic and data.

**The process is simple:**
1.  **Input:** The user can either select a mood from a dropdown menu (like Happy, Sad, Angry) or type a sentence (e.g., "I am feeling very low").
2.  **Processing:** If the user types a sentence, the code looks for specific keywords. For example, if it finds words like "gym," "power," or "run," it knows the mood is "Energetic."
3.  **Output:** The app searches through a list of songs I created. Each song is tagged with a mood. The app picks songs that match the detected mood and shows them with a YouTube link.

## 4. Implementation Details
I used the following tools to build the project:
* **Python:** For the main coding logic.
* **Streamlit:** This is a library that allowed me to create the website interface easily without writing complex HTML or CSS.
* **GitHub:** To store my code and manage versions.
* **Streamlit Cloud:** To host the website so anyone can use it.

**Key Features:**
* **Hybrid Input:** You can type your feelings or just pick from a list.
* **Desi Database:** I manually curated a list of songs that Indian students actually listen to, including Desi Hip Hop and Bollywood.

## 5. Results and Conclusion
The application works successfully. It correctly identifies the user's mood and displays the right songs. For example, selecting "Angry" shows aggressive rap songs, while "Relaxed" shows slow indie music.

This project helped me understand how to build a web app using Python and how to deploy it on the internet. It is a simple but useful tool for music lovers.

## 6. Future Scope
In the future, I plan to connect this to the Spotify API so the songs play directly in the app instead of opening YouTube. I also want to add support for Hindi typing.

---
**Live App Link:** https://vibetunes-project-qv9fbcndkevrrkyrisenmt.streamlit.app/
**GitHub Repository:** https://github.com/iamtanmay37/VibeTunes-Project
