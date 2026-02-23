#!/usr/bin/env python3
"""
AI-900 Hour 4: Natural Language Processing
===========================================

Interactive console demo covering Azure AI Language and Azure AI Speech services.
Demonstrates sentiment analysis, key phrase extraction, named entity recognition,
PII detection, language detection, speech-to-text, and text-to-speech.

Prerequisites:
    uv sync
    # Ensure C:/github/ai900/demos/.env has AZURE_AI_ENDPOINT and AZURE_AI_KEY

Azure Setup:
    - Multi-service Foundry resource (covers Language + Speech)
    - Region: eastus2
    - Endpoint: https://eastus2.api.cognitive.microsoft.com/

SDK Packages:
    - azure-ai-textanalytics (Language: sentiment, key phrases, entities, PII)
    - azure-cognitiveservices-speech (Speech: recognition + synthesis)
"""

from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import TYPE_CHECKING

from dotenv import find_dotenv, load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

if TYPE_CHECKING:
    from azure.ai.textanalytics import TextAnalyticsClient

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

SPEECH_REGION = "eastus2"

ASSETS_DIR = Path(__file__).resolve().parent.parent / "assets"

OCR_DIR = ASSETS_DIR / "OCR"
AUDIO_DIR = ASSETS_DIR / "Audio-Video"

GETTYSBURG_PATH = OCR_DIR / "Gettysburg.txt"
KENNEDY_PATH = OCR_DIR / "KennedyInaugural.txt"

WEATHER_WAV = AUDIO_DIR / "whatstheweatherlike.wav"
LIGHT_ON_WAV = AUDIO_DIR / "LightOn.wav"
LIGHT_OFF_WAV = AUDIO_DIR / "LightOff.wav"

SENTIMENT_COLOR_MAP: dict[str, str] = {
    "positive": "green",
    "negative": "red",
    "neutral": "yellow",
    "mixed": "yellow",
}

SAMPLE_REVIEWS: tuple[str, ...] = (
    "I absolutely love the new Azure AI services! The documentation is fantastic.",
    "The hotel was terrible. Room was dirty and staff was incredibly rude.",
    "The product arrived on time. It works as described, nothing special.",
    "Started off great but the battery died after a week. Very disappointed.",
    "Best purchase I've made all year -- highly recommend to everyone!",
)

MULTILINGUAL_SAMPLES: tuple[tuple[str, str], ...] = (
    ("Hello, how are you today? The weather is beautiful.", "English"),
    ("Hola, como estas hoy? El clima es hermoso.", "Spanish"),
    ("Bonjour, comment allez-vous aujourd'hui? Le temps est magnifique.", "French"),
    ("Hallo, wie geht es Ihnen heute? Das Wetter ist wunderbar.", "German"),
    ("Konnichiwa, kyou wa ogenki desu ka? Tenki ga subarashii desu.", "Japanese"),
)

PII_SAMPLE_TEXT = (
    "My name is John Smith and my email is john.smith@contoso.com. "
    "You can reach me at 555-123-4567. My SSN is 123-45-6789 "
    "and I live at 1234 Elm Street, Seattle, WA 98101."
)

NER_SAMPLE_TEXT = (
    "Microsoft announced Microsoft Foundry at the Build conference in Seattle "
    "on May 21, 2024. CEO Satya Nadella presented the new platform, which "
    "integrates OpenAI's GPT-4 model. The stock rose 3.5% to $420.50 on NASDAQ."
)

