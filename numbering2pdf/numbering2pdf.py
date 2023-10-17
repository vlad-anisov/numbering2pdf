from io import BytesIO
import os

from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from PyPDF4.pdf import PdfFileReader, PdfFileWriter

standard_fonts = (
    "Courier", "Courier-Bold", "Courier-Oblique", "Courier-BoldOblique",
    "Helvetica", "Helvetica-Bold", "Helvetica-Oblique", "Helvetica-BoldOblique",
    "Times-Roman", "Times-Bold", "Times-Italic", "Times-BoldItalic",
    "Symbol", "ZapfDingbats",
)

position_to_width = {
    "left": 10,
    "center": 38,
    "right": 65.5,
}


def add_numbering_to_pdf(pdf_file, new_pdf_file_path=None, position="center", start_page=1, end_page=None,
                         start_index=1, size=14, font="Times-Roman") -> bytes:
    """Adds numbering to pdf file"""
    pdf_file = get_pdf_file(pdf_file)
    original_pdf = PdfFileReader(BytesIO(pdf_file), strict=False)
    parameters = get_parameters_for_numbering(original_pdf, position, start_page, end_page, start_index, size, font)
    empty_numbered_pdf = create_empty_numbered_pdf(**parameters)
    new_pdf_file = merge_pdf_pages(original_pdf, empty_numbered_pdf)
    if new_pdf_file_path:
        save_file(new_pdf_file, new_pdf_file_path)
    return new_pdf_file


def get_pdf_file(pdf_file) -> bytes:
    """Path like string to file"""
    if isinstance(pdf_file, str):
        if isinstance(pdf_file, os.PathLike):
            pdf_file = os.fspath(pdf_file)
        file = open(pdf_file, "br")
        pdf_file = file.read()
        file.close()
    return pdf_file


def get_parameters_for_numbering(original_pdf, position, start_page, end_page, start_index, size, font) -> dict:
    """Setting parameters for numbering"""
    return {
        "width_of_pages": get_width_of_pages(original_pdf, position),
        "height": 15 * mm,
        "start_page": start_page - 1,
        "end_page": end_page or original_pdf.getNumPages() + 1,
        "start_index": start_index,
        "size": size,
        "font": font,
        "number_of_pages": original_pdf.getNumPages(),
    }


def get_width_of_pages(original_pdf, position) -> list:
    """Returns width of pages"""
    width_of_pages = []
    for index in range(original_pdf.getNumPages()):
        ratio = original_pdf.getPage(index).mediaBox.getWidth() / 200 #< CAUTION: returns Decimal that, strange enough
        width = position_to_width[position] * float(ratio) * mm       #< ... can't be multiplied by floats!
        width_of_pages.append(width)
    return width_of_pages


def create_empty_numbered_pdf(width_of_pages, height, start_page, end_page, start_index, size, font,
                              number_of_pages) -> PdfFileReader:
    """Returns empty pdf file with numbering only"""
    empty_canvas = canvas.Canvas("empty_canvas.pdf")
    for index in range(number_of_pages):
        empty_canvas.setFont(font, size)
        if index in range(start_page, end_page):
            number = str(index - start_page + start_index)
            empty_canvas.drawString(width_of_pages[index], height, number)
        else:
            empty_canvas.drawString(width_of_pages[index], height, "")
        empty_canvas.showPage()
    return PdfFileReader(BytesIO(empty_canvas.getpdfdata()))


def merge_pdf_pages(first_pdf, second_pdf) -> bytes:
    """Returns file with combined pages of first and second pdf"""
    writer = PdfFileWriter()
    for number_of_page in range(first_pdf.getNumPages()):
        page_of_first_pdf = first_pdf.getPage(number_of_page)
        page_of_second_pdf = second_pdf.getPage(number_of_page)
        page_of_first_pdf.mergePage(page_of_second_pdf)
        writer.addPage(page_of_first_pdf)
    result = BytesIO()
    writer.write(result)
    return result.getvalue()


def save_file(new_pdf_file, new_pdf_file_path) -> None:
    """Saves file with new file name"""
    with open(new_pdf_file_path, "bw") as file:
        file.write(new_pdf_file)
