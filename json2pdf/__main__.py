#!/usr/bin/env python3
import json
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm

def _create_styles():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="Title", fontName="Helvetica-Bold", fontSize=18,
                              leading=22, textColor=colors.HexColor("#1C2833"), spaceAfter=10))
    styles.add(ParagraphStyle(name="Heading", fontName="Helvetica-Bold", fontSize=12,
                              leading=16, textColor=colors.HexColor("#2E4053"), spaceBefore=8, spaceAfter=4))
    styles.add(ParagraphStyle(name="Body", fontName="Helvetica", fontSize=10.5,
                              leading=14, textColor=colors.black, leftIndent=12, spaceAfter=2))
    return styles

def _render_table(data_list, story):
    if not data_list:
        return
    headers = list(data_list[0].keys())
    table_data = [headers] + [[str(row.get(col, '')) for col in headers] for row in data_list]
    table = Table(table_data, hAlign="LEFT")
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#2E86C1")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#F4F6F7")]),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('FONTSIZE', (0, 0), (-1, -1), 9)
    ]))
    story.append(table)
    story.append(Spacer(1, 0.3 * cm))

def _render_json(data, story, styles, level=0):
    indent_style = ParagraphStyle(name=f"Indent_{level}", parent=styles["Body"], leftIndent=level * 15)
    if isinstance(data, dict):
        for key, value in data.items():
            story.append(Paragraph(f"<b>{key}</b>:", styles["Heading"]))
            _render_json(value, story, styles, level + 1)
    elif isinstance(data, list):
        if all(isinstance(item, dict) for item in data):
            _render_table(data, story)
        else:
            for item in data:
                _render_json(item, story, styles, level + 1)
    else:
        story.append(Paragraph(str(data), indent_style))

def json_to_pdf(json_input, output_pdf, title="JSON Report"):
    if isinstance(json_input, str):
        with open(json_input, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = json_input
    doc = SimpleDocTemplate(output_pdf, pagesize=A4, rightMargin=2*cm, leftMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)
    styles = _create_styles()
    story = [Paragraph(title, styles["Title"]), Spacer(1, 0.5 * cm)]
    _render_json(data, story, styles)
    doc.build(story)
    print(f"✅ PDF generated successfully: {output_pdf}")

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Convert JSON to PDF.")
    parser.add_argument("input", help="Path to the input JSON file")
    parser.add_argument("output", help="Path to the output PDF file")
    parser.add_argument("--title", default="JSON Report", help="Title for the PDF")
    args = parser.parse_args()
    json_to_pdf(args.input, args.output, args.title)

if __name__ == "__main__":
    main()
