#!/usr/bin/env python3
"""AI-900 Hour 3: Computer Vision -- Interactive Console Demo.

Demonstrates five core Azure AI Vision capabilities:
  1. Image Analysis (4.0) -- captions, tags, objects, smart crops
  2. OCR (Read Text) -- extract text from clean and noisy images
  3. Face Detection -- face rectangles, head pose, blur, mask
  4. Document Intelligence -- receipt extraction with prebuilt model
  5. Custom Vision Concepts -- educational walkthrough and quiz

Prerequisites:
    uv sync                 # install dependencies from pyproject.toml
    Set environment variables in ../../.env (see README for details)
"""

from __future__ import annotations

import logging
import os
import sys
from pathlib import Path
from typing import Final

from dotenv import find_dotenv, load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Rich console (shared across all demos)
# ---------------------------------------------------------------------------
console: Final[Console] = Console()

# ---------------------------------------------------------------------------
# Asset paths (relative to this file)
# ---------------------------------------------------------------------------
BASE_DIR: Final[Path] = Path(__file__).resolve().parent
ASSETS_DIR: Final[Path] = BASE_DIR.parent / "assets"  # demos/assets/

PEOPLE_DIR: Final[Path] = ASSETS_DIR / "People"
PLACES_DIR: Final[Path] = ASSETS_DIR / "Places"
THINGS_DIR: Final[Path] = ASSETS_DIR / "Things"
OCR_DIR: Final[Path] = ASSETS_DIR / "OCR"


# ===================================================================
# Environment helpers
# ===================================================================

def _load_env() -> None:
    """Load environment variables from the shared .env file."""
    dotenv_path = find_dotenv(filename=".env", usecwd=True)
    if dotenv_path:
        load_dotenv(dotenv_path)
        logger.info("Loaded .env from %s", dotenv_path)
    else:
        logger.warning("No .env file found; relying on shell environment.")


def _require_env(name: str) -> str:
    """Return an environment variable or exit with a helpful message.

    Args:
        name: The environment variable name.

    Returns:
        The environment variable value.

    Raises:
        SystemExit: If the variable is not set.
    """
    value = os.environ.get(name, "").strip()
    if not value:
        console.print(
            f"[bold red]Missing required environment variable:[/] {name}\n"
            "Set it in demos/.env or export it in your shell."
        )
        sys.exit(1)
    return value


# ===================================================================
# Helpers
# ===================================================================

def _pick_file(options: dict[str, Path]) -> Path | None:
    """Present a numbered file picker and return the chosen Path.

    Args:
        options: Mapping of display label to file path.

    Returns:
        The selected Path, or None if the user cancels.
    """
    labels = list(options.keys())
    for idx, label in enumerate(labels, start=1):
        path = options[label]
        exists_marker = "[green]OK[/]" if path.exists() else "[red]MISSING[/]"
        console.print(f"  {idx}. {label}  ({exists_marker})")
    console.print("  0. Back to main menu")

    choice = console.input("\n  Choose an image: ").strip()
    if choice == "0":
        return None
    try:
        index = int(choice) - 1
        if 0 <= index < len(labels):
            selected = options[labels[index]]
            if not selected.exists():
                console.print(f"[red]File not found:[/] {selected}")
                return None
            return selected
    except ValueError:
        pass
    console.print("[yellow]Invalid choice.[/]")
    return None


def _section(title: str) -> None:
    """Print a styled section header.

    Args:
        title: The section heading text.
    """
    console.print()
    console.rule(f"[bold cyan]{title}[/]")
    console.print()


# ===================================================================
# Demo 1 -- Image Analysis (4.0)
# ===================================================================

