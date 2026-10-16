import os

from pdfminer.high_level import extract_text

PDFS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pdfs")


def extract_all():
    results = {}
    for name in sorted(os.listdir(PDFS_DIR)):
        if not name.endswith(".pdf"):
            continue
        path = os.path.join(PDFS_DIR, name)
        try:
            text = extract_text(path)
            results[name] = text.strip()
        except Exception:
            pass
    return results


def main():
    results = extract_all()


if __name__ == "__main__":
    main()