QUIZ_QUESTIONS: tuple[dict[str, str | tuple[str, ...]], ...] = (
    {
        "question": (
            "You need to build a bot that understands 'Book a flight to Seattle "
            "tomorrow'. Which Azure service should you use?"
        ),
        "choices": (
            "A) Custom Question Answering",
            "B) Conversational Language Understanding (CLU)",
            "C) Azure Translator",
            "D) Azure AI Speech",
        ),
        "answer": "B",
        "explanation": (
            "CLU (formerly LUIS) is designed for understanding intents and "
            "extracting entities from natural language utterances. 'Book a flight' "
            "is an intent; 'Seattle' and 'tomorrow' are entities."
        ),
    },
    {
        "question": (
            "What is the difference between an INTENT and an ENTITY "
            "in Conversational Language Understanding?"
        ),
        "choices": (
            "A) Intents are nouns; entities are verbs",
            "B) Intents represent what the user wants to DO; entities are the KEY DETAILS",
            "C) Intents and entities are the same thing",
            "D) Entities represent actions; intents represent data",
        ),
        "answer": "B",
        "explanation": (
            "An intent is the user's goal or action (e.g., 'BookFlight'). "
            "Entities are the important details extracted from the utterance "
            "(e.g., destination='Seattle', date='tomorrow')."
        ),
    },
    {
        "question": (
            "A company wants to create an FAQ bot from their existing documentation. "
            "Which service is the BEST fit?"
        ),
        "choices": (
            "A) Conversational Language Understanding (CLU)",
            "B) Azure AI Speech",
            "C) Custom Question Answering",
            "D) Sentiment Analysis",
        ),
        "answer": "C",
        "explanation": (
            "Custom Question Answering (formerly QnA Maker) is purpose-built for "
            "creating FAQ-style Q&A bots from existing documents, URLs, and manual "
            "Q&A pairs. CLU is better for complex intent-based conversations."
        ),
    },
    {
        "question": (
            "Which Azure AI service converts spoken audio into written text?"
        ),
        "choices": (
            "A) Text-to-Speech (TTS)",
            "B) Speech-to-Text (STT)",
            "C) Azure Translator",
            "D) Azure AI Language",
        ),
        "answer": "B",
        "explanation": (
            "Speech-to-Text (STT) transcribes audio into text. "
            "Text-to-Speech (TTS) does the opposite -- it synthesizes spoken "
            "audio from written text. Both are part of Azure AI Speech."
        ),
    },
    {
        "question": (
            "You analyze customer reviews and get a sentiment score of "
            "positive=0.05, neutral=0.10, negative=0.85. What is the overall sentiment?"
        ),
        "choices": (
            "A) Positive",
            "B) Neutral",
            "C) Negative",
            "D) Mixed",
        ),
        "answer": "C",
        "explanation": (
            "The highest confidence score determines the overall sentiment. "
            "With negative=0.85 being the highest, the document sentiment is "
            "Negative. Confidence scores always sum to approximately 1.0."
        ),
    },
)

console = Console()


# ---------------------------------------------------------------------------
# Client Factory
# ---------------------------------------------------------------------------


def _load_env() -> tuple[str, str]:
    """Load environment variables from the nearest .env file.

    Returns:
        Tuple of (endpoint, key).

    Raises:
        SystemExit: If required environment variables are missing.
    """
    dotenv_path = find_dotenv(filename=".env", usecwd=True)
    if dotenv_path:
        load_dotenv(dotenv_path)

    endpoint = os.getenv("AZURE_AI_ENDPOINT", "")
    key = os.getenv("AZURE_AI_KEY", "")

    if not endpoint or not key:
        console.print(
            Panel(
                "[bold red]Missing required environment variables![/]\n\n"
                "Please set the following in C:/github/ai900/demos/.env:\n"
                "  AZURE_AI_ENDPOINT\n"
                "  AZURE_AI_KEY",
                title="Configuration Error",
            )
        )
        sys.exit(1)

    return endpoint, key


def create_text_client(endpoint: str, key: str) -> TextAnalyticsClient:
    """Create an Azure AI Language TextAnalyticsClient.

    Args:
        endpoint: The Azure AI services endpoint URL.
        key: The Azure AI services subscription key.

    Returns:
        Configured TextAnalyticsClient instance.
    """
    from azure.ai.textanalytics import TextAnalyticsClient
    from azure.core.credentials import AzureKeyCredential

    return TextAnalyticsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key),
    )


# ---------------------------------------------------------------------------
# Demo 1: Sentiment Analysis
# ---------------------------------------------------------------------------