def demo_image_analysis() -> None:
    """Analyze an image using Azure AI Vision Image Analysis 4.0.

    Shows caption, dense captions, tags, detected objects, and smart
    crop suggestions for a user-selected image.
    """
    from azure.ai.vision.imageanalysis import ImageAnalysisClient
    from azure.ai.vision.imageanalysis.models import VisualFeatures
    from azure.core.credentials import AzureKeyCredential

    _section("Demo 1: Image Analysis (4.0)")

    endpoint = _require_env("AZURE_AI_ENDPOINT")
    key = _require_env("AZURE_AI_KEY")

    image_options: dict[str, Path] = {
        "Landmark (Places)": PLACES_DIR / "landmark01.jpg",
        "Product placement (Things)": THINGS_DIR / "product-placement.png",
        "Satya Nadella (People)": PEOPLE_DIR / "satya.jpg",
        "Celebrity (People)": PEOPLE_DIR / "celebrity01.jpg",
        "Me (People)": PEOPLE_DIR / "me.png",
    }

    selected = _pick_file(image_options)
    if selected is None:
        return

    console.print(f"\n[bold]Analyzing:[/] {selected.name}")

    client = ImageAnalysisClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key),
    )

    with open(selected, "rb") as image_stream:
        try:
            result = client.analyze(
                image_data=image_stream,
                visual_features=[
                    VisualFeatures.CAPTION,
                    VisualFeatures.DENSE_CAPTIONS,
                    VisualFeatures.TAGS,
                    VisualFeatures.OBJECTS,
                    VisualFeatures.SMART_CROPS,
                ],
                smart_crops_aspect_ratios=[0.9, 1.33, 1.78],
            )
        except Exception as exc:
            _handle_sdk_error("Image Analysis", exc)
            return

    # Caption
    if result.caption is not None:
        console.print(
            Panel(
                f"[bold]{result.caption.text}[/]\n"
                f"Confidence: {result.caption.confidence:.2%}",
                title="Caption",
                border_style="green",
            )
        )

    # Dense captions
    if result.dense_captions is not None and result.dense_captions.list:
        table = Table(title="Dense Captions", show_lines=True)
        table.add_column("#", justify="right", width=4)
        table.add_column("Text")
        table.add_column("Confidence", justify="right")
        table.add_column("Bounding Box")
        for idx, dc in enumerate(result.dense_captions.list, start=1):
            bbox = dc.bounding_box
            bbox_str = (
                f"({bbox.x}, {bbox.y}, {bbox.width}x{bbox.height})"
                if bbox else "N/A"
            )
            table.add_row(
                str(idx),
                dc.text,
                f"{dc.confidence:.2%}",
                bbox_str,
            )
        console.print(table)

    # Tags
    if result.tags is not None and result.tags.list:
        table = Table(title="Tags", show_lines=True)
        table.add_column("Tag")
        table.add_column("Confidence", justify="right")
        for tag in sorted(result.tags.list, key=lambda t: t.confidence, reverse=True):
            bar = _confidence_bar(tag.confidence)
            table.add_row(tag.name, f"{tag.confidence:.2%}  {bar}")
        console.print(table)

    # Objects
    if result.objects is not None and result.objects.list:
        table = Table(title="Detected Objects", show_lines=True)
        table.add_column("Object")
        table.add_column("Confidence", justify="right")
        table.add_column("Bounding Box")
        for obj in result.objects.list:
            bbox = obj.bounding_box
            bbox_str = f"({bbox.x}, {bbox.y}, {bbox.width}x{bbox.height})"
            table.add_row(
                obj.tags[0].name if obj.tags else "unknown",
                f"{obj.tags[0].confidence:.2%}" if obj.tags else "N/A",
                bbox_str,
            )
        console.print(table)

    # Smart crops
    if result.smart_crops is not None and result.smart_crops.list:
        table = Table(title="Smart Crop Suggestions", show_lines=True)
        table.add_column("Aspect Ratio", justify="right")
        table.add_column("Bounding Box")
        for crop in result.smart_crops.list:
            bbox = crop.bounding_box
            bbox_str = f"({bbox.x}, {bbox.y}, {bbox.width}x{bbox.height})"
            table.add_row(f"{crop.aspect_ratio:.2f}", bbox_str)
        console.print(table)


