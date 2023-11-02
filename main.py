import argparse
import os
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


def keep_pages(input_pdf, output_pdf, page_ranges_to_keep):
    print(
        f"Keeping pages {page_ranges_to_keep} from {input_pdf} and saving to {output_pdf}"
    )

    pdf_writer = PyPDF2.PdfWriter()

    with open(input_pdf, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        total_pages = len(pdf_reader.pages)

        pages_to_keep = []
        for page_range in page_ranges_to_keep:
            start, end = page_range
            if 1 <= start <= end <= total_pages:
                pages_to_keep.extend(range(start - 1, end))
            else:
                print(f"Invalid page range: {page_range}. Skipping.")

        for page_num in range(total_pages):
            if page_num in pages_to_keep:
                page = pdf_reader.pages[page_num]
                pdf_writer.add_page(page)

        with open(output_pdf, "wb") as output_file:
            pdf_writer.write(output_file)


def merge_pdfs(input_pdfs, output_pdf):
    pdf_merger = PyPDF2.PdfFileMerger()

    for pdf in input_pdfs:
        with open(pdf, "rb") as pdf_file:
            pdf_merger.append(pdf_file)

    with open(output_pdf, "wb") as output_file:
        pdf_merger.write(output_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Modify a PDF by removing or keeping specific page ranges."
    )
    parser.add_argument(
        "action",
        choices=["remove", "keep"],
        help="Specify whether to remove or keep specific page ranges.",
    )
    parser.add_argument("input_pdf", help="Input PDF file.")
    parser.add_argument(
        "--output",
        help="Name of output PDF file. If not provided, a default suffix will be used.",
    )
    parser.add_argument(
        "page_ranges",
        nargs="+",
        type=lambda x: tuple(map(int, x.split("-"))),
        help="Page ranges in the format 'start-end' (e.g., 1-10 20-30)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force overwrite of existing output file without confirmation.",
    )

    args = parser.parse_args()

    input_pdf = args.input_pdf
    base_dir = os.path.dirname(input_pdf)
    base_name, extension = os.path.splitext(os.path.basename(input_pdf))
    if args.output:
        output_pdf = os.path.join(base_dir, args.output)
        if not output_pdf.endswith(extension):
            output_pdf += extension
    else:
        print("No output file provided. Using default suffix 'modified'.")
        output_pdf = os.path.join(base_dir, f"{base_name}_modified{extension}")

    # Get confirmation from user before overwriting existing file
    if (not args.force) and os.path.exists(output_pdf):
        overwrite = input(f"File {output_pdf} already exists. Overwrite? (y/N): ")
        if overwrite.lower() != "y":
            print("Exiting.")
            exit()

    if args.action == "remove":
        remove_pages(input_pdf, output_pdf, args.page_ranges)
    elif args.action == "keep":
        keep_pages(input_pdf, output_pdf, args.page_ranges)

    # TODO: Add support for merging multiple PDFs
