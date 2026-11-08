#!/usr/bin/env python3
"""Build the three-page OCF V1 LinkedIn carousel from the launch seed.

Also rasterizes the finished PDF into three 1080x1350 page PNGs for native
LinkedIn image-carousel uploads.
"""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MultipleLocator
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
SEED_PATH = ROOT / "launch" / "_linkedin_seed.json"
OUTPUT_PATH = ROOT / "launch" / "OCF-V1-LinkedIn-Carousel-3page.pdf"
PAGE_PNG_PATHS = [ROOT / "launch" / "carousel-page-{}.png".format(n) for n in (1, 2, 3)]
PNG_SCALE = 1.0

PAGE_W, PAGE_H = 1080, 1350
BG = "#11191A"
PANEL = "#1A2526"
PANEL_ALT = "#202D2E"
TEAL = "#38E0C6"
AMBER = "#FFBB63"
WHITE = "#F3F7F5"
MUTED = "#AAB9B6"
GRID = "#3A4949"

REPO_URL = "https://github.com/aruncmichael-alt/ocf-v1-beyond-vram"
RELEASE_URL = REPO_URL + "/releases/tag/v1.2.0"
DOI_URL = "https://doi.org/10.5281/zenodo.23945369"
RECORD_URL = "https://zenodo.org/records/23945369"
REPORT_URL = REPO_URL + "/blob/main/docs/full-token-cost-report-2026-11-08.md"
PAPER_URL = REPO_URL + "/blob/main/paper/case-study.md"


def set_font(c: canvas.Canvas, name: str, size: float, color: str) -> None:
    c.setFont(name, size)
    c.setFillColor(HexColor(color))


def wrap_words(text: str, font: str, size: float, max_width: float) -> list[str]:
    lines: list[str] = []
    current = ""
    for word in text.split():
        candidate = word if not current else current + " " + word
        if stringWidth(candidate, font, size) <= max_width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_wrapped(
    c: canvas.Canvas,
    text: str,
    x: float,
    y: float,
    max_width: float,
    font: str = "Helvetica",
    size: float = 18,
    leading: float = 26,
    color: str = WHITE,
) -> float:
    set_font(c, font, size, color)
    for line in wrap_words(text, font, size, max_width):
        c.drawString(x, y, line)
        y -= leading
    return y


def draw_base(c: canvas.Canvas, page_no: int, label: str) -> None:
    c.setFillColor(HexColor(BG))
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    c.setFillColor(HexColor(TEAL))
    c.rect(0, PAGE_H - 14, PAGE_W * 0.72, 14, stroke=0, fill=1)
    c.setFillColor(HexColor(AMBER))
    c.rect(PAGE_W * 0.72, PAGE_H - 14, PAGE_W * 0.08, 14, stroke=0, fill=1)

    set_font(c, "Helvetica-Bold", 15, TEAL)
    c.drawString(76, 1290, "OCF V1  /  " + label.upper())
    set_font(c, "Helvetica", 15, MUTED)
    c.drawRightString(1004, 1290, "{:02d}  /  03".format(page_no))

    c.setStrokeColor(HexColor(GRID))
    c.setLineWidth(1)
    c.line(76, 88, 1004, 88)
    set_font(c, "Helvetica", 13, MUTED)
    footer = "doi.org/10.5281/zenodo.23945369  /  Zenodo concept DOI"
    c.drawString(76, 58, footer)
    c.linkURL(DOI_URL, (72, 48, 680, 76), relative=0, thickness=0)
    c.drawRightString(1004, 58, "ARUN C MICHAEL")


