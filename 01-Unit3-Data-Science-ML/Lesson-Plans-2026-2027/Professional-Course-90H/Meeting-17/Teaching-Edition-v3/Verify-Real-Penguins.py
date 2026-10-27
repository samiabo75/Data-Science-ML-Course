# Teacher-only reproducibility check for Meeting 17 (not a student lab solution)
# Usage from repository root:
#   python 01-Unit3-Data-Science-ML/Lesson-Plans-2026-2027/Professional-Course-90H/Meeting-17/Teaching-Edition-v3/Verify-Real-Penguins.py
# Or:
#   python Verify-Real-Penguins.py --csv /path/to/penguins.csv
# Verified with pandas 2.2.3, numpy 2.3.5, scikit-learn 1.8.0.

from argparse import ArgumentParser
from io import BytesIO
from pathlib import Path
import hashlib
import urllib.request

import numpy as np
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

RAW_URL = "https://raw.githubusercontent.com/samiabo75/Data-Science-ML-Course/main/Datasets/penguins.csv"
EXPECTED_GIT_BLOB_SHA1 = "b5093336d83d99d8835c606b455d00065ab7cdcf"

def load_verified_csv(csv_path):
    path = Path(csv_path)
    if path.is_file():
        content = path.read_bytes()
        origin = str(path)
    else:
        # In Colab, when the repository has not been cloned, download RAW CSV.
        with urllib.request.urlopen(RAW_URL, timeout=20) as response:
            content = response.read()
        origin = RAW_URL

    # Git blob ID includes the "blob SIZE\0" prefix; this is not plain SHA-1.
    header = ("blob " + str(len(content)) + "\0").encode("utf-8")
    actual_git_sha = hashlib.sha1(header + content).hexdigest()
    if actual_git_sha != EXPECTED_GIT_BLOB_SHA1:
        raise AssertionError(
            "Dataset version does not match the verified course CSV. "
            + "Expected " + EXPECTED_GIT_BLOB_SHA1 + ", got " + actual_git_sha
        )
    df = pd.read_csv(BytesIO(content))
    assert df.shape == (344, 7)
    assert df["species"].isna().sum() == 0
    print("CSV verified:", origin, "| git blob:", actual_git_sha)
    return df

def run_one_path(df, features, seed):
    source_copy = df.copy(deep=True)
    model_df = df.dropna(subset=["species"]).copy()
    X = model_df[features].copy()
    y = model_df["species"].copy()

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=seed, stratify=y
    )
    assert X_train.shape == (258, 2)
    assert X_test.shape == (86, 2)
    assert X_train.index.equals(y_train.index)
    assert X_test.index.equals(y_test.index)

    # Learn all imputation parameters from Train only.
    train_means = X_train.mean()
    X_train_ready = X_train.fillna(train_means)
    X_test_ready = X_test.fillna(train_means)

    scaler = StandardScaler().set_output(transform="pandas")
    scaler.fit(X_train_ready)
    X_train_scaled = scaler.transform(X_train_ready)
    X_test_scaled = scaler.transform(X_test_ready)
    assert X_train_scaled.index.equals(y_train.index)
    assert X_test_scaled.index.equals(y_test.index)
    assert not X_train_scaled.isna().any().any()
    assert not X_test_scaled.isna().any().any()
    assert np.allclose(scaler.mean_, X_train_ready.mean().to_numpy())

    model = KNeighborsClassifier(
        n_neighbors=3, weights="uniform", metric="euclidean"
    )
    model.fit(X_train_scaled, y_train)
    predictions = model.predict(X_test_scaled)

    # predictions is an array in X_test row order; y_test has source indices.
    comparison = pd.DataFrame(
        {"actual": y_test, "predicted": predictions}, index=y_test.index
    )
    comparison["correct"] = comparison["actual"] == comparison["predicted"]
    correct_count = int(comparison["correct"].sum())
    errors = comparison.loc[~comparison["correct"]].copy()
    accuracy_manual = correct_count / len(comparison)
    accuracy_library = accuracy_score(y_test, predictions)

    assert len(predictions) == len(y_test) == 86
    assert abs(accuracy_manual - accuracy_library) < 1e-12
    assert correct_count + len(errors) == 86
    assert df.equals(source_copy)
    return {
        "features": features,
        "seed": seed,
        "correct": correct_count,
        "errors": len(errors),
        "accuracy": accuracy_library,
        "first_errors": errors.head(3),
        "test_class_counts": y_test.value_counts().to_dict(),
        "training_means": train_means.to_dict(),
    }

def main():
    parser = ArgumentParser()
    parser.add_argument("--csv", default="Datasets/penguins.csv")
    args = parser.parse_args()
    df = load_verified_csv(args.csv)
    print("Versions: pandas", pd.__version__, "numpy", np.__version__,
          "scikit-learn", sklearn.__version__)

    settings = [
        ("Teacher guided", ["flipper_length_mm", "body_mass_g"], 42),
        ("Student-lab teacher solution", ["bill_length_mm", "bill_depth_mm"], 17),
    ]
    for title, features, seed in settings:
        result = run_one_path(df, features, seed)
        print("\n" + title)
        print("Features:", features, "| seed:", seed)
        print("Correct:", result["correct"], "/ 86")
        print("Errors:", result["errors"])
        print("Accuracy:", result["accuracy"], "=",
              round(100 * result["accuracy"], 2), "%")
        print("First three errors, source-row indices:")
        print(result["first_errors"][["actual", "predicted"]].to_string())

        if sklearn.__version__ == "1.8.0":
            expected = 60 if seed == 42 else 83
            assert result["correct"] == expected, (
                "Unexpected result relative to verified sklearn 1.8.0 baseline"
            )

    print("\nPASS: course CSV, Train-only preparation, K=3 predictions, "
          "Accuracy consistency, row indices, unchanged source.")
    print("CAUTION: two feature pairs ALSO use different splits; "
          "do not rank them by these Test scores.")
    print("This script runs the same computation as the teacher notebooks, "
          "but it is NOT Google Colab Run All of their .ipynb files.")

if __name__ == "__main__":
    main()