def demo_sentiment_analysis(client: TextAnalyticsClient) -> None:
    """Analyze sentiment of sample texts and optional user input.

    Shows document-level and per-sentence sentiment with color-coded
    confidence scores. Green = positive, red = negative, yellow = neutral/mixed.

    Args:
        client: Configured TextAnalyticsClient.
    """
    console.print(Panel("[bold cyan]Demo 1: Sentiment Analysis[/]", expand=False))
    console.print(
        "Analyzes text to determine positive, negative, neutral, or mixed sentiment.\n"
    )

    # Build the list of texts to analyze
    texts: list[str] = list(SAMPLE_REVIEWS)

    console.print("[bold]Sample texts loaded.[/] You can also add your own.")
    user_text = console.input(
        "[dim]Type your own text (or press Enter to skip):[/] "
    ).strip()
    if user_text:
        texts.append(user_text)

    console.print()

    try:
        results = client.analyze_sentiment(texts, show_opinion_mining=True)
    except Exception as exc:
        _handle_api_error("Sentiment Analysis", exc)
        return

    for idx, result in enumerate(results):
        if result.is_error:
            console.print(f"[red]Error on text {idx + 1}: {result.error.message}[/]")
            continue

        color = SENTIMENT_COLOR_MAP.get(result.sentiment, "white")
        header = Text(f"Text {idx + 1}: {result.sentiment.upper()}", style=f"bold {color}")

        table = Table(show_header=True, header_style="bold")
        table.add_column("Metric", style="dim")
        table.add_column("Value")

        table.add_row("Positive", f"{result.confidence_scores.positive:.2%}")
        table.add_row("Neutral", f"{result.confidence_scores.neutral:.2%}")
        table.add_row("Negative", f"{result.confidence_scores.negative:.2%}")

        console.print(header)
        console.print(f"  [dim]{texts[idx][:100]}{'...' if len(texts[idx]) > 100 else ''}[/]")
        console.print(table)

        # Per-sentence breakdown
        for sent in result.sentences:
            sent_color = SENTIMENT_COLOR_MAP.get(sent.sentiment, "white")
            console.print(
                f"  [{sent_color}]Sentence:[/] \"{sent.text[:80]}\" "
                f"-> [{sent_color}]{sent.sentiment}[/] "
                f"(pos={sent.confidence_scores.positive:.0%}, "
                f"neu={sent.confidence_scores.neutral:.0%}, "
                f"neg={sent.confidence_scores.negative:.0%})"
            )
        console.print()

    _pause()


# ---------------------------------------------------------------------------
# Demo 2: Key Phrase Extraction
# ---------------------------------------------------------------------------


def demo_key_phrase_extraction(client: TextAnalyticsClient) -> None:
    """Extract key phrases from the Gettysburg Address or Kennedy Inaugural.

    Args:
        client: Configured TextAnalyticsClient.
    """
    console.print(Panel("[bold cyan]Demo 2: Key Phrase Extraction[/]", expand=False))
    console.print("Extracts the most important phrases from a document.\n")

    # Let user pick a speech
    console.print("[bold]Available texts:[/]")
    console.print("  1) Gettysburg Address (Lincoln)")
    console.print("  2) Kennedy Inaugural Address")
    choice = console.input("\n[dim]Pick 1 or 2 (default=1):[/] ").strip()

    if choice == "2":
        path = KENNEDY_PATH
        label = "Kennedy Inaugural Address"
    else:
        path = GETTYSBURG_PATH
        label = "Gettysburg Address"

    text = _read_text_file(path)
    if text is None:
        return

    console.print(f"\n[bold]Analyzing:[/] {label}")
    console.print(f"[dim]({len(text)} characters)[/]\n")

    # The API accepts documents up to 5120 chars; split if needed
    documents = _chunk_text(text, max_chars=5120)

    try:
        results = client.extract_key_phrases(documents)
    except Exception as exc:
        _handle_api_error("Key Phrase Extraction", exc)
        return

    all_phrases: list[str] = []
    for result in results:
        if result.is_error:
            console.print(f"[red]Error: {result.error.message}[/]")
            continue
        all_phrases.extend(result.key_phrases)

    # Deduplicate while preserving order
    seen: set[str] = set()
    unique_phrases: list[str] = []
    for phrase in all_phrases:
        lower = phrase.lower()
        if lower not in seen:
            seen.add(lower)
            unique_phrases.append(phrase)

    table = Table(title=f"Key Phrases from {label}", show_lines=False)
    table.add_column("#", style="dim", width=4)
    table.add_column("Key Phrase", style="bold green")

    for i, phrase in enumerate(unique_phrases, 1):
        table.add_row(str(i), phrase)

    console.print(table)
    console.print(f"\n[bold]{len(unique_phrases)}[/] unique key phrases extracted.\n")
    _pause()


