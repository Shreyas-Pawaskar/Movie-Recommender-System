
# 🎬 Movie Recommender System

This project is a **Movie Recommender System** built with **Streamlit** that suggests movies based on user preferences. It uses a content-based filtering approach and recommends movies similar to the one selected by the user.

## 📋 Features

- **Movie Selection**: Choose from a wide list of movies using a dropdown menu.
- **Recommendations**: Get top 5 similar movie recommendations based on your selection.
- **Poster Display**: View movie posters for a more visual experience.
- **User Interface**: A professional and user-friendly interface with a custom design.
- **Image Carousel**: An interactive image carousel showcasing popular movies.

## 🛠️ Technologies Used

- **Python**: The core programming language for this project.
- **Streamlit**: For building the web app interface.
- **TMDB API**: To fetch movie posters and other related information.
- **Pickle**: To load pre-trained models and movie data.

## 📦 Setup and Installation

1. **Clone the repository**:
    \`\`\`bash
    git clone https://github.com/your-username/movie-recommender-system.git
    cd movie-recommender-system
    \`\`\`

2. **Install the required packages**:
    \`\`\`bash
    pip install -r requirements.txt
    \`\`\`

3. **Run the Streamlit app**:
    \`\`\`bash
    streamlit run app.py
    \`\`\`

4. **Navigate to the app**:
    Open your browser and go to `http://localhost:8501`.

## 🗂️ Project Structure

- `app.py`: The main script for running the Streamlit app.
- `movies_list.pkl`: Pickle file containing movie data.
- `similarity.pkl`: Pickle file containing the similarity matrix for movie recommendations.
- `frontend/public`: Directory containing the frontend components for the image carousel.

## 🎨 Customization

The app appearance has been customized with CSS for a professional look. You can further modify the `st.markdown` section in `app.py` to change colors, fonts, and other styling elements.

## 🌐 API Usage

This project uses the **TMDB API** to fetch movie posters. Ensure you have a valid API key, and replace the placeholder in the `fetch_poster` function with your key:

\`\`\`python
api_key = 'your_tmdb_api_key_here'
\`\`\`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

Thank you for using the Movie Recommender System! If you found this project useful, please give it a ⭐ on GitHub.
