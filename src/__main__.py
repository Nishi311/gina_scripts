from copy import deepcopy
from typing import Dict
import pandas as pd

from src.constants import *


def standardize_country_names(sheet_dictionary: pd.DataFrame) -> pd.DataFrame:
    for sheet_name, sheet_df in sheet_dictionary.items():
        if COUNTRY_COLUMN_NAME in sheet_df.columns:
            for primary_name, alias_list in COUNTRY_ALIAS_MAP.items():
                sheet_df[COUNTRY_COLUMN_NAME].replace(to_replace=alias_list, value=primary_name, inplace=True)
        else:
            raise KeyError(f"Given dataframe does not have the country column {COUNTRY_COLUMN_NAME}")
        sheet_dictionary[sheet_name] = sheet_df
    return sheet_dictionary


def export_sheets_to_excel_file(file_path: Path, sheet_dictionary: Dict[str, pd.DataFrame]) -> None:
    with pd.ExcelWriter(file_path) as writer:
        for sheet_name, sheet_df in sheet_dictionary.items():
            sheet_df.to_excel(writer, sheet_name=sheet_name, index=False)


def aggregated_information(sheet_dictionary: Dict[str, pd.DataFrame]) -> Dict:
    aggregated_info_dict = {}
    for sheet_name, sheet_df in sheet_dictionary.items():
        # Break down information to a country-by-country basis
        country_grouping = sheet_df.groupby(COUNTRY_COLUMN_NAME)

        for country_name, country_info in country_grouping:

            country_info_columns = list(country_info.columns)
            # Not interested in the country name since we already have that.
            country_info_columns.remove(COUNTRY_COLUMN_NAME)

            # Add the country to the dictionary if it doesn't already exist from some other sheet
            all_country_info = None
            if country_name not in aggregated_info_dict.keys():
                aggregated_info_dict[country_name] = {}
                all_country_info = {}
            else:
                all_country_info = aggregated_info_dict[country_name]

            for country_info_column in country_info_columns:
                if country_info_column not in all_country_info.keys():
                    all_country_info[country_info_column] = list(country_info[country_info_column])
                else:
                    all_country_info[country_info_column].append(list(country_info[country_info_column]))
            aggregated_info_dict[country_name] = all_country_info

    return aggregated_info_dict


if __name__ == "__main__":
    original_sheet_dictionary = pd.read_excel(TEST_MAP, sheet_name=None)
    changed_sheet_directory = deepcopy(original_sheet_dictionary)

    changed_sheet_directory = standardize_country_names(changed_sheet_directory)

    aggregated_df = aggregated_information(changed_sheet_directory)

    # export_sheets_to_excel_file(changed_sheet_directory)


    blarg = "honk"