# ---------------------------------------------------------------------------
# Demo 3: Named Entity Recognition + PII Detection
# ---------------------------------------------------------------------------


def demo_entity_recognition(client: TextAnalyticsClient) -> None:
    """Run NER on sample text, then demonstrate PII detection.

    Args:
        client: Configured TextAnalyticsClient.
    """
    console.print(
        Panel("[bold cyan]Demo 3: Named Entity Recognition & PII Detection[/]", expand=False)
    )

    # --- Part A: NER ---
    console.print("[bold]Part A: Named Entity Recognition[/]")
    console.print(f"[dim]Text: {NER_SAMPLE_TEXT}[/]\n")

    try:
        ner_results = client.recognize_entities([NER_SAMPLE_TEXT])
    except Exception as exc:
        _handle_api_error("Entity Recognition", exc)
        return

    result = ner_results[0]
    if result.is_error:
        console.print(f"[red]Error: {result.error.message}[/]")
    else:
        table = Table(title="Recognized Entities", show_lines=True)
        table.add_column("Entity", style="bold")
        table.add_column("Category", style="cyan")
        table.add_column("Subcategory", style="dim")
        table.add_column("Confidence", justify="right")

        for entity in result.entities:
            table.add_row(
                entity.text,
                entity.category,
                entity.subcategory or "-",
                f"{entity.confidence_score:.0%}",
            )
        console.print(table)

    # --- Part B: PII Detection ---
    console.print("\n[bold]Part B: PII (Personally Identifiable Information) Detection[/]")
    console.print(f"[dim]Text: {PII_SAMPLE_TEXT}[/]\n")

    try:
        pii_results = client.recognize_pii_entities([PII_SAMPLE_TEXT])
    except Exception as exc:
        _handle_api_error("PII Detection", exc)
        return

    pii_result = pii_results[0]
    if pii_result.is_error:
        console.print(f"[red]Error: {pii_result.error.message}[/]")
    else:
        table = Table(title="Detected PII Entities", show_lines=True)
        table.add_column("PII Value", style="bold red")
        table.add_column("Category", style="cyan")
        table.add_column("Confidence", justify="right")

        for entity in pii_result.entities:
            table.add_row(
                entity.text,
                entity.category,
                f"{entity.confidence_score:.0%}",
            )

        console.print(table)
        console.print(
            f"\n[bold]Redacted text:[/]\n[dim]{pii_result.redacted_text}[/]\n"
        )

    _pause()


# ---------------------------------------------------------------------------
# Demo 4: Language Detection
# ---------------------------------------------------------------------------


