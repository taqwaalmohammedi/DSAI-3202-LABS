from sklearn.ensemble import RandomForestClassifier

def train_model(X_train, y_train):
    """
    Trains a RandomForestClassifier on the given training data.

    Args:
        X_train (pandas.DataFrame): The training features.
        y_train (pandas.Series): The training labels.

    Returns:
        RandomForestClassifier: The trained model.
    """
    model = RandomForestClassifier(random_state=42)  # Initializes the model
    model.fit(X_train, y_train)  # Trains the model
    return model  # Returns the trained model
