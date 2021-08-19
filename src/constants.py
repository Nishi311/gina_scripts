from pathlib import Path
TESTING_FILES_DIR = Path(__file__).parent.parent / "test_files"
TEST_MAP = TESTING_FILES_DIR / "test_map.xlsx"

TEST_OUTPUT_FILE = TESTING_FILES_DIR / "results.xlsx"
COUNTRY_ALIAS_MAP = {
    "United States of America": ["United States of America", "USA", "America", "United States"],
    "Japan": ["Japan"],
    "United Kingdom": ["United Kingdom", "UK"],
    "Germany": ["Germany"],
}

COUNTRY_COLUMN_NAME = "Country"
SITE_COLUMN_NAME = "SITE"
PHYSICIAN_COLUMN_NAME = "Physician"