def _confidence_bar(confidence: float, width: int = 20) -> str:
    """Return a simple text-based confidence bar.

    Args:
        confidence: Value between 0.0 and 1.0.
        width: Total character width of the bar.

    Returns:
        A string like '|========          |'.
    """
    filled = int(confidence * width)
    return "|" + "=" * filled + " " * (width - filled) + "|"


# ===================================================================
# Demo 2 -- OCR (Read Text)
# ===================================================================

def demo_ocr() -> None:
    """Extract text from images using Image Analysis 4.0 READ feature.

    Lets the user pick a clean or noisy OCR test image and displays
    extracted text blocks with confidence scores.
    """
    from azure.ai.vision.imageanalysis import ImageAnalysisClient
    from azure.ai.vision.imageanalysis.models import VisualFeatures
    from azure.core.credentials import AzureKeyCredential

    _section("Demo 2: OCR (Read Text)")

    endpoint = _require_env("AZURE_AI_ENDPOINT")
    key = _require_env("AZURE_AI_KEY")

    image_options: dict[str, Path] = {
        "Clean text image": OCR_DIR / "ocrtest-clean.png",
        "Noisy text image": OCR_DIR / "ocrtest-noisy.jpg",
    }

    selected = _pick_file(image_options)
    if selected is None:
        return

    console.print(f"\n[bold]Reading text from:[/] {selected.name}")

    client = ImageAnalysisClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key),
    )

    with open(selected, "rb") as image_stream:
        try:
            result = client.analyze(
                image_data=image_stream,
                visual_features=[VisualFeatures.READ],
            )
        except Exception as exc:
            _handle_sdk_error("OCR", exc)
            return

    if result.read is None or not result.read.blocks:
        console.print("[yellow]No text detected in this image.[/]")
        return

    for block_idx, block in enumerate(result.read.blocks, start=1):
        console.print(f"\n[bold]Block {block_idx}[/]")
        for line in block.lines:
            console.print(f"  [cyan]{line.text}[/]")
            word_table = Table(show_header=True, header_style="dim")
            word_table.add_column("Word")
            word_table.add_column("Confidence", justify="right")
            for word in line.words:
                style = "green" if word.confidence >= 0.9 else (
                    "yellow" if word.confidence >= 0.7 else "red"
                )
                word_table.add_row(
                    word.text,
                    f"[{style}]{word.confidence:.2%}[/]",
                )
            console.print(word_table)


# ===================================================================
# Demo 3 -- Face Detection
# ===================================================================

