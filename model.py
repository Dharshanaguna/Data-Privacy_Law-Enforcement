import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
import pickle
import os

# Load the dataset
data = pd.read_csv("laws-97-5.csv")  # Adjust path as necessary

# Handle NaN values
data.fillna(value="", inplace=True)  # Replace NaN values with an empty string

# Split the dataset into features (X) and target variable (y)
X = data["Attribute"]
y = data["Law/Regulation"]

# Vectorize the textual data using TF-IDF
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
X = tfidf_vectorizer.fit_transform(X)

# Split the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Gradient Boosting Classifier
gb_model = GradientBoostingClassifier()

# Set up the parameter grid for GridSearchCV
param_grid = {
    'n_estimators': [100, 200],
    'learning_rate': [0.01, 0.1, 0.2],
    'max_depth': [3, 5, 7]
}

# Use GridSearchCV to find the best hyperparameters
grid_search = GridSearchCV(estimator=gb_model, param_grid=param_grid, cv=3, n_jobs=-1, verbose=2)
grid_search.fit(X_train, y_train)

# Get the best model from grid search
best_gb_model = grid_search.best_estimator_

# Train the best model
best_gb_model.fit(X_train, y_train)

# Evaluate the model
y_pred = best_gb_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy * 100)

# Print best parameters found by GridSearchCV
print("Best Parameters:", grid_search.best_params_)

# Ensure the models directory exists
os.makedirs('models', exist_ok=True)

# Save the TF-IDF vectorizer
with open('models/tfidf_vectorizer.pkl', 'wb') as file:
    pickle.dump(tfidf_vectorizer, file)

# Save the best gradient boosting model
with open('models/best_gb_model.pkl', 'wb') as file:
    pickle.dump(best_gb_model, file)

