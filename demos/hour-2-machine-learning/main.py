"""AI-900 Hour 2: Machine Learning Fundamentals.

Console demo application demonstrating core ML concepts locally
using scikit-learn and the UCI Bank Marketing dataset.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Final

import numpy as np
import pandas as pd
from dotenv import find_dotenv, load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs, make_regression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    r2_score,
    recall_score,
)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

BANNER: Final[str] = "AI-900 Hour 2: Machine Learning Fundamentals"
CSV_PATH: Final[Path] = Path(__file__).resolve().parent.parent / "assets" / "bankmarketing_train.csv"
RANDOM_STATE: Final[int] = 42

console = Console()


# ---------------------------------------------------------------------------
# Data helpers
# ---------------------------------------------------------------------------

def _load_bank_data() -> pd.DataFrame:
    """Load the bank marketing CSV and return an immutable copy.

    Returns:
        DataFrame with the bank marketing dataset.

    Raises:
        FileNotFoundError: If the CSV file is not at the expected path.
    """
    if not CSV_PATH.exists():
        raise FileNotFoundError(
            f"Bank marketing CSV not found at {CSV_PATH}. "
            "Please ensure the file exists."
        )
    return pd.read_csv(CSV_PATH)


# ---------------------------------------------------------------------------
# Demo 1 - Explore the Bank Marketing Dataset
# ---------------------------------------------------------------------------

def demo_explore_dataset() -> None:
    """Load and explore the bank marketing dataset.

    Shows shape, columns, dtypes, first 5 rows, class distribution,
    basic stats, and a text bar chart of class balance.
    """
    console.rule("[bold cyan]Demo 1: Explore the Bank Marketing Dataset[/]")
    df = _load_bank_data()

    # Shape
    console.print(f"\n[bold]Dataset shape:[/] {df.shape[0]} rows x {df.shape[1]} columns\n")

    # Column names and dtypes
    dtype_table = Table(title="Columns & Data Types", show_lines=True)
    dtype_table.add_column("Column", style="cyan")
    dtype_table.add_column("Dtype", style="green")
    for col in df.columns:
        dtype_table.add_row(col, str(df[col].dtype))
    console.print(dtype_table)

    # First 5 rows
    console.print("\n[bold]First 5 rows:[/]")
    preview_table = Table(show_lines=True, row_styles=["", "dim"])
    for col in df.columns:
        preview_table.add_column(col, overflow="fold", max_width=14)
    for _, row in df.head(5).iterrows():
        preview_table.add_row(*(str(v) for v in row))
    console.print(preview_table)

    # Class distribution of target column 'y'
    console.print("\n[bold]Target column 'y' — class distribution:[/]")
    counts = df["y"].value_counts()
    total = len(df)
    dist_table = Table(show_lines=True)
    dist_table.add_column("Class", style="cyan")
    dist_table.add_column("Count", style="green", justify="right")
    dist_table.add_column("Percentage", style="yellow", justify="right")
    for label, count in counts.items():
        dist_table.add_row(str(label), str(count), f"{count / total * 100:.1f}%")
    console.print(dist_table)

    # Text bar chart
    console.print("\n[bold]Class balance bar chart:[/]")
    max_bar = 50
    max_count = counts.max()
    for label, count in counts.items():
        bar_len = int(count / max_count * max_bar)
        bar = "\u2588" * bar_len
        console.print(f"  {str(label):>3s} | {bar} {count}")

    # Basic stats for numeric columns
    console.print("\n[bold]Basic statistics (numeric columns):[/]")
    stats = df.describe().T
    stats_table = Table(show_lines=True)
    stats_table.add_column("Column", style="cyan")
    for stat_col in stats.columns:
        stats_table.add_column(stat_col, justify="right")
    for idx_label, row in stats.iterrows():
        stats_table.add_row(str(idx_label), *(f"{v:.2f}" for v in row))
    console.print(stats_table)

    console.print("\n[green]Takeaway:[/] This dataset records whether bank clients subscribed "
                  "to a term deposit ('yes'/'no'). Notice the class imbalance -- most clients "
                  "said 'no'. This is a [bold]binary classification[/] problem.")


# ---------------------------------------------------------------------------
# Demo 2 - Classification (Decision Tree)
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class ClassificationResult:
    """Immutable container for classification metrics."""

    accuracy: float
    precision: float
    recall: float
    f1: float
    confusion: np.ndarray = field(repr=False)


def _train_classifier(df: pd.DataFrame) -> ClassificationResult:
    """Encode features, split, train a DecisionTreeClassifier, and evaluate.

    Args:
        df: The bank marketing DataFrame.

    Returns:
        ClassificationResult with all evaluation metrics.
    """
    df_encoded = df.copy()

    # Label-encode every object column
    encoders: dict[str, LabelEncoder] = {}
    for col in df_encoded.select_dtypes(include=["object"]).columns:
        enc = LabelEncoder()
        df_encoded[col] = enc.fit_transform(df_encoded[col])
        encoders[col] = enc

    x = df_encoded.drop(columns=["y"])
    y = df_encoded["y"]

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=RANDOM_STATE, stratify=y,
    )

    model = DecisionTreeClassifier(max_depth=5, random_state=RANDOM_STATE)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)

    return ClassificationResult(
        accuracy=float(accuracy_score(y_test, y_pred)),
        precision=float(precision_score(y_test, y_pred, zero_division=0)),
        recall=float(recall_score(y_test, y_pred, zero_division=0)),
        f1=float(f1_score(y_test, y_pred, zero_division=0)),
        confusion=confusion_matrix(y_test, y_pred),
    )


def demo_classification() -> None:
    """Train a Decision Tree on bank marketing data and explain metrics."""
    console.rule("[bold cyan]Demo 2: Classification Demo (Decision Tree)[/]")
    df = _load_bank_data()

    console.print("\n[dim]Training a DecisionTreeClassifier (max_depth=5) ...[/]\n")
    result = _train_classifier(df)

    metrics_table = Table(title="Classification Metrics", show_lines=True)
    metrics_table.add_column("Metric", style="cyan")
    metrics_table.add_column("Value", style="green", justify="right")
    metrics_table.add_column("Plain-English Meaning", style="yellow")

    metrics_table.add_row(
        "Accuracy", f"{result.accuracy:.4f}",
        "Fraction of ALL predictions that were correct.",
    )
    metrics_table.add_row(
        "Precision", f"{result.precision:.4f}",
        "Of clients predicted 'yes', how many actually subscribed?",
    )
    metrics_table.add_row(
        "Recall", f"{result.recall:.4f}",
        "Of clients who DID subscribe, how many did we catch?",
    )
    metrics_table.add_row(
        "F1 Score", f"{result.f1:.4f}",
        "Harmonic mean of precision & recall (balanced measure).",
    )
    console.print(metrics_table)

    # Confusion matrix
    console.print("\n[bold]Confusion Matrix:[/]")
    cm = result.confusion
    cm_table = Table(show_lines=True)
    cm_table.add_column("", style="bold")
    cm_table.add_column("Predicted: no", justify="center")
    cm_table.add_column("Predicted: yes", justify="center")
    cm_table.add_row("Actual: no", str(cm[0][0]), str(cm[0][1]))
    cm_table.add_row("Actual: yes", str(cm[1][0]), str(cm[1][1]))
    console.print(cm_table)

    console.print(
        "\n[green]Takeaway:[/] Classification predicts a [bold]category[/] (yes/no). "
        "The confusion matrix shows where the model gets it right and wrong. "
        "High accuracy can be misleading with imbalanced data -- always check "
        "precision, recall, and F1."
    )


# ---------------------------------------------------------------------------
# Demo 3 - Regression Concepts
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class RegressionResult:
    """Immutable container for regression metrics."""

    coefficients: tuple[float, ...]
    intercept: float
    r2: float
    y_test: tuple[float, ...]
    y_pred: tuple[float, ...]
    feature_names: tuple[str, ...]


def _train_regression() -> RegressionResult:
    """Generate synthetic auto-price-like data and train a LinearRegression.

    Returns:
        RegressionResult with coefficients, R-squared, and predictions.
    """
    x, y = make_regression(
        n_samples=200,
        n_features=3,
        noise=15.0,
        random_state=RANDOM_STATE,
    )
    feature_names = ("Engine Size", "Horsepower", "Curb Weight")

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=RANDOM_STATE,
    )

    model = LinearRegression()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)

    return RegressionResult(
        coefficients=tuple(float(c) for c in model.coef_),
        intercept=float(model.intercept_),
        r2=float(r2_score(y_test, y_pred)),
        y_test=tuple(float(v) for v in y_test),
        y_pred=tuple(float(v) for v in y_pred),
        feature_names=feature_names,
    )


def demo_regression() -> None:
    """Demonstrate linear regression on synthetic auto-price data."""
    console.rule("[bold cyan]Demo 3: Regression Concepts[/]")

    console.print(
        "\n[dim]Generating synthetic auto-price data (200 samples, 3 features) ...[/]\n"
    )
    result = _train_regression()

    # Coefficients
    coeff_table = Table(title="Model Coefficients", show_lines=True)
    coeff_table.add_column("Feature", style="cyan")
    coeff_table.add_column("Coefficient", style="green", justify="right")
    for name, coeff in zip(result.feature_names, result.coefficients, strict=True):
        coeff_table.add_row(name, f"{coeff:.4f}")
    coeff_table.add_row("[bold]Intercept[/]", f"{result.intercept:.4f}")
    console.print(coeff_table)

    console.print(f"\n[bold]R-squared (R\u00b2):[/] {result.r2:.4f}")
    console.print(
        "  R\u00b2 measures how well the model explains variance in the target. "
        "1.0 = perfect fit, 0.0 = no better than predicting the mean.\n"
    )

    # Text scatter: predicted vs actual (first 20 samples)
    console.print("[bold]Predicted vs Actual (first 20 test samples):[/]")
    scatter_table = Table(show_lines=True)
    scatter_table.add_column("#", justify="right", style="dim")
    scatter_table.add_column("Actual", justify="right", style="cyan")
    scatter_table.add_column("Predicted", justify="right", style="green")
    scatter_table.add_column("Error", justify="right", style="red")
    for i in range(min(20, len(result.y_test))):
        actual = result.y_test[i]
        pred = result.y_pred[i]
        scatter_table.add_row(
            str(i + 1),
            f"{actual:.1f}",
            f"{pred:.1f}",
            f"{actual - pred:+.1f}",
        )
    console.print(scatter_table)

    console.print(
        "\n[green]Takeaway:[/] [bold]Regression[/] predicts a continuous number "
        "(e.g., price, temperature). [bold]Classification[/] predicts a category "
        "(e.g., yes/no, cat/dog). Choose the task type based on your target variable."
    )


# ---------------------------------------------------------------------------
# Demo 4 - Clustering (KMeans)
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class ClusteringResult:
    """Immutable container for clustering output."""

    centers: tuple[tuple[float, float], ...]
    labels: tuple[int, ...]
    x_data: tuple[tuple[float, float], ...]
    k: int


def _run_clustering(k: int = 3, n_samples: int = 150) -> ClusteringResult:
    """Generate 2D blobs and run KMeans clustering.

    Args:
        k: Number of clusters.
        n_samples: Total number of data points.

    Returns:
        ClusteringResult with centers, labels, and data points.
    """
    x, _ = make_blobs(
        n_samples=n_samples,
        n_features=2,
        centers=k,
        cluster_std=1.2,
        random_state=RANDOM_STATE,
    )
    model = KMeans(n_clusters=k, random_state=RANDOM_STATE, n_init=10)
    model.fit(x)

    return ClusteringResult(
        centers=tuple((float(c[0]), float(c[1])) for c in model.cluster_centers_),
        labels=tuple(int(lb) for lb in model.labels_),
        x_data=tuple((float(row[0]), float(row[1])) for row in x),
        k=k,
    )


def _render_cluster_grid(result: ClusteringResult, grid_size: int = 25) -> None:
    """Render a text-based 2D scatter plot of clustered data.

    Args:
        result: ClusteringResult to visualize.
        grid_size: Width and height of the character grid.
    """
    xs = [p[0] for p in result.x_data]
    ys = [p[1] for p in result.x_data]
    x_min, x_max = min(xs), max(xs)
    y_min, y_max = min(ys), max(ys)

    x_range = x_max - x_min or 1.0
    y_range = y_max - y_min or 1.0

    cluster_chars = ("A", "B", "C", "D", "E", "F")
    cluster_colors = ("red", "green", "blue", "yellow", "magenta", "cyan")

    # Build grid
    grid: list[list[str]] = [[" "] * grid_size for _ in range(grid_size)]
    color_grid: list[list[str]] = [["white"] * grid_size for _ in range(grid_size)]

    for (px, py), label in zip(result.x_data, result.labels, strict=True):
        col = int((px - x_min) / x_range * (grid_size - 1))
        row = int((py - y_min) / y_range * (grid_size - 1))
        row = grid_size - 1 - row  # flip y-axis
        col = max(0, min(col, grid_size - 1))
        row = max(0, min(row, grid_size - 1))
        grid[row][col] = cluster_chars[label % len(cluster_chars)]
        color_grid[row][col] = cluster_colors[label % len(cluster_colors)]

    # Mark cluster centers with '*'
    for cx, cy in result.centers:
        col = int((cx - x_min) / x_range * (grid_size - 1))
        row = int((cy - y_min) / y_range * (grid_size - 1))
        row = grid_size - 1 - row
        col = max(0, min(col, grid_size - 1))
        row = max(0, min(row, grid_size - 1))
        grid[row][col] = "*"
        color_grid[row][col] = "bold white"

    text = Text()
    for r in range(grid_size):
        for c in range(grid_size):
            text.append(grid[r][c], style=color_grid[r][c])
        text.append("\n")

    console.print(Panel(text, title="Cluster Visualization (* = center)", border_style="cyan"))


def demo_clustering() -> None:
    """Demonstrate KMeans clustering on synthetic 2D data."""
    console.rule("[bold cyan]Demo 4: Clustering Demo (KMeans)[/]")
    console.print("\n[dim]Generating 150 synthetic 2D data points with 3 natural groups ...[/]\n")

    result = _run_clustering(k=3)

    # Cluster centers
    center_table = Table(title="Cluster Centers", show_lines=True)
    center_table.add_column("Cluster", style="cyan", justify="center")
    center_table.add_column("X", style="green", justify="right")
    center_table.add_column("Y", style="green", justify="right")
    center_table.add_column("Points", style="yellow", justify="right")
    for i, (cx, cy) in enumerate(result.centers):
        count = sum(1 for lb in result.labels if lb == i)
        center_table.add_row(str(i), f"{cx:.2f}", f"{cy:.2f}", str(count))
    console.print(center_table)

    # Visualization
    console.print()
    _render_cluster_grid(result)

    console.print(
        "\n[green]Takeaway:[/] Clustering is [bold]unsupervised[/] learning -- the "
        "algorithm finds groups WITHOUT labeled examples. Use it for customer "
        "segmentation, anomaly detection, and pattern discovery. [bold]Supervised[/] "
        "learning (classification/regression) requires labeled training data."
    )


# ---------------------------------------------------------------------------
# Demo 5 - ML Concepts Quiz
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class QuizQuestion:
    """A single quiz question."""

    scenario: str
    correct: str
    explanation: str


QUIZ_QUESTIONS: Final[tuple[QuizQuestion, ...]] = (
    QuizQuestion(
        scenario=(
            "A bank wants to predict whether a customer will default on a loan. "
            "The answer is yes or no."
        ),
        correct="classification",
        explanation=(
            "Predicting a category (yes/no) is classification. "
            "This is binary classification -- exactly two possible outcomes."
        ),
    ),
    QuizQuestion(
        scenario=(
            "An insurance company wants to estimate the dollar amount of a claim "
            "based on vehicle age, driver history, and location."
        ),
        correct="regression",
        explanation=(
            "Predicting a continuous number (dollar amount) is regression. "
            "The target variable is numeric, not categorical."
        ),
    ),
    QuizQuestion(
        scenario=(
            "A retailer groups customers into segments based on purchasing "
            "behavior. There are no predefined labels."
        ),
        correct="clustering",
        explanation=(
            "Finding natural groups in unlabeled data is clustering -- "
            "a form of unsupervised learning."
        ),
    ),
    QuizQuestion(
        scenario=(
            "A hospital predicts patient readmission risk as Low, Medium, or High "
            "based on diagnosis codes and demographics."
        ),
        correct="classification",
        explanation=(
            "Predicting one of several categories (Low/Medium/High) is "
            "multi-class classification."
        ),
    ),
    QuizQuestion(
        scenario=(
            "In a transformer architecture, what mechanism allows the model to "
            "weigh the importance of different input tokens relative to each other?"
        ),
        correct="self-attention",
        explanation=(
            "Self-attention (also called scaled dot-product attention) lets each "
            "token attend to every other token in the sequence, computing relevance "
            "weights. This is the core innovation of the Transformer paper "
            "'Attention Is All You Need' (2017)."
        ),
    ),
    QuizQuestion(
        scenario=(
            "A weather service predicts tomorrow's high temperature in degrees "
            "Fahrenheit from historical data."
        ),
        correct="regression",
        explanation=(
            "Predicting a continuous numeric value (temperature) is regression. "
            "The output is a number on a continuous scale."
        ),
    ),
)


def demo_quiz() -> None:
    """Run an interactive ML concepts quiz."""
    console.rule("[bold cyan]Demo 5: ML Concepts Quiz[/]")
    console.print(
        "\nFor each scenario, type [bold]regression[/], [bold]classification[/], "
        "[bold]clustering[/], or the concept name.\n"
    )

    score = 0
    total = len(QUIZ_QUESTIONS)

    for i, q in enumerate(QUIZ_QUESTIONS, start=1):
        console.print(Panel(q.scenario, title=f"Question {i}/{total}", border_style="cyan"))
        answer = input("  Your answer: ").strip().lower()

        if answer == q.correct:
            console.print("  [bold green]Correct![/]")
            score += 1
        else:
            console.print(f"  [bold red]Incorrect.[/] The answer is [bold]{q.correct}[/].")
        console.print(f"  [dim]{q.explanation}[/]\n")

    # Score summary
    pct = score / total * 100
    if pct >= 80:
        style = "bold green"
        verdict = "Excellent -- you have a strong grasp of ML concepts!"
    elif pct >= 50:
        style = "bold yellow"
        verdict = "Good effort -- review the explanations above to strengthen weak areas."
    else:
        style = "bold red"
        verdict = "Keep studying -- revisit the demos above and try again."

    console.print(Panel(
        f"Score: {score}/{total} ({pct:.0f}%)\n{verdict}",
        title="Quiz Results",
        border_style=style,
    ))


# ---------------------------------------------------------------------------
# Menu
# ---------------------------------------------------------------------------

DEMOS: Final[tuple[tuple[str, str, object], ...]] = (
    ("1", "Explore the Bank Marketing Dataset", demo_explore_dataset),
    ("2", "Classification Demo (Decision Tree)", demo_classification),
    ("3", "Regression Concepts", demo_regression),
    ("4", "Clustering Demo (KMeans)", demo_clustering),
    ("5", "ML Concepts Quiz", demo_quiz),
)


def _show_menu() -> None:
    """Display the numbered demo menu."""
    menu_table = Table(show_header=False, box=None, padding=(0, 2))
    menu_table.add_column(style="bold cyan", justify="right")
    menu_table.add_column(style="white")
    for key, label, _ in DEMOS:
        menu_table.add_row(key, label)
    menu_table.add_row("Q", "Quit")
    console.print(menu_table)


def main() -> None:
    """Entry point: display banner and run the interactive menu loop."""
    load_dotenv(find_dotenv())

    console.print(Panel(
        f"[bold white]{BANNER}[/]",
        border_style="bright_cyan",
        padding=(1, 4),
    ))

    demo_lookup: dict[str, object] = {key: fn for key, _, fn in DEMOS}

    while True:
        console.print()
        _show_menu()
        choice = input("\nSelect a demo (1-5) or Q to quit: ").strip().upper()

        if choice == "Q":
            console.print("\n[bold cyan]Thanks for learning about Machine Learning! Goodbye.[/]\n")
            break

        handler = demo_lookup.get(choice)
        if handler is None:
            console.print("[red]Invalid choice. Please enter 1-5 or Q.[/]")
            continue

        console.print()
        try:
            handler()  # type: ignore[operator]
        except FileNotFoundError as exc:
            console.print(f"[red]File error:[/] {exc}")
        except KeyboardInterrupt:
            console.print("\n[yellow]Demo interrupted. Returning to menu.[/]")
        except ValueError as exc:
            console.print(f"[red]Value error:[/] {exc}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[bold cyan]Goodbye![/]")
        sys.exit(0)
