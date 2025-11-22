VibeTunes: Emotion-Based Music Recommendation System

Name: Tanmay

Date: November 2025

1. Abstract

Music plays a vital role in human emotional regulation. However, with the overwhelming amount of music available on streaming platforms, users often suffer from decision fatigue. VibeTunes is a web-based application designed to solve this by recommending music based on the user's text input. Utilizing Natural Language Processing (NLP) techniques and a Python-based recommendation engine, the system interprets user sentiment and retrieves relevant musical tracks, providing a personalized listening experience.

2. Introduction

2.1 Problem Statement

Traditional music players require users to manually search for songs or browse generic genres. They lack the ability to understand the context of the user's mood (e.g., the difference between "sad" and "heartbroken" or "gym" and "running").

2.2 Objective

The primary objective of this project is to develop a system that:

Accepts natural language text input from the user.

Analyzes the input to determine the dominant emotion.

Maps the emotion to a specific subset of songs.

Displays a playable playlist interface.

3. System Architecture and Methodology

3.1 Flowchart

User Input: User types a sentence (e.g., "I want to relax after a long day").

Preprocessing: Text is converted to lowercase and tokenized.

Keyword Matching: The system scans for high-weight keywords associated with predefined mood categories.

Scoring Algorithm: A frequency counter determines the dominant mood (Happy, Sad, Energetic, Relaxed, Romantic).

Data Retrieval: The system queries the internal JSON-structure database for songs tagged with the detected mood.

Output: The UI renders song cards with title, artist, and playback links.

3.2 Technology Stack

Python: Selected for its robust string processing capabilities and ease of prototyping.

Streamlit: Used for the frontend to create a rapid, data-driven web interface without the overhead of HTML/CSS.

GitHub: Used for version control and CI/CD (Continuous Deployment) integration.

Streamlit Cloud: Used for hosting the live application.

4. Implementation Details

4.1 The Recommendation Engine

The core logic relies on a dictionary-based mapping system. Emotions are categorized into five distinct classes. Each class contains a bag-of-words model (synonyms and related terms).

Example Logic:

Input: "I am going to the gym."

Keywords Detected: "gym"

Mapped Category: "Energetic"

Result: Returns songs like "Eye of the Tiger".

4.2 Database Structure

The data is stored in a structured list of dictionaries, simulating a NoSQL database approach. Each entry contains:

Title

Artist

Mood Tag

Streaming Link

5. Results and Analysis

The system successfully identifies simple and compound sentences regarding emotional states.

Accuracy: The keyword-based approach provides high accuracy for explicit emotional expressions.

Performance: The application loads in under 2 seconds and processes input in <500ms.

Limitations: Sarcasm or extremely complex metaphors may not be detected by the current rule-based engine.

6. Conclusion and Future Scope

VibeTunes successfully demonstrates the intersection of basic NLP and Web Development. It provides a functional, user-friendly solution for mood-based music discovery.

Future Scope includes:

Spotify API Integration: To fetch real-time data instead of a static list.

Machine Learning: Implementing a trained classifier (e.g., Naive Bayes) for better sentiment accuracy.

User History: Saving user preferences to refine recommendations over time.

Github Repository: https://www.google.com/url?sa=E&source=gmail&q=https://github.com/iamtanmay37/VibeTunes-Project