def demo_language_detection(client: TextAnalyticsClient) -> None:
    """Detect languages in multilingual samples and optional user input.

    Args:
        client: Configured TextAnalyticsClient.
    """
    console.print(Panel("[bold cyan]Demo 4: Language Detection[/]", expand=False))
    console.print("Identifies the language of input text with confidence scores.\n")

    texts: list[str] = [sample for sample, _expected in MULTILINGUAL_SAMPLES]
    expected: list[str] = [exp for _sample, exp in MULTILINGUAL_SAMPLES]

    user_text = console.input(
        "[dim]Type text in any language (or press Enter to skip):[/] "
    ).strip()
    if user_text:
        texts.append(user_text)
        expected.append("(your input)")

    console.print()

    try:
        results = client.detect_language(texts)
    except Exception as exc:
        _handle_api_error("Language Detection", exc)
        return

    table = Table(title="Language Detection Results", show_lines=True)
    table.add_column("#", style="dim", width=4)
    table.add_column("Text (first 60 chars)", max_width=60)
    table.add_column("Expected", style="dim")
    table.add_column("Detected", style="bold green")
    table.add_column("ISO Code", style="cyan")
    table.add_column("Confidence", justify="right")

    for idx, result in enumerate(results):
        if result.is_error:
            table.add_row(
                str(idx + 1),
                texts[idx][:60],
                expected[idx],
                f"[red]Error[/]",
                "-",
                "-",
            )
            continue

        lang = result.primary_language
        table.add_row(
            str(idx + 1),
            texts[idx][:60],
            expected[idx],
            lang.name,
            lang.iso6391_name,
            f"{lang.confidence_score:.0%}",
        )

    console.print(table)
    console.print()
    _pause()


# ---------------------------------------------------------------------------
# Demo 5: Speech Recognition & Synthesis
# ---------------------------------------------------------------------------


def demo_speech(key: str) -> None:
    """Demonstrate speech-to-text and text-to-speech with Azure AI Speech.

    Args:
        key: The Azure AI services subscription key.
    """
    console.print(Panel("[bold cyan]Demo 5: Speech Recognition & Synthesis[/]", expand=False))

    try:
        import azure.cognitiveservices.speech as speechsdk
    except ImportError:
        console.print(
            "[red]azure-cognitiveservices-speech is not installed.[/]\n"
            "Run: uv pip install azure-cognitiveservices-speech"
        )
        _pause()
        return

    console.print("[bold]Available sub-demos:[/]")
    console.print("  A) Speech-to-Text: Transcribe a WAV file")
    console.print("  B) Text-to-Speech: Synthesize text to a WAV file")
    choice = console.input("\n[dim]Pick A or B (default=A):[/] ").strip().upper()

    if choice == "B":
        _demo_text_to_speech(speechsdk, key)
    else:
        _demo_speech_to_text(speechsdk, key)

    _pause()


def _demo_speech_to_text(speechsdk: object, key: str) -> None:
    """Transcribe a WAV file using Azure AI Speech.

    Args:
        speechsdk: The imported azure.cognitiveservices.speech module.
        key: The Azure AI services subscription key.
    """
    console.print("\n[bold]Speech-to-Text: Transcribe a WAV file[/]\n")

    wav_files = {
        "1": (WEATHER_WAV, "whatstheweatherlike.wav"),
        "2": (LIGHT_ON_WAV, "LightOn.wav"),
        "3": (LIGHT_OFF_WAV, "LightOff.wav"),
    }

    console.print("[bold]Available WAV files:[/]")
    for num, (_path, name) in wav_files.items():
        exists = "[green]found[/]" if _path.exists() else "[red]not found[/]"
        console.print(f"  {num}) {name} ({exists})")

    pick = console.input("\n[dim]Pick 1-3 (default=1):[/] ").strip()
    wav_path, wav_name = wav_files.get(pick, wav_files["1"])

    if not wav_path.exists():
        console.print(f"[red]File not found: {wav_path}[/]")
        return

    console.print(f"\n[bold]Transcribing:[/] {wav_name}")
    console.print("[dim]Processing...[/]")

    try:
        speech_config = speechsdk.SpeechConfig(subscription=key, region=SPEECH_REGION)
        audio_config = speechsdk.AudioConfig(filename=str(wav_path))
        recognizer = speechsdk.SpeechRecognizer(
            speech_config=speech_config, audio_config=audio_config
        )

        result = recognizer.recognize_once()

        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            console.print(
                Panel(
                    f"[bold green]{result.text}[/]",
                    title="Recognized Text",
                    border_style="green",
                )
            )
        elif result.reason == speechsdk.ResultReason.NoMatch:
            console.print("[yellow]No speech could be recognized from the audio.[/]")
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation = result.cancellation_details
            console.print(f"[red]Speech recognition canceled: {cancellation.reason}[/]")
            if cancellation.error_details:
                console.print(f"[red]Error: {cancellation.error_details}[/]")
        else:
            console.print(f"[yellow]Unexpected result reason: {result.reason}[/]")

    except Exception as exc:
        _handle_api_error("Speech-to-Text", exc)


