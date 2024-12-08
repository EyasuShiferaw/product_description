
import os
import xml.etree.ElementTree as ET  # Included for potential future XML data support

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    Image,
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

# --- Constants ---
_OUTPUT_FILENAME = "product_description.pdf"
_DEFAULT_IMAGE_DIR = "images"
_DEFAULT_FONT_DIR = "fonts"

_DEFAULT_FONT_NAME = "Helvetica"
_DEFAULT_FONT_NAME_BOLD = "Helvetica-Bold"

# --- Configuration ---
# These can be modified if needed
OUTPUT_FILENAME = _OUTPUT_FILENAME
IMAGE_DIR = _DEFAULT_IMAGE_DIR
FONT_DIR = _DEFAULT_FONT_DIR
FONT_NAME = _DEFAULT_FONT_NAME
FONT_NAME_BOLD = _DEFAULT_FONT_NAME_BOLD

# --- Directory Management ---

def _ensure_directory_exists(dir_path):
    """Creates a directory if it doesn't exist."""
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

# --- Font Handling ---

def _register_fonts():
    """Registers custom fonts from the FONT_DIR.

    Falls back to default fonts if registration fails.
    """
    global FONT_NAME, FONT_NAME_BOLD
    try:
        _ensure_directory_exists(FONT_DIR)  # Ensure font directory exists
        font_path = os.path.join(FONT_DIR, "Roboto-Regular.ttf")
        pdfmetrics.registerFont(TTFont("Roboto", font_path))
        font_path_bold = os.path.join(FONT_DIR, "Roboto-Bold.ttf")
        pdfmetrics.registerFont(TTFont("Roboto-Bold", font_path_bold))
        FONT_NAME = "Roboto"
        FONT_NAME_BOLD = "Roboto-Bold"
    except Exception as e:
        print(f"Font registration error: {e}. Using default fonts.")

# --- Style Definitions ---

def _create_styles():
    """Defines and returns a dictionary of paragraph and table styles."""
    styles = getSampleStyleSheet()

    base_style = ParagraphStyle(
        "BaseStyle",
        parent=styles["Normal"],
        fontName=FONT_NAME,
        fontSize=11,
        leading=14,
    )

    title_style = ParagraphStyle(
        "TitleStyle",
        parent=base_style,
        fontName=FONT_NAME_BOLD,
        fontSize=28,
        textColor=colors.darkblue,
        spaceAfter=0.75 * inch,
        alignment=1,
    )

    tagline_style = ParagraphStyle(
        "TaglineStyle",
        parent=base_style,
        fontName=FONT_NAME_BOLD,
        fontSize=18,
        textColor=colors.grey,
        spaceAfter=0.5 * inch,
        alignment=1,
    )

    heading_style = ParagraphStyle(
        "HeadingStyle",
        parent=base_style,
        fontName=FONT_NAME_BOLD,
        fontSize=14,
        spaceBefore=0.4 * inch,
        spaceAfter=0.2 * inch,
        textColor=colors.black,
    )

    body_style = ParagraphStyle("BodyStyle", parent=base_style, alignment=4)

    list_style = ParagraphStyle(
        "ListStyle",
        parent=base_style,
        leftIndent=0 * inch,
        spaceBefore=0,
    )

    table_style = TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
            ("FONTNAME", (0, 0), (-1, 0), FONT_NAME_BOLD),
            ("FONTSIZE", (0, 0), (-1, 0), 11),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("FONTNAME", (0, 1), (-1, -1), FONT_NAME),
            ("FONTSIZE", (0, 1), (-1, -1), 11),
            ("TOPPADDING", (0, 1), (-1, -1), 8),
            ("BOTTOMPADDING", (0, 1), (-1, -1), 8),
        ]
    )

    return {
        "base": base_style,
        "title": title_style,
        "tagline": tagline_style,
        "heading": heading_style,
        "body": body_style,
        "list": list_style,
        "table": table_style,
    }

# --- Content Creation ---

def _create_title_page(product_data: dict, styles: dict) -> list:
    """Generates content for the title page.
    
    Args:
        product_data: A dictionary containing product information.
        styles: A dictionary containing styles.
    """

    content = []
    content.append(Spacer(1, 2 * inch))
    content.append(Paragraph(product_data["name"], styles["title"]))
    content.append(Spacer(1, 0.25 * inch))
    content.append(Paragraph(product_data["tagline"], styles["tagline"]))
    content.append(PageBreak())

    return content

def _create_product_description(product_data: dict, styles: dict) -> list:
    """Generates content for the product description section.
    
    Args:
        product_data: A dictionary containing product information.
        styles: A dictionary containing styles.
    """
    content = []
    content.append(Paragraph("Product Description", styles["heading"]))
    for paragraph_text in product_data["description"].split("\n\n"):
        if paragraph_text.strip():
            content.append(Paragraph(paragraph_text, styles["body"]))
            content.append(Spacer(1, 0.1 * inch))
    content.append(Spacer(1, 0.5 * inch))
    return content

def _create_features_section(product_data: dict, styles: dict) -> list:
    """Generates content for the key features section.
    
    Args:
        product_data: A dictionary containing product information.
        styles: A dictionary containing styles.
    """
    content = []
    content.append(Paragraph("Key Features", styles["heading"]))
    features_list = [
        ListItem(Paragraph(feature, styles["list"]))
        for feature in product_data["features"]
    ]
    list_flowable = ListFlowable(
        features_list, bulletType="bullet", start="•", bulletFontSize=12, bulletIndent=5
    )
    content.append(Spacer(0.5 * inch, 0))
    content.append(list_flowable)
    content.append(Spacer(1, 0.5 * inch))
    return content

def _create_price_section(product_data: dict, styles: dict) -> list:
    """Generates content for the price section.
    
    Args:
        product_data: A dictionary containing product information.
        styles: A dictionary containing styles.
    """
    content = []
    content.append(Paragraph(f"Price: {product_data['price']}", styles["heading"]))
    return content


def create_content(product_data: dict) -> list:
    """Generates all the content for the PDF document.

    Args:
        product_data: A dictionary containing product information.

    Returns:
        A list of flowables representing the PDF content.
    """
    _register_fonts()  # Register fonts before creating styles
    styles = _create_styles()

    content = []
    content.extend(_create_title_page(product_data, styles))
    content.extend(_create_product_description(product_data, styles))
    content.extend(_create_features_section(product_data, styles))
    content.extend(_create_price_section(product_data, styles))


    return content


def generate_pdf(product_data, output_filename=OUTPUT_FILENAME) -> None:
    """Generates a PDF

    Args:
        product_data: A dictionary containing product information.
        output_filename: The path to the output PDF file.
    """ 
    doc = SimpleDocTemplate(output_filename, pagesize=letter)
    content = create_content(product_data)
    doc.build(content)
    print(f"PDF generated: {output_filename}")