def demo_face_detection() -> None:
    """Detect faces using Azure AI Face service.

    Shows face rectangle, head pose, mask status, and recognition
    quality for a user-selected people image.
    """
    from azure.ai.vision.face import FaceClient
    from azure.ai.vision.face.models import (
        FaceAttributeTypeDetection03,
        FaceAttributeTypeRecognition04,
        FaceDetectionModel,
        FaceRecognitionModel,
    )
    from azure.core.credentials import AzureKeyCredential

    _section("Demo 3: Face Detection")

    endpoint = _require_env("AZURE_AI_ENDPOINT")
    key = _require_env("AZURE_AI_KEY")

    image_options: dict[str, Path] = {
        "Satya Nadella": PEOPLE_DIR / "satya.jpg",
        "Celebrity": PEOPLE_DIR / "celebrity01.jpg",
        "Me": PEOPLE_DIR / "me.png",
    }

    selected = _pick_file(image_options)
    if selected is None:
        return

    console.print(f"\n[bold]Detecting faces in:[/] {selected.name}")

    with FaceClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key),
    ) as face_client:
        file_content = selected.read_bytes()
        try:
            faces = face_client.detect(
                file_content,
                detection_model=FaceDetectionModel.DETECTION03,
                recognition_model=FaceRecognitionModel.RECOGNITION04,
                return_face_id=False,
                return_face_attributes=[
                    FaceAttributeTypeDetection03.HEAD_POSE,
                    FaceAttributeTypeDetection03.MASK,
                    FaceAttributeTypeDetection03.BLUR,
                    FaceAttributeTypeRecognition04.QUALITY_FOR_RECOGNITION,
                ],
                return_face_landmarks=True,
            )
        except Exception as exc:
            _handle_sdk_error("Face Detection", exc)
            return

    if not faces:
        console.print("[yellow]No faces detected in this image.[/]")
        return

    console.print(f"\n[bold green]Found {len(faces)} face(s).[/]\n")

    for idx, face in enumerate(faces, start=1):
        rect = face.face_rectangle
        table = Table(
            title=f"Face #{idx}",
            show_lines=True,
            border_style="blue",
        )
        table.add_column("Attribute", style="bold")
        table.add_column("Value")

        table.add_row(
            "Bounding Box",
            f"top={rect.top}, left={rect.left}, "
            f"width={rect.width}, height={rect.height}",
        )

        attrs = face.face_attributes
        if attrs is not None:
            if attrs.head_pose is not None:
                hp = attrs.head_pose
                table.add_row(
                    "Head Pose",
                    f"pitch={hp.pitch:.1f}, yaw={hp.yaw:.1f}, roll={hp.roll:.1f}",
                )
            if attrs.mask is not None:
                table.add_row(
                    "Mask",
                    f"type={attrs.mask.type}, nose+mouth covered={attrs.mask.nose_and_mouth_covered}",
                )
            if attrs.blur is not None:
                table.add_row(
                    "Blur",
                    f"level={attrs.blur.blur_level}, value={attrs.blur.value:.2f}",
                )
            if attrs.quality_for_recognition is not None:
                table.add_row(
                    "Quality for Recognition",
                    str(attrs.quality_for_recognition),
                )

        if face.face_landmarks is not None:
            landmark_count = len([
                attr for attr in dir(face.face_landmarks)
                if not attr.startswith("_") and attr not in ("as_dict", "clear",
                "copy", "get", "items", "keys", "pop", "popitem",
                "setdefault", "update", "values")
            ])
            table.add_row("Landmarks Detected", str(landmark_count))

        console.print(table)


# ===================================================================
# Demo 4 -- Document Intelligence (Receipt)
# ===================================================================

