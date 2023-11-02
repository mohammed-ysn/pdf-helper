# PDF Helper

This is a Python command-line tool for manipulating PDF files, allowing you to remove or keep specific ranges from a PDF document.

## Installation

To install the required dependencies for this tool, do the following:

1. Clone or download this repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies using `pip`:

```
pip install -r requirements.txt
```

## Usage

To use the tool, run the script from the command line with the desired action and options. The available actions are:

- `remove`: Remove specific page ranges from a PDF.
- `keep`: Keep specific page ranges from a PDF.

You can also provide an optional `--output` argument to specify the name of the output PDF file. If not provided, the tool will use a default suffix.

## Examples

### Remove Pages

```
python main.py remove input.pdf --output short.pdf 1-10 20-30
```

This will remove pages 1 to 10 and 20 to 30 from `input.pdf` and save the result to `short.pdf`.

### Keep Pages

```
python main.py keep input.pdf 5-10
```

This will keep only pages 5 to 10 from `input.pdf` and save the result to `input_modified.pdf`.