def add_output_chart(path: Path, coding: int, compaction: int) -> None:
    fig, ax = plt.subplots(figsize=(12.95, 2.0), dpi=120)
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    labels = ["Coding", "Compaction"]
    values = [coding, compaction]
    colors = [TEAL, AMBER]
    bars = ax.barh(labels, values, color=colors, height=0.50)
    ax.invert_yaxis()
    ax.set_xlim(0, 5_850_000)
    ax.xaxis.set_major_locator(MultipleLocator(1_000_000))
    ax.xaxis.set_major_formatter(FuncFormatter(lambda value, _: "{:.0f}M".format(value / 1_000_000)))
    ax.tick_params(axis="y", colors=WHITE, labelsize=13, length=0, pad=10)
    ax.tick_params(axis="x", colors=MUTED, labelsize=11, length=0, pad=8)
    ax.grid(axis="x", color=GRID, linewidth=0.8, alpha=0.8)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_visible(False)
    for bar, value in zip(bars, values):
        ax.text(
            value + 75_000,
            bar.get_y() + bar.get_height() / 2,
            "{:,}".format(value),
            va="center",
            ha="left",
            color=WHITE,
            fontsize=13,
            fontweight="bold",
        )
    fig.subplots_adjust(left=0.13, right=0.96, top=0.97, bottom=0.26)
    fig.savefig(path, facecolor=BG, bbox_inches="tight", pad_inches=0.08)
    plt.close(fig)


def add_cloud_chart(path: Path, scenarios: list[tuple[str, float]]) -> None:
    fig, ax = plt.subplots(figsize=(12.95, 5.83), dpi=120)
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)

    labels = [name for name, _ in scenarios]
    values = [value for _, value in scenarios]
    bars = ax.barh(labels, values, color=[TEAL, TEAL, TEAL, AMBER, AMBER], height=0.56)
    ax.invert_yaxis()
    ax.set_xlim(0, 300)
    ax.xaxis.set_major_locator(MultipleLocator(50))
    ax.xaxis.set_major_formatter(FuncFormatter(lambda value, _: chr(36) + "{:.0f}".format(value)))
    ax.tick_params(axis="y", colors=WHITE, labelsize=15, length=0, pad=10)
    ax.tick_params(axis="x", colors=MUTED, labelsize=12, length=0, pad=8)
    ax.grid(axis="x", color=GRID, linewidth=0.8, alpha=0.8)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_visible(False)
    for bar, value in zip(bars, values):
        ax.text(
            value + 4,
            bar.get_y() + bar.get_height() / 2,
            "$" + format(value, ",.2f"),
            va="center",
            ha="left",
            color=WHITE,
            fontsize=14,
            fontweight="bold",
        )
    fig.subplots_adjust(left=0.30, right=0.95, top=0.98, bottom=0.12)
    fig.savefig(path, facecolor=BG, bbox_inches="tight", pad_inches=0.08)
    plt.close(fig)


def draw_card(
    c: canvas.Canvas,
    x: float,
    y: float,
    width: float,
    height: float,
    value: str,
    label: str,
    accent: str,
    note: str | None = None,
) -> None:
    c.setFillColor(HexColor(PANEL))
    c.roundRect(x, y, width, height, 18, stroke=0, fill=1)
    c.setFillColor(HexColor(accent))
    c.rect(x, y + height - 7, width, 7, stroke=0, fill=1)
    set_font(c, "Helvetica-Bold", 36, accent)
    c.drawString(x + 24, y + height - 60, value)
    set_font(c, "Helvetica-Bold", 15, WHITE)
    c.drawString(x + 24, y + 45, label.upper())
    if note:
        set_font(c, "Helvetica", 13, MUTED)
        c.drawString(x + 24, y + 23, note)