def demo_document_intelligence() -> None:
    """Analyze a Contoso receipt with Azure AI Document Intelligence.

    Uses the prebuilt-receipt model to extract merchant name, date,
    line items, totals, and key-value pairs.
    """
    from azure.ai.documentintelligence import DocumentIntelligenceClient
    from azure.core.credentials import AzureKeyCredential

    _section("Demo 4: Document Intelligence (Receipt)")

    endpoint = _require_env("AZURE_DOCINTELL_ENDPOINT")
    key = _require_env("AZURE_DOCINTELL_KEY")

    image_options: dict[str, Path] = {
        "Contoso receipt (PNG)": OCR_DIR / "contoso-receipt.png",
        "Contoso all-in-one receipt (JPG)": OCR_DIR / "contoso-allinone-receipt.jpg",
    }

    selected = _pick_file(image_options)
    if selected is None:
        return

    console.print(f"\n[bold]Analyzing receipt:[/] {selected.name}")
    console.print("[dim]This may take a few seconds...[/]\n")

    client = DocumentIntelligenceClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key),
    )

    with open(selected, "rb") as receipt_stream:
        try:
            poller = client.begin_analyze_document(
                "prebuilt-receipt",
                body=receipt_stream,
                locale="en-US",
            )
            result = poller.result()
        except Exception as exc:
            _handle_sdk_error("Document Intelligence", exc)
            return

    if not result.documents:
        console.print("[yellow]No receipt data extracted.[/]")
        return

    for doc_idx, receipt in enumerate(result.documents, start=1):
        console.print(
            Panel(
                f"[bold]Receipt #{doc_idx}[/]  "
                f"(confidence: {receipt.confidence:.2%})",
                border_style="magenta",
            )
        )

        fields = receipt.fields or {}

        # Merchant info
        _print_receipt_field(fields, "MerchantName", "Merchant")
        _print_receipt_field(fields, "MerchantAddress", "Address")
        _print_receipt_field(fields, "MerchantPhoneNumber", "Phone")
        _print_receipt_field(fields, "TransactionDate", "Date")
        _print_receipt_field(fields, "TransactionTime", "Time")

        # Line items
        items_field = fields.get("Items")
        if items_field and items_field.get("valueArray"):
            table = Table(title="Line Items", show_lines=True)
            table.add_column("#", justify="right", width=4)
            table.add_column("Description")
            table.add_column("Qty", justify="right")
            table.add_column("Price", justify="right")
            table.add_column("Total", justify="right")

            for item_idx, item in enumerate(items_field["valueArray"], start=1):
                item_obj = item.get("valueObject", {})
                desc = _extract_field_value(item_obj.get("Description"))
                qty = _extract_field_value(item_obj.get("Quantity"))
                price = _extract_field_value(item_obj.get("Price"))
                total = _extract_field_value(item_obj.get("TotalPrice"))
                table.add_row(
                    str(item_idx),
                    desc or "N/A",
                    qty or "",
                    price or "",
                    total or "",
                )
            console.print(table)

        # Totals
        console.print()
        _print_receipt_field(fields, "Subtotal", "Subtotal")
        _print_receipt_field(fields, "TotalTax", "Tax")
        _print_receipt_field(fields, "Tip", "Tip")
        _print_receipt_field(fields, "Total", "Total")


def _extract_field_value(field: dict | None) -> str | None:
    """Extract a display-friendly value from a Document Intelligence field.

    Args:
        field: The field dictionary from the API response.

    Returns:
        A string representation of the value, or None.
    """
    if field is None:
        return None
    for value_key in ("valueString", "valueNumber", "valueDate",
                      "valueCurrency", "content"):
        val = field.get(value_key) if isinstance(field, dict) else getattr(field, value_key, None)
        if val is not None:
            if isinstance(val, dict):
                # valueCurrency is {amount, currencySymbol}
                amount = val.get("amount", "")
                symbol = val.get("currencySymbol", "$")
                return f"{symbol}{amount}"
            return str(val)
    # Fall back to content
    content = field.get("content") if isinstance(field, dict) else getattr(field, "content", None)
    return str(content) if content is not None else None


def _print_receipt_field(
    fields: dict,
    field_name: str,
    label: str,
) -> None:
    """Print a single receipt field if it exists.

    Args:
        fields: The receipt fields dictionary.
        field_name: Key to look up in the fields dict.
        label: Human-readable label for display.
    """
    field = fields.get(field_name)
    if field is None:
        return
    value = _extract_field_value(field)
    confidence = getattr(field, "confidence", None)
    conf_str = f"  [dim](confidence: {confidence:.2%})[/]" if confidence else ""
    console.print(f"  [bold]{label}:[/] {value}{conf_str}")


# ===================================================================
# Demo 5 -- Custom Vision Concepts (Educational)
# ===================================================================

