from markitdown import MarkItDown, UnsupportedFormatException
from pathlib import Path

def read(file):
    file = Path(file)

    if file.is_file():
        try:
            markitdown_engine = MarkItDown()
            conversion_result = markitdown_engine.convert(str(file))
            return conversion_result.text_content
        except UnsupportedFormatException:
            return f"{file} Uses an unsupported format, try exporting it in a different format."
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"
    else:
        return f"{file} Doesn't exist or isn't named correctly."