def build_pdf(seed: dict) -> None:
    headline = seed["headline"]
    coding = int(headline["coding"])
    compaction = int(headline["compaction"])
    output = int(headline["output"])
    sessions = int(headline["sessions"])
    cache_pct = float(headline["cache_pct"])
    if coding + compaction != output:
        raise ValueError("Seed output total does not equal coding plus compaction.")

    scenarios = [
        ("Codex GPT-6 Luna", float(headline["luna"])),
        ("Codex GPT-6.1 Sol", float(headline["sol"])),
        ("Cursor Composer 2.5", float(headline["composer"])),
        ("Cursor GPT-5.3 Codex", float(headline["codex_cursor"])),
        ("Cursor Grok 4.7", float(headline["grok"])),
    ]
    with tempfile.TemporaryDirectory(prefix="linkedin-carousel-") as temp_dir:
        temp = Path(temp_dir)
        output_chart = temp / "output-split.png"
        cloud_chart = temp / "cloud-counterfactuals.png"
        add_output_chart(output_chart, coding, compaction)
        add_cloud_chart(cloud_chart, scenarios)

        c = canvas.Canvas(str(OUTPUT_PATH), pagesize=(PAGE_W, PAGE_H), pageCompression=1)
        c.setTitle("OCF V1 LinkedIn Carousel: Local Token Economics")
        c.setAuthor("Arun C Michael")
        c.setSubject("Three-page summary of the supplied OCF V1 token economics seed")

        # Page 1: result.
        draw_base(c, 1, "The result")
        set_font(c, "Helvetica-Bold", 53, WHITE)
        c.drawString(76, 1165, "More model than GPU.")
        set_font(c, "Helvetica", 21, MUTED)
        c.drawString(80, 1118, "One local inference ledger, measured across 224 coding sessions.")
        set_font(c, "Helvetica-Bold", 139, TEAL)
        c.drawString(72, 920, "{:.2f}M".format(output / 1_000_000))
        set_font(c, "Helvetica-Bold", 23, WHITE)
        c.drawString(85, 872, "LOCAL OUTPUT TOKENS")
        set_font(c, "Helvetica", 17, MUTED)
        c.drawString(85, 836, "Coding and compaction output in the retained OpenCode ledger")

        card_y, card_h, card_w, gap = 560, 190, 286, 25
        draw_card(c, 76, card_y, card_w, card_h, str(sessions), "coding sessions", TEAL)
        draw_card(c, 76 + card_w + gap, card_y, card_w, card_h, "$0", "local API charge", AMBER, "in this ledger")
        draw_card(
            c,
            76 + 2 * (card_w + gap),
            card_y,
            card_w,
            card_h,
            "83.6 / 16",
            "GB model / GB VRAM",
            TEAL,
        )
        set_font(c, "Helvetica", 17, MUTED)
        c.drawString(82, 515, "One workstation envelope: high host RAM and NVMe offload.")
        c.setStrokeColor(HexColor(GRID))
        c.line(76, 420, 1004, 420)
        set_font(c, "Helvetica-Bold", 21, WHITE)
        c.drawString(82, 370, "A measured case study by Arun C Michael")
        set_font(c, "Helvetica", 18, MUTED)
        c.drawString(82, 333, "OCF V1  /  local execution  /  dated token ledger")
        c.showPage()

        # Page 2: output split and same-footprint cloud prices.
        draw_base(c, 2, "The graphs")
        set_font(c, "Helvetica-Bold", 48, WHITE)
        c.drawString(76, 1195, "Where the numbers land.")
        set_font(c, "Helvetica", 18, MUTED)
        c.drawString(80, 1157, "One output ledger; five list-rate cloud counterfactuals.")

        set_font(c, "Helvetica-Bold", 22, WHITE)
        c.drawString(82, 1088, "Output split  /  5,290,865 total")
        c.drawImage(ImageReader(str(output_chart)), 74, 920, width=932, height=145, mask="auto")

        set_font(c, "Helvetica-Bold", 22, WHITE)
        c.drawString(82, 860, "Cloud counterfactuals  /  USD")
        c.drawImage(ImageReader(str(cloud_chart)), 74, 415, width=932, height=420, mask="auto")

        draw_card(c, 76, 175, 440, 165, "$0", "local API", AMBER, "no cloud API charge in ledger")
        draw_card(
            c,
            540,
            175,
            464,
            165,
            "{:.2f}%".format(cache_pct),
            "cache-read share",
            TEAL,
            "of recorded input tokens",
        )
        c.showPage()

        # Page 3: source links and interpretation.
        draw_base(c, 3, "Links and context")
        set_font(c, "Helvetica-Bold", 48, WHITE)
        c.drawString(76, 1195, "Read the numbers in context.")
        set_font(c, "Helvetica", 18, MUTED)
        c.drawString(80, 1157, "Sources, release history, and the limits of the comparison.")

        links = [
            ("REPOSITORY", REPO_URL),
            ("ECONOMICS CONTINUATION  /  v1.2.0", RELEASE_URL),
            ("ZENODO CONCEPT DOI", DOI_URL),
            ("ZENODO RECORD", RECORD_URL),
            ("FULL TOKEN REPORT", REPORT_URL),
            ("PAPER  /  SECTION 5.7", PAPER_URL),
        ]
        link_y = 1060
        for label, url in links:
            height = 73
            c.setFillColor(HexColor(PANEL))
            c.roundRect(76, link_y - height, 928, height, 14, stroke=0, fill=1)
            set_font(c, "Helvetica-Bold", 13, TEAL)
            c.drawString(96, link_y - 23, label)
            url_size = 14
            while stringWidth(url, "Helvetica", url_size) > 880 and url_size > 10:
                url_size -= 0.5
            set_font(c, "Helvetica", url_size, WHITE)
            c.drawString(96, link_y - 51, url)
            c.linkURL(url, (88, link_y - height + 6, 992, link_y - 5), relative=0, thickness=0)
            link_y -= height + 10

        box_y, box_h = 148, 360
        c.setFillColor(HexColor(PANEL_ALT))
        c.roundRect(76, box_y, 928, box_h, 18, stroke=0, fill=1)
        set_font(c, "Helvetica-Bold", 20, AMBER)
        c.drawString(101, box_y + box_h - 44, "HOW TO READ THIS COMPARISON")
        notes = [
            "Cloud rows price the same recorded local token mix. They are counterfactuals, not invoices or quality comparisons.",
            "The OpenCode ledger, live-process counters, and retained timing log are separate, overlapping, non-additive views.",
            "The DOI above identifies the Zenodo concept record. v1.2.0 continues the economics package; v1.0.x paper releases remain.",
        ]
        note_y = box_y + box_h - 87
        for note in notes:
            c.setFillColor(HexColor(TEAL))
            c.circle(105, note_y + 5, 4, stroke=0, fill=1)
            note_y = draw_wrapped(
                c,
                note,
                124,
                note_y,
                835,
                font="Helvetica",
                size=16,
                leading=23,
                color=WHITE,
            )
            note_y -= 15
        c.showPage()
        c.save()


