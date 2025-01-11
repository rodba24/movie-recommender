# Movie Recommender

This project is a content-based movie recommendation system that helps users discover movies similar to those they already enjoy. It leverages the TMDB (The Movie Database) dataset and machine learning techniques to provide accurate recommendations based on movie content such as genres, overviews, and more.

You can try the app live on Hugging Face: [Movie Recommender](https://huggingface.co/spaces/rodba24/movie-recommender).


## How It Works
1. **Dataset**: The TMDB dataset was used for movie metadata like genres, overviews, and popularity.
2. **Data Cleaning**: Jupyter Notebook was used to preprocess, filter, and clean the dataset, ensuring accurate and relevant recommendations.
3. **Recommendation engine**: A content-based filtering algorithm computes similarity between movies using features extracted from the dataset.
4. **Pickle Files**: Precomputed similarity matrices and data are stored in `.pkl` files to speed up recommendations.  
   **Note**: Due to size limitations on GitHub, the `.pkl` files are not included in this repository. However, they are used to power the live app on Hugging Face.

## Technologies Used
- **TMDB Dataset**: The Movie Database's extensive dataset for movie metadata.
- **Jupyter Notebook**: For filtering and cleaning raw data from the TMDB dataset.
- **Streamlit**: Frontend framework for creating the web app.
- **Hugging Face Spaces**: Hosting platform for the application.

## How to Use
1. Visit the [Movie Recommender app](https://huggingface.co/spaces/rodba24/movie-recommender).
2. Enter the title of a movie you like in the search bar.
3. View a list of recommended movies based on the selected title.

## Acknowledgments
- The TMDB dataset is provided by [The Movie Database](https://www.themoviedb.org/).
