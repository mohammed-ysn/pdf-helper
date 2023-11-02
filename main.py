import argparse
import PyPDF2


def remove_pages(input_pdf, output_pdf, page_ranges_to_remove):
    print(
        f"Removing pages {page_ranges_to_remove} from {input_pdf} and saving to {output_pdf}"
    )

    pdf_writer = PyPDF2.PdfWriter()

    with open(input_pdf, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        total_pages = len(pdf_reader.pages)

        pages_to_remove = []
        for page_range in page_ranges_to_remove:
            start, end = page_range
            if 1 <= start <= end <= total_pages:
                pages_to_remove.extend(range(start - 1, end))
            else:
                print(f"Invalid page range: {page_range}. Skipping.")

        for page_num in range(total_pages):
            if page_num not in pages_to_remove:
                page = pdf_reader.pages[page_num]
                pdf_writer.add_page(page)

        with open(output_pdf, "wb") as output_file:
            pdf_writer.write(output_file)


if __name__ == "__main__":
    input_pdf = "/mnt/c/Users/moham/Downloads/routing.pdf"
    output_pdf = "/mnt/c/Users/moham/Downloads/short_routing.pdf"

    parser = argparse.ArgumentParser(
        description="Remove specific page ranges from a PDF."
    )
    parser.add_argument(
        "page_ranges_to_remove",
        nargs="+",
        type=lambda x: tuple(map(int, x.split("-"))),
        help="Page ranges to remove in the format 'start-end' (e.g., 1-10 20-30)",
    )
    args = parser.parse_args()
    page_ranges_to_remove = args.page_ranges_to_remove

    remove_pages(input_pdf, output_pdf, page_ranges_to_remove)
