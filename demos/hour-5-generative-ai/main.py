#!/usr/bin/env python3
"""
AI-900 Hour 5: Generative AI & Azure OpenAI
=============================================

Interactive console demo covering:
  1. Chat with GPT-4o (persona selection, conversation history)
  2. Prompt Engineering Workshop (zero-shot -> chain-of-thought)
  3. Temperature Explorer (creativity vs. determinism)
  4. DALL-E 3 Image Generation
  5. Content Filter Demo (Azure AI content safety)
  6. RAG Pattern Explainer (grounded vs. ungrounded answers)
  7. Generative AI Quiz (6 exam-style questions)

Prerequisites:
    uv sync
    # Ensure C:/github/ai900/demos/.env has required keys

Environment variables (loaded from ../.env via find_dotenv):
    AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_KEY, AZURE_OPENAI_DEPLOYMENT
    AZURE_OPENAI_API_VERSION
    AZURE_OPENAI_DALLE_ENDPOINT, AZURE_OPENAI_DALLE_KEY,
    AZURE_OPENAI_DALLE_DEPLOYMENT
"""

from __future__ import annotations

import os
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import openai
from dotenv import find_dotenv, load_dotenv
from openai import AzureOpenAI
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

load_dotenv(find_dotenv())

console = Console()


@dataclass(frozen=True)
class AzureConfig:
    """Immutable container for Azure OpenAI connection settings."""

    endpoint: str
    key: str
    deployment: str
    api_version: str


def _require_env(name: str) -> str:
    """Return an environment variable or exit with a helpful message."""
    value = os.getenv(name, "").strip()
    if not value:
        console.print(
            f"[bold red]Missing required environment variable:[/] {name}\n"
            "Ensure your .env file is at C:/github/ai900/demos/.env"
        )
        sys.exit(1)
    return value


def load_gpt_config() -> AzureConfig:
    """Load GPT-4o connection settings from environment."""
    return AzureConfig(
        endpoint=_require_env("AZURE_OPENAI_ENDPOINT"),
        key=_require_env("AZURE_OPENAI_KEY"),
        deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4o"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-10-21"),
    )


def load_dalle_config() -> AzureConfig:
    """Load DALL-E 3 connection settings from environment."""
    return AzureConfig(
        endpoint=_require_env("AZURE_OPENAI_DALLE_ENDPOINT"),
        key=_require_env("AZURE_OPENAI_DALLE_KEY"),
        deployment=os.getenv("AZURE_OPENAI_DALLE_DEPLOYMENT", "dall-e-3"),
        api_version="2024-02-01",
    )


def build_gpt_client(config: AzureConfig) -> AzureOpenAI:
    """Create an AzureOpenAI client for GPT."""
    return AzureOpenAI(
        azure_endpoint=config.endpoint,
        api_key=config.key,
        api_version=config.api_version,
    )


def build_dalle_client(config: AzureConfig) -> AzureOpenAI:
    """Create an AzureOpenAI client for DALL-E (separate endpoint)."""
    return AzureOpenAI(
        azure_endpoint=config.endpoint,
        api_key=config.key,
        api_version=config.api_version,
    )


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def show_token_usage(usage: Any) -> None:
    """Display token usage from an API response."""
    if usage is None:
        return
    table = Table(title="Token Usage", show_header=True, header_style="bold cyan")
    table.add_column("Metric", style="dim")
    table.add_column("Count", justify="right")
    table.add_row("Prompt tokens", str(usage.prompt_tokens))
    table.add_row("Completion tokens", str(usage.completion_tokens))
    table.add_row("Total tokens", str(usage.total_tokens))
    console.print(table)


