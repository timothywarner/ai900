"""AI-900 Hour 1: AI Fundamentals & Responsible AI - Interactive Console Demo.

This module provides an interactive console application demonstrating core AI-900
concepts including Azure AI Vision, Azure AI Content Safety, Responsible AI
principles, and AI workload classification.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from pathlib import Path
from collections.abc import Callable
from typing import TYPE_CHECKING

from dotenv import find_dotenv, load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

if TYPE_CHECKING:
    from azure.ai.vision.imageanalysis import ImageAnalysisResult

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

logging.basicConfig(
    level=logging.WARNING,
    format="%(levelname)s: %(message)s",
)
logger = logging.getLogger(__name__)

console = Console()

IMAGE_PATH = Path(__file__).resolve().parent / ".." / "assets" / "People" / "satya.jpg"


# ---------------------------------------------------------------------------
# Data models (frozen / immutable)
# ---------------------------------------------------------------------------


@dataclass(frozen=True, slots=True)
class QuizQuestion:
    """A single quiz question with a scenario, correct answer, and explanation."""

    scenario: str
    correct_answer: str
    explanation: str


@dataclass(frozen=True, slots=True)
class SeverityResult:
    """Content safety severity result for a single category."""

    category: str
    severity: int


# ---------------------------------------------------------------------------
# Environment helpers
# ---------------------------------------------------------------------------


def _load_env() -> None:
    """Load environment variables from the nearest .env file."""
    env_path = find_dotenv(usecwd=True)
    if env_path:
        load_dotenv(env_path)
    else:
        logger.warning("No .env file found. Azure services may not authenticate.")


def _get_env_var(name: str) -> str:
    """Retrieve a required environment variable or exit with an error.

    Args:
        name: The environment variable name to look up.

    Returns:
        The value of the environment variable.

    Raises:
        SystemExit: If the environment variable is not set.
    """
    import os

    value = os.environ.get(name)
    if not value:
        console.print(
            f"[bold red]ERROR:[/] Environment variable '{name}' is not set.\n"
            f"Ensure your .env file at demos/.env contains {name}=<value>."
        )
        raise SystemExit(1)
    return value


# ---------------------------------------------------------------------------
# Demo 1: Analyze an Image (Azure AI Vision 4.0)
# ---------------------------------------------------------------------------


def _analyze_image() -> None:
    """Analyze a local image using Azure AI Vision Image Analysis 4.0.

    Displays the caption, detected tags, and detected objects for the
    configured image file (People/satya.jpg).
    """
    from azure.ai.vision.imageanalysis import ImageAnalysisClient
    from azure.ai.vision.imageanalysis.models import VisualFeatures
    from azure.core.credentials import AzureKeyCredential
    from azure.core.exceptions import HttpResponseError

    endpoint = _get_env_var("AZURE_AI_ENDPOINT")
    key = _get_env_var("AZURE_AI_KEY")

    resolved_path = IMAGE_PATH.resolve()
    if not resolved_path.is_file():
        console.print(f"[bold red]ERROR:[/] Image not found at {resolved_path}")
        return

    console.print(f"\n[dim]Analyzing image:[/] {resolved_path.name}")
    console.print("[dim]Connecting to Azure AI Vision...[/]\n")

    client = ImageAnalysisClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key),
    )

    try:
        with open(resolved_path, "rb") as image_file:
            result: ImageAnalysisResult = client.analyze(
                image_data=image_file.read(),
                visual_features=[
                    VisualFeatures.DENSE_CAPTIONS,
                    VisualFeatures.TAGS,
                    VisualFeatures.OBJECTS,
                ],
            )
    except HttpResponseError as exc:
        console.print(f"[bold red]Azure API error:[/] {exc.message}")
        return
    except FileNotFoundError:
        console.print(f"[bold red]ERROR:[/] Could not open image at {resolved_path}")
        return

    _display_vision_results(result)


def _display_vision_results(result: ImageAnalysisResult) -> None:
    """Render image analysis results in a rich table.

    Args:
        result: The ImageAnalysisResult from the Azure AI Vision SDK.
    """
    # Dense Captions (first caption displayed as primary)
    if result.dense_captions is not None and result.dense_captions.list:
        top_caption = result.dense_captions.list[0]
        console.print(
            Panel(
                f"[bold cyan]{top_caption.text}[/]\n"
                f"Confidence: {top_caption.confidence:.1%}",
                title="Image Caption",
                border_style="cyan",
            )
        )

    # Tags
    if result.tags is not None and result.tags.list:
        tag_table = Table(title="Detected Tags", border_style="green")
        tag_table.add_column("Tag", style="bold green")
        tag_table.add_column("Confidence", justify="right")
        for tag in sorted(result.tags.list, key=lambda t: t.confidence, reverse=True):
            tag_table.add_row(tag.name, f"{tag.confidence:.1%}")
        console.print(tag_table)

    # Objects
    if result.objects is not None and result.objects.list:
        obj_table = Table(title="Detected Objects", border_style="yellow")
        obj_table.add_column("Object", style="bold yellow")
        obj_table.add_column("Confidence", justify="right")
        obj_table.add_column("Bounding Box", justify="right", style="dim")
        for obj in result.objects.list:
            if not obj.tags:
                continue
            bbox = obj.bounding_box
            bbox_str = f"({bbox.x}, {bbox.y}, {bbox.width}x{bbox.height})"
            obj_table.add_row(obj.tags[0].name, f"{obj.tags[0].confidence:.1%}", bbox_str)
        console.print(obj_table)


# ---------------------------------------------------------------------------
# Demo 2: Content Safety Check
# ---------------------------------------------------------------------------


def _content_safety_check() -> None:
    """Analyze user-provided text with Azure AI Content Safety.

    Prompts the user for text input, sends it to the Content Safety API,
    and displays severity levels for hate, violence, sexual, and self-harm
    categories.
    """
    from azure.ai.contentsafety import ContentSafetyClient
    from azure.ai.contentsafety.models import AnalyzeTextOptions, TextCategory
    from azure.core.credentials import AzureKeyCredential
    from azure.core.exceptions import HttpResponseError

    endpoint = _get_env_var("AZURE_AI_ENDPOINT")
    key = _get_env_var("AZURE_AI_KEY")

    console.print(
        "\n[bold]Enter text to analyze for content safety[/] "
        "(or press Enter for a sample):"
    )
    user_text = input("> ").strip()
    if not user_text:
        user_text = "I really dislike that group of people and think they should be excluded."
        console.print(f"[dim]Using sample text:[/] {user_text}\n")

    client = ContentSafetyClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key),
    )

    request = AnalyzeTextOptions(text=user_text)

    try:
        response = client.analyze_text(request)
    except HttpResponseError as exc:
        try:
            error_msg = exc.error.message if exc.error else str(exc)
        except AttributeError:
            error_msg = str(exc)
        console.print(f"[bold red]Azure Content Safety error:[/] {error_msg}")
        return

    categories_map: dict[TextCategory, str] = {
        TextCategory.HATE: "Hate",
        TextCategory.SELF_HARM: "Self-Harm",
        TextCategory.SEXUAL: "Sexual",
        TextCategory.VIOLENCE: "Violence",
    }

    results: tuple[SeverityResult, ...] = tuple(
        SeverityResult(
            category=categories_map.get(item.category, str(item.category)),
            severity=item.severity,
        )
        for item in response.categories_analysis
        if item.category in categories_map
    )

    _display_safety_results(results)


def _display_safety_results(results: tuple[SeverityResult, ...]) -> None:
    """Render content safety severity results in a rich table.

    Args:
        results: Tuple of SeverityResult objects to display.
    """
    severity_labels = {0: "Safe", 2: "Low", 4: "Medium", 6: "High"}

    table = Table(title="Content Safety Analysis", border_style="magenta")
    table.add_column("Category", style="bold")
    table.add_column("Severity", justify="center")
    table.add_column("Level", justify="center")
    table.add_column("Indicator", justify="left")

    for item in results:
        level = severity_labels.get(item.severity, f"Level {item.severity}")
        bar_count = item.severity
        bar = "[red]" + "!" * bar_count + "[/]" if bar_count > 0 else "[green]OK[/]"
        style = "green" if item.severity == 0 else "yellow" if item.severity <= 2 else "red"
        table.add_row(item.category, str(item.severity), f"[{style}]{level}[/]", bar)

    console.print(table)
    console.print(
        "[dim]Severity scale: 0 = Safe, 2 = Low, 4 = Medium, 6 = High[/]"
    )


# ---------------------------------------------------------------------------
# Demo 3: Responsible AI Principles Quiz
# ---------------------------------------------------------------------------

RAI_PRINCIPLES: tuple[str, ...] = (
    "Fairness",
    "Reliability & Safety",
    "Privacy & Security",
    "Inclusiveness",
    "Transparency",
    "Accountability",
)

RAI_QUESTIONS: tuple[QuizQuestion, ...] = (
    QuizQuestion(
        scenario=(
            "A hiring AI system consistently ranks male candidates higher than "
            "equally qualified female candidates for engineering roles."
        ),
        correct_answer="Fairness",
        explanation=(
            "Fairness requires AI systems to treat all people equitably. "
            "Bias in hiring decisions violates this principle."
        ),
    ),
    QuizQuestion(
        scenario=(
            "A self-driving car's AI must handle unexpected road conditions "
            "and safely pull over when its sensors are degraded by heavy rain."
        ),
        correct_answer="Reliability & Safety",
        explanation=(
            "Reliability & Safety means AI systems must perform dependably "
            "and not cause harm, especially in safety-critical scenarios."
        ),
    ),
    QuizQuestion(
        scenario=(
            "A healthcare AI stores patient diagnostic images on an unsecured "
            "server, and the data is accessed by unauthorized third parties."
        ),
        correct_answer="Privacy & Security",
        explanation=(
            "Privacy & Security requires AI systems to protect sensitive data "
            "and comply with privacy laws and regulations."
        ),
    ),
    QuizQuestion(
        scenario=(
            "A government chatbot is designed only in English, making it "
            "inaccessible to non-English-speaking residents who need services."
        ),
        correct_answer="Inclusiveness",
        explanation=(
            "Inclusiveness means AI should empower everyone and engage people, "
            "including those with disabilities or language barriers."
        ),
    ),
    QuizQuestion(
        scenario=(
            "A bank uses an AI model to deny loan applications, but applicants "
            "receive no explanation of why they were rejected or how the "
            "decision was made."
        ),
        correct_answer="Transparency",
        explanation=(
            "Transparency means people should understand how AI decisions are "
            "made and be able to identify potential biases or errors."
        ),
    ),
)


def _responsible_ai_quiz() -> None:
    """Run an interactive quiz on Microsoft's 6 Responsible AI principles.

    Presents 5 scenario-based questions. The user selects which principle
    applies. Displays a final score at the end.
    """
    console.print(
        "\n[bold magenta]Microsoft's 6 Responsible AI Principles:[/]"
    )
    for i, principle in enumerate(RAI_PRINCIPLES, 1):
        console.print(f"  {i}. {principle}")
    console.print()

    score = 0
    for q_num, question in enumerate(RAI_QUESTIONS, 1):
        console.print(
            Panel(question.scenario, title=f"Question {q_num}/5", border_style="blue")
        )
        console.print("[bold]Which Responsible AI principle applies?[/]")
        for i, principle in enumerate(RAI_PRINCIPLES, 1):
            console.print(f"  {i}. {principle}")

        answer = _get_quiz_answer(len(RAI_PRINCIPLES))
        selected = RAI_PRINCIPLES[answer - 1]

        if selected == question.correct_answer:
            score += 1
            console.print(f"[bold green]CORRECT![/] {question.explanation}\n")
        else:
            console.print(
                f"[bold red]Not quite.[/] The answer is "
                f"[bold]{question.correct_answer}[/].\n"
                f"{question.explanation}\n"
            )

    _display_quiz_score(score, len(RAI_QUESTIONS), "Responsible AI Quiz")


# ---------------------------------------------------------------------------
# Demo 4: AI Workload Identifier
# ---------------------------------------------------------------------------

AI_WORKLOAD_TYPES: tuple[str, ...] = (
    "Computer Vision",
    "Natural Language Processing",
    "Document Intelligence",
    "Generative AI",
)

WORKLOAD_QUESTIONS: tuple[QuizQuestion, ...] = (
    QuizQuestion(
        scenario=(
            "A retail company uses cameras to automatically count the number "
            "of customers entering each store location throughout the day."
        ),
        correct_answer="Computer Vision",
        explanation=(
            "Computer Vision enables AI to interpret visual information from "
            "cameras and images, such as detecting and counting people."
        ),
    ),
    QuizQuestion(
        scenario=(
            "A travel agency deploys a chatbot that understands customer "
            "questions in multiple languages and responds with relevant "
            "booking information."
        ),
        correct_answer="Natural Language Processing",
        explanation=(
            "NLP enables machines to understand, interpret, and respond to "
            "human language in a meaningful way."
        ),
    ),
    QuizQuestion(
        scenario=(
            "An insurance company automatically extracts policyholder names, "
            "dates, and claim amounts from scanned paper forms."
        ),
        correct_answer="Document Intelligence",
        explanation=(
            "Document Intelligence (formerly Form Recognizer) extracts "
            "structured data from documents, forms, and receipts."
        ),
    ),
    QuizQuestion(
        scenario=(
            "A marketing team uses an AI tool to draft blog posts, social "
            "media captions, and product descriptions from a short brief."
        ),
        correct_answer="Generative AI",
        explanation=(
            "Generative AI creates new content -- text, images, code -- based "
            "on patterns learned from training data."
        ),
    ),
    QuizQuestion(
        scenario=(
            "A factory uses AI to inspect products on an assembly line and "
            "flag items with visible surface defects before packaging."
        ),
        correct_answer="Computer Vision",
        explanation=(
            "Computer Vision can detect anomalies and defects in images, "
            "making it ideal for quality inspection on production lines."
        ),
    ),
)


def _ai_workload_quiz() -> None:
    """Run an interactive quiz on AI workload types.

    Presents 5 scenario-based questions. The user identifies which AI
    workload type matches the scenario. Displays a final score.
    """
    console.print("\n[bold magenta]AI Workload Types:[/]")
    for i, workload in enumerate(AI_WORKLOAD_TYPES, 1):
        console.print(f"  {i}. {workload}")
    console.print()

    score = 0
    for q_num, question in enumerate(WORKLOAD_QUESTIONS, 1):
        console.print(
            Panel(question.scenario, title=f"Question {q_num}/5", border_style="blue")
        )
        console.print("[bold]Which AI workload type does this describe?[/]")
        for i, workload in enumerate(AI_WORKLOAD_TYPES, 1):
            console.print(f"  {i}. {workload}")

        answer = _get_quiz_answer(len(AI_WORKLOAD_TYPES))
        selected = AI_WORKLOAD_TYPES[answer - 1]

        if selected == question.correct_answer:
            score += 1
            console.print(f"[bold green]CORRECT![/] {question.explanation}\n")
        else:
            console.print(
                f"[bold red]Not quite.[/] The answer is "
                f"[bold]{question.correct_answer}[/].\n"
                f"{question.explanation}\n"
            )

    _display_quiz_score(score, len(WORKLOAD_QUESTIONS), "AI Workload Identifier")


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------


def _get_quiz_answer(max_choice: int) -> int:
    """Prompt the user for a numeric quiz answer within a valid range.

    Args:
        max_choice: The maximum valid answer number (inclusive).

    Returns:
        The validated integer answer (1-based).
    """
    while True:
        raw = input(f"Your answer (1-{max_choice}): ").strip()
        try:
            choice = int(raw)
        except ValueError:
            console.print(f"[yellow]Please enter a number between 1 and {max_choice}.[/]")
            continue
        if 1 <= choice <= max_choice:
            return choice
        console.print(f"[yellow]Please enter a number between 1 and {max_choice}.[/]")


def _display_quiz_score(score: int, total: int, quiz_name: str) -> None:
    """Display the final quiz score with a styled panel.

    Args:
        score: Number of correct answers.
        total: Total number of questions.
        quiz_name: Display name of the quiz.
    """
    pct = score / total * 100 if total > 0 else 0
    color = "green" if pct >= 80 else "yellow" if pct >= 60 else "red"
    console.print(
        Panel(
            f"[bold {color}]{score}/{total} correct ({pct:.0f}%)[/]",
            title=f"{quiz_name} -- Final Score",
            border_style=color,
        )
    )


# ---------------------------------------------------------------------------
# Menu and entry point
# ---------------------------------------------------------------------------

MENU_OPTIONS: tuple[tuple[str, str], ...] = (
    ("1", "Analyze an Image (Azure AI Vision)"),
    ("2", "Content Safety Check (Azure AI Content Safety)"),
    ("3", "Responsible AI Principles Quiz"),
    ("4", "AI Workload Identifier Quiz"),
    ("Q", "Quit"),
)


def _display_banner() -> None:
    """Print the application startup banner."""
    banner_text = Text()
    banner_text.append("AI-900 Hour 1\n", style="bold cyan")
    banner_text.append("AI Fundamentals & Responsible AI", style="bold white")
    console.print(
        Panel(
            banner_text,
            border_style="bright_blue",
            padding=(1, 4),
            subtitle="Interactive Console Demo",
        )
    )
    console.print()


def _display_menu() -> None:
    """Print the numbered menu of available demos."""
    table = Table(
        show_header=False,
        border_style="bright_blue",
        title="Main Menu",
        padding=(0, 2),
    )
    table.add_column("Key", style="bold cyan", width=4)
    table.add_column("Description")
    for key, description in MENU_OPTIONS:
        table.add_row(key, description)
    console.print(table)


def _run_menu_loop() -> None:
    """Execute the main interactive menu loop until the user quits."""
    dispatch: dict[str, Callable[[], None]] = {
        "1": _analyze_image,
        "2": _content_safety_check,
        "3": _responsible_ai_quiz,
        "4": _ai_workload_quiz,
    }

    while True:
        _display_menu()
        choice = input("\nSelect an option (1-4, Q to quit): ").strip().upper()

        if choice == "Q":
            console.print("\n[bold cyan]Thanks for exploring AI fundamentals![/]")
            break

        handler = dispatch.get(choice)
        if handler is None:
            console.print("[yellow]Invalid choice. Please try again.[/]\n")
            continue

        console.rule(style="dim")
        try:
            handler()
        except KeyboardInterrupt:
            console.print("\n[dim]Returning to menu...[/]")
        except Exception as exc:
            logger.exception("Unexpected error in demo %s", choice)
            console.print(f"[bold red]Error:[/] {exc}")
        console.rule(style="dim")
        console.print()


def main() -> None:
    """Application entry point. Loads configuration and starts the menu."""
    _load_env()
    _display_banner()
    _run_menu_loop()


if __name__ == "__main__":
    main()
