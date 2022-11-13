# train.py

import argparse
import sys

import numpy as np
from sklearn.linear_model import LogisticRegression

import mlflow

from mlflow import log_metric, log_param, log_artifacts

if __name__ == "__main__":
    X = np.array([-2, -1, 0, 1, 2, 1]).reshape(-1, 1)
    y = np.array([0, 0, 1, 1, 1, 0])

    lr = LogisticRegression(solver=sys.argv[1], penalty=sys.argv[2], l1_ratio=float(sys.argv[3]))

    with mlflow.start_run() as run:
        lr.fit(X, y)

    log_param("solver", sys.argv[1])
    log_param("penalty", sys.argv[2])
    log_param("l1_ratio", sys.argv[3])

    score = float(lr.score(X, y))
    log_metric("score", score)
    print("Score: %s" % score)
   