def demo_custom_vision_concepts() -> None:
    """Educational walkthrough of Azure Custom Vision concepts.

    Explains training vs. prediction, classification vs. object
    detection, export options, and runs an interactive quiz.
    """
    _section("Demo 5: Custom Vision Concepts")

    # --- Concept overview ---
    console.print(Panel(
        "[bold]What is Custom Vision?[/]\n\n"
        "Azure Custom Vision lets you build, deploy, and improve your own\n"
        "image classification and object detection models with minimal ML\n"
        "expertise. You upload labeled images, train a model, and publish\n"
        "a prediction endpoint -- all through the portal or REST API.",
        title="Custom Vision Service",
        border_style="cyan",
    ))

    console.print(Panel(
        "[bold]Training vs. Prediction[/]\n\n"
        "  [cyan]Training resource[/]  -- Used to create projects, upload\n"
        "    images, label them, and train iterations of your model.\n\n"
        "  [cyan]Prediction resource[/] -- Hosts your published model and\n"
        "    serves predictions via a REST endpoint. You can have multiple\n"
        "    published iterations and route traffic between them.",
        title="Two Resources, Two Roles",
        border_style="yellow",
    ))

    console.print(Panel(
        "[bold]Classification vs. Object Detection[/]\n\n"
        "  [green]Image Classification[/]\n"
        "    Assigns one or more labels to an entire image.\n"
        "    Multilabel: an image can belong to multiple classes.\n"
        "    Multiclass: exactly one class per image.\n\n"
        "  [green]Object Detection[/]\n"
        "    Locates objects within an image and returns bounding boxes\n"
        "    plus class labels for each detected object.",
        title="Project Types",
        border_style="green",
    ))

    console.print(Panel(
        "[bold]Export Options[/]\n\n"
        "  Compact models can be exported for edge deployment:\n"
        "  - TensorFlow / TensorFlow Lite\n"
        "  - ONNX (Windows ML, Azure IoT Edge)\n"
        "  - CoreML (iOS)\n"
        "  - Dockerfile (ARM / x86)\n"
        "  - Vision AI Dev Kit",
        title="Edge Deployment",
        border_style="magenta",
    ))

    # --- Show Carrot images ---
    console.print("\n[bold]Training Data Example: Carrot Images[/]\n")
    carrot_images = sorted(THINGS_DIR.glob("Carrot*.JPG"))
    if carrot_images:
        table = Table(title="Available Carrot Training Images")
        table.add_column("#", justify="right", width=4)
        table.add_column("Filename")
        table.add_column("Size (KB)", justify="right")
        for idx, img in enumerate(carrot_images, start=1):
            size_kb = img.stat().st_size / 1024
            table.add_row(str(idx), img.name, f"{size_kb:.0f}")
        console.print(table)
        console.print(
            f"\n  [dim]Found {len(carrot_images)} images. In the Custom Vision portal you\n"
            "  would upload these, tag them as 'carrot', then train an iteration.\n"
            "  The service needs at least 5 images per tag (15+ recommended).[/]"
        )
    else:
        console.print("[yellow]  No Carrot images found in Things directory.[/]")

    # --- Interactive quiz ---
    console.print("\n")
    console.rule("[bold cyan]Knowledge Check: Custom Vision Quiz[/]")
    console.print()

    questions: tuple[tuple[str, tuple[str, ...], int, str], ...] = (
        (
            "What is the MINIMUM number of images per tag recommended\n"
            "  to start training a Custom Vision model?",
            ("A) 1", "B) 5", "C) 15", "D) 50"),
            1,  # index of correct answer (B)
            "You need at least 5 images per tag, though 15+ gives\n"
            "    better results. More diverse images improve generalization.",
        ),
        (
            "Which project type returns bounding boxes around detected items?",
            (
                "A) Image Classification (Multiclass)",
                "B) Image Classification (Multilabel)",
                "C) Object Detection",
                "D) Semantic Segmentation",
            ),
            2,  # C
            "Object Detection draws bounding boxes. Classification assigns\n"
            "    labels to the whole image. Segmentation is not a Custom Vision type.",
        ),
        (
            "You want to run a Custom Vision model on an IoT device with\n"
            "  no internet connection. What must you do?",
            (
                "A) Use a Standard domain and call the REST API",
                "B) Use a Compact domain and export the model",
                "C) Deploy the full Azure endpoint to the device",
                "D) Custom Vision models cannot run offline",
            ),
            1,  # B
            "Compact domains produce smaller models that can be exported\n"
            "    to TensorFlow, ONNX, CoreML, or Docker for edge deployment.",
        ),
    )

    score = 0
    for q_idx, (question, choices, correct_idx, explanation) in enumerate(
        questions, start=1
    ):
        console.print(f"  [bold]Question {q_idx}:[/] {question}")
        for choice in choices:
            console.print(f"    {choice}")

        answer = console.input("\n    Your answer (A/B/C/D): ").strip().upper()
        answer_map = {"A": 0, "B": 1, "C": 2, "D": 3}
        chosen = answer_map.get(answer, -1)

        if chosen == correct_idx:
            console.print("    [bold green]Correct![/]")
            score += 1
        else:
            correct_letter = list(answer_map.keys())[correct_idx]
            console.print(
                f"    [bold red]Incorrect.[/] The correct answer is "
                f"[bold]{correct_letter}[/]."
            )
        console.print(f"    [dim]Explanation: {explanation}[/]\n")

    console.print(
        Panel(
            f"You scored [bold]{score}/{len(questions)}[/].",
            title="Quiz Results",
            border_style="green" if score == len(questions) else "yellow",
        )
    )


