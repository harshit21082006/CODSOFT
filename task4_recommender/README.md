# Task 4: Recommendation System

## Objective
Build a simple hybrid recommender system using MovieLens dataset.

## Approach
- Collaborative filtering + content-based hybrid model
- Python with pandas, scikit-learn, surprise library

## How to Run
1. Install requirements: `pip install -r requirements.txt`
2. Run preprocessing: `python preprocess.py`
3. Run model: `python model.py`
4. Optional UI: `streamlit run app.py`

## Dataset
- MovieLens 100K / 1M
- Provide download instructions

## Results
- Top-K movie recommendations for user
- Evaluation: RMSE, precision@k

## Future Improvements
- Use deep learning embeddings
- Add more metrics
