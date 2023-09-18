import pandas as pd

import sklearn
from sklearn.metrics import mean_squared_error, mean_absolute_error, accuracy_score, f1_score
    

def print_regressor_scores(y_preds, y_actuals, set_name=None):
    """Print the RMSE and MAE for the provided data

    Parameters
    ----------
    y_preds : Numpy Array
        Predicted target
    y_actuals : Numpy Array
        Actual target
    set_name : str
        Name of the set to be printed

    Returns
    -------
    """
    rmse = mean_squared_error(y_actuals, y_preds, squared=False)
    mae = mean_absolute_error(y_actuals, y_preds)
    print(f"RMSE {set_name}: {rmse}")
    print(f"MAE {set_name}: {mae}")

    return rmse, mae


def assess_regressor_set(model: sklearn.base.BaseEstimator,
                         features, target, set_name=''):
    """Save the predictions from a trained model on a given set and print its RMSE and MAE scores

    Parameters
    ----------
    model: sklearn.base.BaseEstimator
        Trained Sklearn model with set hyperparameters
    features : Numpy Array
        Features
    target : Numpy Array
        Target variable
    set_name : str
        Name of the set to be printed

    Returns
    -------
    """
    preds = model.predict(features)
    return print_regressor_scores(y_preds=preds, y_actuals=target, set_name=set_name)


def fit_assess_regressor(model: sklearn.base.BaseEstimator,
                         X_train, y_train, X_val, y_val):
    """Train a regressor model, print its RMSE and MAE scores on the training and validation set and return the trained model

    Parameters
    ----------
    model: sklearn.base.BaseEstimator
        Instantiated Sklearn model with set hyperparameters
    X_train : Numpy Array
        Features for the training set
    y_train : Numpy Array
        Target for the training set
    X_train : Numpy Array
        Features for the validation set
    y_train : Numpy Array
        Target for the validation set

    Returns
    sklearn.base.BaseEstimator
        Trained model
    -------
    """
    model.fit(X_train, y_train)
    train_rmse, train_mae = assess_regressor_set(model, X_train, y_train, set_name='Training')
    val_rmse, val_mae = assess_regressor_set(model, X_val, y_val, set_name='Validation')
    return {"model": model,
            "train_rmse": train_rmse,
            "train_mae": train_mae,
            "val_rmse": val_rmse,
            "val_mae": val_mae}


def print_classifier_scores(y_preds, y_actuals, set_name=None):
    """Print the Accuracy and F1 score for the provided data.
    The value of the 'average' parameter for F1 score will be determined according to the number of distinct values of the target variable: 'binary' for bianry classification' or 'weighted' for multi-classs classification

    Parameters
    ----------
    y_preds : Numpy Array
        Predicted target
    y_actuals : Numpy Array
        Actual target
    set_name : str
        Name of the set to be printed
    Returns
    -------
    """
    average = 'weighted' if pd.Series(y_actuals).nunique() > 2 else 'binary'

    print(f"Accuracy {set_name}: {accuracy_score(y_actuals, y_preds)}")
    print(f"F1 {set_name}: {f1_score(y_actuals, y_preds, average=average)}")


def assess_classifier_set(model: sklearn.base.BaseEstimator,
                          features, target, set_name=''):
    """Save the predictions from a trained model on a given set and print its accuracy and F1 scores

    Parameters
    ----------
    model: sklearn.base.BaseEstimator
        Trained Sklearn model with set hyperparameters
    features : Numpy Array
        Features
    target : Numpy Array
        Target variable
    set_name : str
        Name of the set to be printed

    Returns
    -------
    """
    preds = model.predict(features)
    print_classifier_scores(y_preds=preds, y_actuals=target, set_name=set_name)


def fit_assess_classifier(model: sklearn.base.BaseEstimator,
                          X_train, y_train, X_val, y_val):
    """Train a classifier model, print its accuracy and F1 scores on the training and validation set and return the trained model

    Parameters
    ----------
    model: sklearn.base.BaseEstimator
        Instantiated Sklearn model with set hyperparameters
    X_train : Numpy Array
        Features for the training set
    y_train : Numpy Array
        Target for the training set
    X_train : Numpy Array
        Features for the validation set
    y_train : Numpy Array
        Target for the validation set

    Returns
    sklearn.base.BaseEstimator
        Trained model
    -------
    """
    model.fit(X_train, y_train)
    assess_classifier_set(model, X_train, y_train, set_name='Training')
    assess_classifier_set(model, X_val, y_val, set_name='Validation')
    return model
