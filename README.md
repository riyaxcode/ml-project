🎬 Movie Recommender System
A content-based movie recommendation engine built with Python and Streamlit. This application suggests movies similar to your favorites by analyzing movie metadata and provides an interactive, easy-to-use web interface.

✨ Features
Smart Recommendations: Uses machine learning (content-based filtering) to suggest 5 similar movies based on the user's selection.

Rich Movie Data: Integrates with the TMDB (The Movie Database) API to fetch high-quality movie posters and details in real-time.

Interactive UI: A clean, responsive, and user-friendly web interface built entirely with Streamlit.

Fast Processing: Efficient data handling and similarity calculations using Python libraries.

🛠️ Tech Stack
Language: Python

Frontend/Framework: Streamlit

API: TMDB (The Movie Database) API

Data Processing: Pandas, Scikit-Learn (for CountVectorizer & Cosine Similarity), NumPy

🧠 How It Works
Data Preprocessing: The system processes a dataset of movies, extracting key features like genres, keywords, cast, and crew.

Vectorization: Text data is converted into vectors using techniques like CountVectorizer.

Similarity Score: The engine calculates the Cosine Similarity between movie vectors to find the closest matches.

API Integration: When a user selects a movie, the app retrieves the top 5 most similar movies and fetches their official posters via the TMDB API to display on the frontend.

🚀 Installation and Setup
Follow these steps to run the project on your local machine.

Prerequisites
Make sure you have Python installed on your system. You will also need a TMDB API key.

Go to TMDB and create an account.

Navigate to your account settings and generate an API key.

Steps to Run
1. Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2. Create a virtual environment (Recommended)
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Add your API Key
Open the main Python file (e.g., app.py) and replace the placeholder API key with your actual TMDB API key where the fetch function is defined.

5. Run the Streamlit app
streamlit run app.py

📂 Project Structure
Plaintext
├── app.py                 # Main Streamlit application code
├── recommender.ipynb      # Jupyter Notebook with data preprocessing and model creation
├── movies_dict.pkl        # Pickled dictionary containing movie data 
├── similarity.pkl         # Pickled similarity matrix
├── requirements.txt       # List of required Python packages
└── README.md              # Project documentation
(Note: Due to GitHub file size limits, you may need to generate similarity.pkl locally by running the Jupyter notebook rather than uploading it directly.)
