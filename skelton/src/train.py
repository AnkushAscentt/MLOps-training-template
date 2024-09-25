import json
import logging
from logging.config import fileConfig
import os
import sys

import yaml
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV, train_test_split

sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), "utilities"))
from fetch_features import fetch_features
from wandb_utils import wandb_logging

# Initialize logging
fileConfig('../logging_config.ini')
logger = logging.getLogger(__name__)


def load_config(file_path):
    """
    Load YAML or JSON configuration file.
    """
    with open(file_path, 'r') as f:
        if file_path.endswith('.yml') or file_path.endswith('.yaml'):
            return yaml.safe_load(f)
        elif file_path.endswith('.json'):
            return json.load(f)
        else:
            raise ValueError("Invalid file extension. Only .json and .yaml/.yml are supported")


def train_model(config):
    """
    Train a Random Forest model based on the given configuration.
    """
    # Load the data
    df = fetch_features(config["feature-store"]["feature-group-name"])
    df = df.dropna()
    x = df.drop([config["model"]["target-column"], "EventTime", "CustomRecordId"], axis=1)
    y = df[config["model"]["target-column"]]

    logger.info("Features fetched successfully.")

    # Split the data
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=config["model"]["test-size"], random_state=config["model"]["random-state"]
    )

    # Hyperparameter Tuning and Model Training
    hyperparameters = load_config("/opt/ml/input/config/hyperparameters.json")
    grid_search = GridSearchCV(RandomForestClassifier(), param_grid=hyperparameters)
    grid_search.fit(x_train, y_train)

    # Best model
    best_model = grid_search.best_estimator_

    # Evaluate the model
    train_score = accuracy_score(y_train, best_model.predict(x_train))
    test_score = accuracy_score(y_test, best_model.predict(x_test))

    # Log the model to WANDB
    if config["wandb"]["enable-wandb"]:
        wandb_logging(
            config["wandb"]["entity-name"],
            config["wandb"]["project-name"],
            config["wandb"]["model-registry"],
            config["wandb"]["enable-wandb"],
            config["wandb"]["model-filename"],
            train_score,
            test_score,
            best_model,
        )
        logger.info("Model saved in WANDB Registry.")


if __name__ == "__main__":
    config = load_config("conf/tdspds-config.yml")
    train_model(config)