def chat_completion(
    client: AzureOpenAI,
    deployment: str,
    messages: list[dict[str, str]],
    *,
    temperature: float = 0.7,
    max_tokens: int = 800,
) -> tuple[str, Any]:
    """Send a chat completion request and return (content, usage).

    Args:
        client: The AzureOpenAI client instance.
        deployment: Model deployment name.
        messages: Conversation messages list.
        temperature: Sampling temperature (0.0 - 1.0).
        max_tokens: Maximum tokens in the completion.

    Returns:
        Tuple of (response text, usage object).

    Raises:
        openai.BadRequestError: When content filtering triggers.
        openai.APIError: For other API-level failures.
    """
    response = client.chat.completions.create(
        model=deployment,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    content = response.choices[0].message.content or ""
    return content, response.usage


def pause() -> None:
    """Wait for the user to press Enter before continuing."""
    console.print("\n[dim]Press Enter to continue...[/]")
    input()


# ---------------------------------------------------------------------------
# Demo 1: Chat with GPT-4o
# ---------------------------------------------------------------------------

PERSONAS: dict[str, str] = {
    "1": (
        "You are a helpful, knowledgeable assistant. "
        "Answer clearly and concisely."
    ),
    "2": (
        "You are a swashbuckling pirate who explains technology concepts "
        "using nautical metaphors. Say 'Arrr' often."
    ),
    "3": (
        "You are a Socratic teacher. Never give direct answers. "
        "Instead, guide the student to discover the answer through "
        "a series of thoughtful questions."
    ),
}


def demo_chat(client: AzureOpenAI, config: AzureConfig) -> None:
    """Interactive chat loop with persona selection.

    Demonstrates system messages and conversation history.
    """
    console.print(Panel("[bold]Demo 1: Chat with GPT-4o[/]", style="blue"))

    console.print("Choose a persona for GPT-4o:\n")
    console.print("  [cyan]1[/] - Helpful Assistant")
    console.print("  [cyan]2[/] - Pirate Explainer")
    console.print("  [cyan]3[/] - Socratic Teacher")

    choice = input("\nYour choice (1/2/3): ").strip()
    system_msg = PERSONAS.get(choice, PERSONAS["1"])

    console.print(
        f"\n[bold green]System message set:[/] {system_msg[:80]}..."
    )
    console.print('[dim]Type "exit" to return to the main menu.[/]\n')

    messages: list[dict[str, str]] = [{"role": "system", "content": system_msg}]

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() == "exit":
            break

        messages = [*messages, {"role": "user", "content": user_input}]

        try:
            reply, usage = chat_completion(
                client, config.deployment, messages
            )
        except openai.APIError as exc:
            console.print(f"[red]API error:[/] {exc}")
            continue

        console.print(f"\n[bold cyan]GPT-4o:[/] {reply}\n")
        show_token_usage(usage)

        messages = [*messages, {"role": "assistant", "content": reply}]


# ---------------------------------------------------------------------------
# Demo 2: Prompt Engineering Workshop
# ---------------------------------------------------------------------------

PROMPT_QUESTION = (
    "What Azure AI service should I use to detect faces in photos?"
)


def demo_prompt_engineering(client: AzureOpenAI, config: AzureConfig) -> None:
    """Show the same question answered 4 ways with progressive improvement.

    Techniques: zero-shot, system message, few-shot, chain-of-thought.
    """
    console.print(
        Panel("[bold]Demo 2: Prompt Engineering Workshop[/]", style="blue")
    )
    console.print(f'[bold]Question:[/] "{PROMPT_QUESTION}"\n')

    # -- a) Zero-shot ---------------------------------------------------------
    console.print("[bold yellow]A) Zero-shot (no context)[/]")
    text_a, usage_a = chat_completion(
        client,
        config.deployment,
        [{"role": "user", "content": PROMPT_QUESTION}],
        temperature=0.3,
    )
    console.print(Markdown(text_a))
    show_token_usage(usage_a)

    # -- b) With system message -----------------------------------------------
    console.print("\n[bold yellow]B) With system message[/]")
    text_b, usage_b = chat_completion(
        client,
        config.deployment,
        [
            {
                "role": "system",
                "content": (
                    "You are an Azure AI certified instructor. "
                    "Give precise, exam-relevant answers referencing "
                    "specific Azure service names."
                ),
            },
            {"role": "user", "content": PROMPT_QUESTION},
        ],
        temperature=0.3,
    )
    console.print(Markdown(text_b))
    show_token_usage(usage_b)

    # -- c) Few-shot ----------------------------------------------------------
    console.print("\n[bold yellow]C) Few-shot (with examples)[/]")
    text_c, usage_c = chat_completion(
        client,
        config.deployment,
        [
            {
                "role": "system",
                "content": (
                    "You are an Azure AI certified instructor. "
                    "Answer in this format: Service Name -> Capability -> Use Case."
                ),
            },
            {
                "role": "user",
                "content": "What Azure service should I use to convert speech to text?",
            },
            {
                "role": "assistant",
                "content": (
                    "Azure AI Speech -> Speech-to-Text -> "
                    "Transcribe audio recordings, enable voice commands, "
                    "create meeting transcripts."
                ),
            },
            {
                "role": "user",
                "content": "What Azure service should I use to analyze sentiment in reviews?",
            },
            {
                "role": "assistant",
                "content": (
                    "Azure AI Language -> Sentiment Analysis -> "
                    "Classify customer feedback as positive/negative/neutral, "
                    "monitor brand perception at scale."
                ),
            },
            {"role": "user", "content": PROMPT_QUESTION},
        ],
        temperature=0.3,
    )
    console.print(Markdown(text_c))
    show_token_usage(usage_c)

    # -- d) Chain-of-thought --------------------------------------------------
    console.print("\n[bold yellow]D) Chain-of-thought (step-by-step)[/]")
    text_d, usage_d = chat_completion(
        client,
        config.deployment,
        [
            {
                "role": "system",
                "content": (
                    "You are an Azure AI certified instructor. "
                    "Think step by step before answering."
                ),
            },
            {
                "role": "user",
                "content": (
                    f"{PROMPT_QUESTION}\n\n"
                    "Let's think step by step:\n"
                    "1. What category does face detection fall under?\n"
                    "2. Which Azure AI service handles that category?\n"
                    "3. What specific API/feature within that service is used?\n"
                    "4. What are the key capabilities of that feature?"
                ),
            },
        ],
        temperature=0.3,
    )
    console.print(Markdown(text_d))
    show_token_usage(usage_d)

    # -- Explanation ----------------------------------------------------------
    console.print(
        Panel(
            "[bold]What improved at each step?[/]\n\n"
            "[yellow]A) Zero-shot:[/] No guidance -- model guesses what level "
            "of detail you want.\n"
            "[yellow]B) System message:[/] Persona focuses the answer on "
            "Azure-specific, exam-relevant content.\n"
            "[yellow]C) Few-shot:[/] Examples teach the desired output format "
            "(Service -> Capability -> Use Case).\n"
            "[yellow]D) Chain-of-thought:[/] Step-by-step reasoning produces "
            "a thorough, structured explanation.",
            title="Prompt Engineering Takeaways",
            style="green",
        )
    )


# ---------------------------------------------------------------------------
# Demo 3: Temperature Explorer
# ---------------------------------------------------------------------------

CREATIVE_PROMPT = "Write a one-sentence tagline for an AI startup."


def demo_temperature(client: AzureOpenAI, config: AzureConfig) -> None:
    """Compare the same creative prompt at temperatures 0.0, 0.5, and 1.0."""
    console.print(
        Panel("[bold]Demo 3: Temperature Explorer[/]", style="blue")
    )
    console.print(f'[bold]Prompt:[/] "{CREATIVE_PROMPT}"\n')

    temperatures = (0.0, 0.5, 1.0)
    results: list[tuple[float, str]] = []

    for temp in temperatures:
        console.print(f"[cyan]Temperature {temp}[/] ...")
        text, usage = chat_completion(
            client,
            config.deployment,
            [{"role": "user", "content": CREATIVE_PROMPT}],
            temperature=temp,
            max_tokens=100,
        )
        results.append((temp, text))
        show_token_usage(usage)

    table = Table(
        title="Temperature Comparison",
        show_header=True,
        header_style="bold magenta",
    )
    table.add_column("Temperature", justify="center")
    table.add_column("Response")
    for temp, text in results:
        table.add_row(str(temp), text)
    console.print(table)

    console.print(
        Panel(
            "[bold]What does temperature control?[/]\n\n"
            "[cyan]0.0[/] -- Deterministic. The model always picks the most "
            "probable next token. Best for factual/analytical tasks.\n\n"
            "[cyan]0.5[/] -- Balanced. Some creativity while staying "
            "coherent. Good default for many tasks.\n\n"
            "[cyan]1.0[/] -- Highly creative. The model samples more "
            "broadly, producing varied and surprising outputs. "
            "Great for brainstorming, but may reduce accuracy.",
            title="Temperature Explained",
            style="green",
        )
    )


# ---------------------------------------------------------------------------
# Demo 4: DALL-E 3 Image Generation
# ---------------------------------------------------------------------------


def demo_dalle(dalle_client: AzureOpenAI, dalle_config: AzureConfig) -> None:
    """Generate an image with DALL-E 3 from a user-provided prompt.

    Uses the separate DALL-E endpoint (eastus) and saves the image locally.
    """
    console.print(
        Panel("[bold]Demo 4: DALL-E 3 Image Generation[/]", style="blue")
    )

    user_prompt = input(
        "Enter an image prompt (or press Enter for default): "
    ).strip()
    if not user_prompt:
        user_prompt = (
            "A futuristic classroom where an AI hologram teacher "
            "is explaining cloud computing to diverse students, "
            "digital art style"
        )
    console.print(f'[bold]Prompt:[/] "{user_prompt}"\n')
    console.print("[dim]Generating image with DALL-E 3 ... this may take 15-30 seconds.[/]")

    try:
        response = dalle_client.images.generate(
            model=dalle_config.deployment,
            prompt=user_prompt,
            n=1,
            size="1024x1024",
        )
    except openai.BadRequestError as exc:
        console.print(
            f"[red]Content filter triggered or bad request:[/] {exc}"
        )
        return
    except openai.APIError as exc:
        console.print(f"[red]API error:[/] {exc}")
        return

    image_url = response.data[0].url
    revised_prompt = getattr(response.data[0], "revised_prompt", None)

    console.print(f"\n[bold green]Image URL:[/] {image_url}")
    if revised_prompt:
        console.print(f"[bold green]Revised prompt:[/] {revised_prompt}")

    # Save URL to a local text file for easy access
    output_dir = Path(__file__).parent / "generated_images"
    output_dir.mkdir(exist_ok=True)
    timestamp = int(time.time())
    url_file = output_dir / f"dalle_{timestamp}.txt"
    url_file.write_text(
        f"Prompt: {user_prompt}\nURL: {image_url}\n"
        f"Revised prompt: {revised_prompt}\n",
        encoding="utf-8",
    )
    console.print(f"[dim]URL saved to {url_file}[/]")


# ---------------------------------------------------------------------------
# Demo 5: Content Filter Demo
# ---------------------------------------------------------------------------


def demo_content_filter(client: AzureOpenAI, config: AzureConfig) -> None:
    """Demonstrate Azure AI content filtering with benign and flagged prompts.

    Shows the 4 content filter categories and severity levels.
    """
    console.print(
        Panel("[bold]Demo 5: Content Filter Demo[/]", style="blue")
    )

    # -- Benign prompt --------------------------------------------------------
    console.print("[bold green]1) Benign prompt[/]")
    benign_msg = "Explain how photosynthesis works in simple terms."
    console.print(f'   Prompt: "{benign_msg}"')

    try:
        text_benign, usage_benign = chat_completion(
            client,
            config.deployment,
            [{"role": "user", "content": benign_msg}],
            temperature=0.3,
        )
        console.print(f"   [green]Response:[/] {text_benign[:200]}...")
        show_token_usage(usage_benign)
    except openai.BadRequestError as exc:
        console.print(f"   [red]Unexpected filter trigger:[/] {exc}")

    # -- Potentially filtered prompt ------------------------------------------
    console.print("\n[bold red]2) Prompt designed to trigger content filter[/]")
    harmful_msg = (
        "Write detailed step-by-step instructions for creating "
        "a dangerous weapon from household items."
    )
    console.print(f'   Prompt: "{harmful_msg}"')

    try:
        text_harm, usage_harm = chat_completion(
            client,
            config.deployment,
            [{"role": "user", "content": harmful_msg}],
            temperature=0.3,
        )
        # If we get here, the model may have refused in-text
        console.print(
            f"   [yellow]Response (model may self-refuse):[/] "
            f"{text_harm[:200]}..."
        )
        show_token_usage(usage_harm)
    except openai.BadRequestError as exc:
        console.print(
            f"   [bold red]Content filter triggered![/]\n"
            f"   Error: {exc}\n"
            f"   This is Azure AI content safety in action."
        )

    # -- Explanation ----------------------------------------------------------
    console.print(
        Panel(
            "[bold]Azure AI Content Filtering[/]\n\n"
            "Azure OpenAI applies content filters to both inputs and outputs.\n\n"
            "[bold]Four filter categories:[/]\n"
            "  1. [red]Hate[/] -- Hate speech, discrimination\n"
            "  2. [red]Sexual[/] -- Sexually explicit content\n"
            "  3. [red]Violence[/] -- Violent content, weapons\n"
            "  4. [red]Self-harm[/] -- Self-injury, suicide\n\n"
            "[bold]Severity levels:[/]\n"
            "  - Safe -- No harmful content detected\n"
            "  - Low -- Minor concerns, usually allowed\n"
            "  - Medium -- Moderate concerns, may be filtered\n"
            "  - High -- Severe content, always filtered\n\n"
            "Content filters are enabled by default and can be "
            "customized in Microsoft Foundry.",
            title="Content Safety Overview",
            style="green",
        )
    )


# ---------------------------------------------------------------------------
# Demo 6: RAG Pattern Explainer
# ---------------------------------------------------------------------------

FICTIONAL_KB = (
    "NovaStar Technologies is a fictional company founded in 2021 in "
    "Portland, Oregon. They specialize in AI-powered supply chain "
    "optimization for mid-size manufacturers.\n\n"
    "NovaStar's flagship product is ChainSight, a real-time supply chain "
    "monitoring dashboard. ChainSight uses computer vision to inspect "
    "incoming shipments, NLP to parse supplier emails automatically, and "
    "predictive analytics to forecast demand. The platform costs $2,500/month "
    "for the Standard tier and $7,500/month for Enterprise.\n\n"
    "In Q3 2024, NovaStar raised a $15 million Series A led by Cascade "
    "Ventures. They currently employ 45 people and serve 120 customers "
    "across the Pacific Northwest. CEO Maria Chen stated their goal is "
    "to expand to 500 customers by end of 2025.\n\n"
    "NovaStar differentiates from competitors by offering on-premises "
    "deployment options for manufacturers with strict data sovereignty "
    "requirements. Their tech stack runs on Azure, using Azure Kubernetes "
    "Service, Azure AI Services, and Azure OpenAI."
)

RAG_QUESTION = "What is NovaStar's flagship product and how much does it cost?"


def demo_rag(client: AzureOpenAI, config: AzureConfig) -> None:
    """Show RAG by comparing answers with and without context.

    Uses a fictional company knowledge base to demonstrate grounding.
    """
    console.print(
        Panel("[bold]Demo 6: RAG Pattern Explainer[/]", style="blue")
    )

    console.print("[bold]Fictional Knowledge Base:[/]")
    console.print(Panel(FICTIONAL_KB, title="NovaStar Technologies KB"))
    console.print(f'\n[bold]Question:[/] "{RAG_QUESTION}"\n')

    # -- Without context (likely hallucination) -------------------------------
    console.print("[bold red]WITHOUT context (no RAG):[/]")
    text_no_rag, usage_no_rag = chat_completion(
        client,
        config.deployment,
        [{"role": "user", "content": RAG_QUESTION}],
        temperature=0.3,
    )
    console.print(Panel(text_no_rag, style="red"))
    show_token_usage(usage_no_rag)

    # -- With context (RAG pattern) -------------------------------------------
    console.print("\n[bold green]WITH context (RAG pattern):[/]")
    text_rag, usage_rag = chat_completion(
        client,
        config.deployment,
        [
            {
                "role": "system",
                "content": (
                    "Answer the user's question using ONLY the context below. "
                    "If the answer is not in the context, say so.\n\n"
                    f"Context:\n{FICTIONAL_KB}"
                ),
            },
            {"role": "user", "content": RAG_QUESTION},
        ],
        temperature=0.3,
    )
    console.print(Panel(text_rag, style="green"))
    show_token_usage(usage_rag)

    # -- Explanation ----------------------------------------------------------
    console.print(
        Panel(
            "[bold]How RAG Works[/]\n\n"
            "1. [cyan]Retrieve[/] -- Search a knowledge base for relevant "
            "documents (here we injected them directly).\n"
            "2. [cyan]Augment[/] -- Add retrieved text to the prompt as "
            "context (system message or user message).\n"
            "3. [cyan]Generate[/] -- The model answers grounded in real data "
            "instead of guessing.\n\n"
            "[bold]Benefits:[/]\n"
            "  - Reduces hallucination\n"
            "  - Keeps answers current without retraining\n"
            "  - Data stays in your control\n\n"
            "In production, Azure AI Search provides vector-based "
            "retrieval at scale.",
            title="RAG Pattern",
            style="green",
        )
    )


# ---------------------------------------------------------------------------
# Demo 7: Generative AI Quiz
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class QuizItem:
    """A single multiple-choice quiz question."""

    question: str
    options: tuple[str, ...]
    answer_index: int
    explanation: str


QUIZ_ITEMS: tuple[QuizItem, ...] = (
    QuizItem(
        question=(
            "What is the portal for managing Azure OpenAI model deployments, "
            "prompt experimentation, and content filters?"
        ),
        options=(
            "A) Azure Portal",
            "B) Microsoft Foundry (formerly Azure AI Studio)",
            "C) Visual Studio Code",
            "D) Azure DevOps",
        ),
        answer_index=1,
        explanation=(
            "Microsoft Foundry (previously called Azure AI Studio / "
            "Azure OpenAI Studio) is the dedicated portal for deploying "
            "models, testing prompts, and configuring content filters."
        ),
    ),
    QuizItem(
        question=(
            "In the Azure OpenAI model catalog, which model family is "
            "best suited for generating images from text descriptions?"
        ),
        options=(
            "A) GPT-4o",
            "B) Whisper",
            "C) DALL-E",
            "D) Ada (embeddings)",
        ),
        answer_index=2,
        explanation=(
            "DALL-E is OpenAI's image generation model. GPT-4o is for "
            "text/multimodal, Whisper is for speech-to-text, and Ada "
            "is for embeddings."
        ),
    ),
    QuizItem(
        question=(
            "Which prompt engineering technique provides example "
            "input-output pairs to guide the model's response format?"
        ),
        options=(
            "A) Zero-shot prompting",
            "B) Chain-of-thought prompting",
            "C) Few-shot prompting",
            "D) Temperature tuning",
        ),
        answer_index=2,
        explanation=(
            "Few-shot prompting includes examples in the prompt so the "
            "model learns the desired format. Zero-shot gives no examples; "
            "chain-of-thought asks for step-by-step reasoning."
        ),
    ),
    QuizItem(
        question=(
            "In Azure OpenAI, what unit is used to measure and bill "
            "for the amount of text processed by the model?"
        ),
        options=(
            "A) Words",
            "B) Characters",
            "C) Tokens",
            "D) Sentences",
        ),
        answer_index=2,
        explanation=(
            "Tokens are sub-word units used by LLMs. Roughly 1 token "
            "= 4 English characters or 0.75 words. Azure OpenAI bills "
            "per 1,000 tokens."
        ),
    ),
    QuizItem(
        question=(
            "Azure OpenAI content filters evaluate content across four "
            "harm categories. Which of the following is NOT one of them?"
        ),
        options=(
            "A) Hate",
            "B) Violence",
            "C) Plagiarism",
            "D) Self-harm",
        ),
        answer_index=2,
        explanation=(
            "The four content filter categories are Hate, Sexual, "
            "Violence, and Self-harm. Plagiarism is not one of the "
            "built-in content filter categories."
        ),
    ),
    QuizItem(
        question=(
            "What does the RAG (Retrieval Augmented Generation) pattern "
            "do to improve generative AI responses?"
        ),
        options=(
            "A) Retrains the model on your data",
            "B) Retrieves relevant documents and injects them into the prompt",
            "C) Increases the temperature parameter",
            "D) Reduces the token limit to save costs",
        ),
        answer_index=1,
        explanation=(
            "RAG retrieves relevant documents from a knowledge base and "
            "adds them to the prompt context, grounding the model's "
            "answer in your actual data without retraining."
        ),
    ),
)


def demo_quiz() -> None:
    """Run a 6-question generative AI quiz and display the score."""
    console.print(Panel("[bold]Demo 7: Generative AI Quiz[/]", style="blue"))
    console.print("Answer each question by typing A, B, C, or D.\n")

    score = 0

    for idx, item in enumerate(QUIZ_ITEMS, start=1):
        console.print(f"[bold]Q{idx}.[/] {item.question}")
        for opt in item.options:
            console.print(f"   {opt}")

        answer = input("\nYour answer: ").strip().upper()
        answer_map = {"A": 0, "B": 1, "C": 2, "D": 3}
        chosen = answer_map.get(answer, -1)

        if chosen == item.answer_index:
            score += 1
            console.print("[bold green]Correct![/]")
        else:
            correct_letter = "ABCD"[item.answer_index]
            console.print(
                f"[bold red]Incorrect.[/] The answer is "
                f"[bold]{correct_letter}[/]."
            )
        console.print(f"[dim]{item.explanation}[/]\n")

    # -- Score summary --------------------------------------------------------
    pct = (score / len(QUIZ_ITEMS)) * 100
    style = "green" if pct >= 80 else "yellow" if pct >= 60 else "red"
    console.print(
        Panel(
            f"[bold]Score: {score}/{len(QUIZ_ITEMS)} ({pct:.0f}%)[/]",
            title="Quiz Results",
            style=style,
        )
    )


# ---------------------------------------------------------------------------
# Main Menu
# ---------------------------------------------------------------------------

BANNER = r"""
    _   ___   ___   ___   ___
   /_\ |_ _| / _ \ / _ \ / _ \
  / _ \ | | | (_) | | | | | | |
 /_/ \_\___| \__  |\___/ \___/
    Hour 5   |___/
  Generative AI & Azure OpenAI
"""


def main() -> None:
    """Entry point: display menu and dispatch to demos."""
    gpt_config = load_gpt_config()
    gpt_client = build_gpt_client(gpt_config)

    console.print(Text(BANNER, style="bold cyan"))
    console.print(
        "[bold]AI-900 Hour 5: Generative AI & Azure OpenAI[/]\n"
    )

    menu = (
        "  [cyan]1[/] - Chat with GPT-4o\n"
        "  [cyan]2[/] - Prompt Engineering Workshop\n"
        "  [cyan]3[/] - Temperature Explorer\n"
        "  [cyan]4[/] - DALL-E 3 Image Generation\n"
        "  [cyan]5[/] - Content Filter Demo\n"
        "  [cyan]6[/] - RAG Pattern Explainer\n"
        "  [cyan]7[/] - Generative AI Quiz\n"
        "  [cyan]Q[/] - Quit"
    )

    while True:
        console.print(Panel(menu, title="Main Menu"))
        choice = input("Select a demo (1-7 or Q): ").strip().lower()

        if choice == "q":
            console.print("[bold green]Thanks for learning with us![/]")
            break
        elif choice == "1":
            demo_chat(gpt_client, gpt_config)
        elif choice == "2":
            demo_prompt_engineering(gpt_client, gpt_config)
        elif choice == "3":
            demo_temperature(gpt_client, gpt_config)
        elif choice == "4":
            dalle_config = load_dalle_config()
            dalle_client = build_dalle_client(dalle_config)
            demo_dalle(dalle_client, dalle_config)
        elif choice == "5":
            demo_content_filter(gpt_client, gpt_config)
        elif choice == "6":
            demo_rag(gpt_client, gpt_config)
        elif choice == "7":
            demo_quiz()
        else:
            console.print("[red]Invalid choice. Enter 1-7 or Q.[/]")

        if choice in {"1", "2", "3", "4", "5", "6", "7"}:
            pause()


if __name__ == "__main__":
    main()