def export_page_pngs() -> None:
    """Render the finished PDF pages to 1080x1350 PNGs."""
    try:
        import pypdfium2 as pdfium
    except ImportError as exc:
        raise SystemExit(
            "pypdfium2 is required to export page PNGs. Run: pip install pypdfium2"
        ) from exc
    pdf = pdfium.PdfDocument(str(OUTPUT_PATH))
    try:
        if len(pdf) != len(PAGE_PNG_PATHS):
            raise ValueError("PDF page count does not match the expected PNG outputs.")
        for page, png_path in zip(pdf, PAGE_PNG_PATHS):
            bitmap = page.render(scale=PNG_SCALE)
            pil_image = bitmap.to_pil()
            if pil_image.size != (PAGE_W, PAGE_H):
                raise ValueError(
                    "Expected {}x{} px for {}, got {}x{}.".format(
                        PAGE_W, PAGE_H, png_path.name, pil_image.size[0], pil_image.size[1]
                    )
                )
            pil_image.save(png_path, "PNG")
    finally:
        pdf.close()


def main() -> None:
    if not SEED_PATH.is_file():
        raise FileNotFoundError("Seed JSON not found: {}".format(SEED_PATH))
    with SEED_PATH.open("r", encoding="utf-8-sig") as stream:
        seed = json.load(stream)
    build_pdf(seed)
    print("Created {}".format(OUTPUT_PATH))
    export_page_pngs()
    for png_path in PAGE_PNG_PATHS:
        print("Created {}".format(png_path))


if __name__ == "__main__":
    main()
