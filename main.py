
import json
from utils.pdf_outline import extract_outline

def main(pdf_path, output_json):
    outline = extract_outline(pdf_path)
    with open(output_json, 'w') as f:
        json.dump(outline, f, indent=4)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python main.py <pdf_path> <output_json>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