def _demo_text_to_speech(speechsdk: object, key: str) -> None:
    """Synthesize text to a WAV file using Azure AI Speech.

    Args:
        speechsdk: The imported azure.cognitiveservices.speech module.
        key: The Azure AI services subscription key.
    """
    console.print("\n[bold]Text-to-Speech: Synthesize speech to a WAV file[/]\n")

    user_text = console.input(
        "[dim]Type text to synthesize (or press Enter for default):[/] "
    ).strip()

    if not user_text:
        user_text = (
            "Welcome to AI 900, Hour 4. Today we explore Natural Language Processing "
            "with Azure AI services. Let's get started!"
        )

    output_path = Path(__file__).resolve().parent / "output_speech.wav"

    console.print(f"\n[bold]Synthesizing:[/] \"{user_text[:80]}{'...' if len(user_text) > 80 else ''}\"")
    console.print(f"[bold]Output file:[/] {output_path}")
    console.print("[dim]Processing...[/]")

    try:
        speech_config = speechsdk.SpeechConfig(subscription=key, region=SPEECH_REGION)
        speech_config.speech_synthesis_voice_name = "en-US-JennyNeural"

        audio_config = speechsdk.AudioConfig(filename=str(output_path))
        synthesizer = speechsdk.SpeechSynthesizer(
            speech_config=speech_config, audio_config=audio_config
        )

        result = synthesizer.speak_text(user_text)

        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            console.print(
                Panel(
                    f"[bold green]Audio saved to {output_path}[/]\n"
                    f"Voice: en-US-JennyNeural\n"
                    f"Text length: {len(user_text)} characters",
                    title="Synthesis Complete",
                    border_style="green",
                )
            )
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation = result.cancellation_details
            console.print(f"[red]Speech synthesis canceled: {cancellation.reason}[/]")
            if cancellation.error_details:
                console.print(f"[red]Error: {cancellation.error_details}[/]")
        else:
            console.print(f"[yellow]Unexpected result reason: {result.reason}[/]")

    except Exception as exc:
        _handle_api_error("Text-to-Speech", exc)


# ---------------------------------------------------------------------------
# Demo 6: NLP Concepts Quiz
# ---------------------------------------------------------------------------


def demo_quiz() -> None:
    """Run an interactive quiz on NLP concepts for the AI-900 exam."""
    console.print(Panel("[bold cyan]Demo 6: NLP Concepts Quiz[/]", expand=False))
    console.print(
        "Test your knowledge of Azure NLP services.\n"
        f"[bold]{len(QUIZ_QUESTIONS)} questions[/] -- let's go!\n"
    )

    score = 0

    for idx, q in enumerate(QUIZ_QUESTIONS, 1):
        console.print(f"[bold]Question {idx}:[/] {q['question']}\n")
        for choice in q["choices"]:
            console.print(f"  {choice}")

        answer = console.input("\n[dim]Your answer (A/B/C/D):[/] ").strip().upper()

        correct = q["answer"]
        if answer == correct:
            score += 1
            console.print(f"[bold green]Correct![/] {q['explanation']}\n")
        else:
            console.print(
                f"[bold red]Incorrect.[/] The correct answer is [bold]{correct}[/].\n"
                f"{q['explanation']}\n"
            )

    # Score summary
    pct = (score / len(QUIZ_QUESTIONS)) * 100
    if pct >= 80:
        color = "green"
        msg = "Excellent work!"
    elif pct >= 60:
        color = "yellow"
        msg = "Good effort -- review the explanations above."
    else:
        color = "red"
        msg = "Keep studying -- you'll get there!"

    console.print(
        Panel(
            f"[bold {color}]Score: {score}/{len(QUIZ_QUESTIONS)} ({pct:.0f}%)[/]\n{msg}",
            title="Quiz Results",
        )
    )
    _pause()


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------