# ===================================================================
# Shared error handler
# ===================================================================

def _handle_sdk_error(service_name: str, exc: Exception) -> None:
    """Log and display an SDK error without crashing the menu loop.

    Args:
        service_name: Human-readable name of the service that failed.
        exc: The exception raised by the SDK.
    """
    from azure.core.exceptions import HttpResponseError

    if isinstance(exc, HttpResponseError):
        console.print(
            f"[bold red]{service_name} API error:[/] "
            f"{exc.status_code} -- {exc.message}"
        )
        logger.error(
            "%s HttpResponseError: %s %s",
            service_name, exc.status_code, exc.message,
        )
    else:
        console.print(f"[bold red]{service_name} error:[/] {exc}")
        logger.exception("%s unexpected error", service_name)


# ===================================================================
# Main menu
# ===================================================================

BANNER: Final[str] = r"""
    _    ___   ___   ___   ___
   / \  |_ _| / _ \ / _ \ / _ \
  / _ \  | | | (_) | | | | | | |
 / ___ \ | |  \__, | |_| | |_| |
/_/   \_\___|   /_/ \___/ \___/

  Hour 3: Computer Vision
"""


def main() -> None:
    """Run the interactive demo menu."""
    _load_env()

    console.print(Panel(
        Text(BANNER, style="bold cyan"),
        title="AI-900 Exam Prep",
        subtitle="Press Q to quit at any time",
        border_style="blue",
    ))

    menu_items: tuple[tuple[str, str], ...] = (
        ("1", "Image Analysis (caption, tags, objects, smart crops)"),
        ("2", "OCR -- Read Text from images"),
        ("3", "Face Detection (rectangle, head pose, blur, mask)"),
        ("4", "Document Intelligence (receipt extraction)"),
        ("5", "Custom Vision Concepts (educational walkthrough + quiz)"),
    )

    while True:
        console.print("\n[bold]Main Menu[/]\n")
        for key, description in menu_items:
            console.print(f"  [bold cyan]{key}.[/] {description}")
        console.print("  [bold cyan]Q.[/] Quit\n")

        choice = console.input("  Choose a demo: ").strip().upper()

        if choice == "Q":
            console.print("\n[bold green]Thanks for exploring Computer Vision![/]\n")
            break
        elif choice == "1":
            demo_image_analysis()
        elif choice == "2":
            demo_ocr()
        elif choice == "3":
            demo_face_detection()
        elif choice == "4":
            demo_document_intelligence()
        elif choice == "5":
            demo_custom_vision_concepts()
        else:
            console.print("[yellow]Invalid choice. Enter 1-5 or Q.[/]")


if __name__ == "__main__":
    main()
