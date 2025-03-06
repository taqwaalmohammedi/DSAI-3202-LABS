from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import concurrent.futures

# Function to train a model
def train_model(model, X_train, y_train):
    model.fit(X_train, y_train)
    return model

# Function to train all models in parallel
def train_all_models(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    models = {
        "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
        "SVM": SVC(kernel='linear', random_state=42),
        "KNN": KNeighborsClassifier(n_neighbors=5)
    }

    trained_models = {}
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = {executor.submit(train_model, model, X_train, y_train): name for name, model in models.items()}
        for future in concurrent.futures.as_completed(futures):
            name = futures[future]
            trained_models[name] = future.result()
            print(f"{name} model trained successfully!")

    return trained_models, X_test, y_test