def _read_text_file(path: Path) -> str | None:
    """Read a UTF-8 text file, returning None on failure.

    Args:
        path: Path to the text file.

    Returns:
        File contents as a string, or None if the file cannot be read.
    """
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        console.print(f"[red]File not found: {path}[/]")
        return None
    except OSError as exc:
        console.print(f"[red]Error reading {path}: {exc}[/]")
        return None


def _chunk_text(text: str, max_chars: int = 5120) -> list[str]:
    """Split text into chunks that fit the API document size limit.

    Args:
        text: The full text to split.
        max_chars: Maximum characters per chunk.

    Returns:
        List of text chunks.
    """
    if len(text) <= max_chars:
        return [text]

    chunks: list[str] = []
    start = 0
    while start < len(text):
        end = start + max_chars
        # Try to break at a sentence boundary
        if end < len(text):
            last_period = text.rfind(".", start, end)
            if last_period > start:
                end = last_period + 1
        chunks.append(text[start:end].strip())
        start = end
    return chunks


def _handle_api_error(operation: str, exc: Exception) -> None:
    """Display a formatted API error message.

    Args:
        operation: Name of the operation that failed.
        exc: The exception that was raised.
    """
    from azure.core.exceptions import HttpResponseError

    if isinstance(exc, HttpResponseError):
        console.print(
            Panel(
                f"[bold red]Azure API Error in {operation}[/]\n\n"
                f"Status: {exc.status_code}\n"
                f"Message: {exc.message}",
                title="API Error",
                border_style="red",
            )
        )
    else:
        console.print(
            Panel(
                f"[bold red]Error in {operation}[/]\n\n"
                f"{type(exc).__name__}: {exc}",
                title="Error",
                border_style="red",
            )
        )


def _pause() -> None:
    """Wait for user to press Enter before continuing."""
    console.input("[dim]Press Enter to continue...[/]")


# ---------------------------------------------------------------------------
# Menu
# ---------------------------------------------------------------------------


BANNER = r"""
    _    ___      ___   ___   ___
   / \  |_ _|   / _ \ / _ \ / _ \
  / _ \  | |   | (_) | | | | | | |
 / ___ \ | |    \__, | |_| | |_| |
/_/   \_\___|     /_/ \___/ \___/

  Hour 4: Natural Language Processing
"""


def show_menu() -> None:
    """Display the main menu options."""
    console.print("\n[bold]Choose a demo:[/]\n")
    console.print("  [cyan]1[/]  Sentiment Analysis")
    console.print("  [cyan]2[/]  Key Phrase Extraction")
    console.print("  [cyan]3[/]  Named Entity Recognition & PII Detection")
    console.print("  [cyan]4[/]  Language Detection")
    console.print("  [cyan]5[/]  Speech Recognition & Synthesis")
    console.print("  [cyan]6[/]  NLP Concepts Quiz")
    console.print("  [cyan]Q[/]  Quit\n")


def main() -> None:
    """Entry point: load config, display menu, and dispatch demos."""
    console.print(Panel(BANNER, style="bold cyan", expand=False))

    endpoint, key = _load_env()
    client = create_text_client(endpoint, key)

    dispatch: dict[str, object] = {
        "1": lambda: demo_sentiment_analysis(client),
        "2": lambda: demo_key_phrase_extraction(client),
        "3": lambda: demo_entity_recognition(client),
        "4": lambda: demo_language_detection(client),
        "5": lambda: demo_speech(key),
        "6": demo_quiz,
    }

    while True:
        show_menu()
        choice = console.input("[bold]Enter choice:[/] ").strip().upper()

        if choice == "Q":
            console.print("\n[bold green]Thanks for exploring NLP! Goodbye.[/]\n")
            break

        handler = dispatch.get(choice)
        if handler is None:
            console.print("[red]Invalid choice. Please try again.[/]")
            continue

        console.print()
        handler()


if __name__ == "__main__":
    main()
