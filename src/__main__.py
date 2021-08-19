from pathlib import Path
import pandas as pd

TESTING_FILES_DIR = Path(__file__).parent.parent / "test_files"
TEST_MAP = TESTING_FILES_DIR / "test_map.xlsx"

if __name__ == "__main__":
    sheet_dictionary = pd.read_excel(TEST_MAP, sheet_name=None)
    blarg = "honk"