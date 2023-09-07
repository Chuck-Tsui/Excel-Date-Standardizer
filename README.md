# Excel-Date-Standardizer

## Description

This Python script standardizes the date formats in a given Excel sheet. It specifically targets the dates in column "D" (or "发布日期") and formats them into a unified style (YYYY/MM/DD).

## Features

- Handles various date formats
- Skips non-date entries
- Works with Excel files

## Requirements

- Python 3.x
- Pandas
- Openpyxl (if you're dealing with `.xlsx` files)

## Installation

1. Clone this repository or download it as a ZIP file.
2. Open a terminal and navigate to the project directory.
3. Run `pip install -r requirements.txt` to install the required packages.

## Usage

1. Place your Excel file in the same directory as the script, or update `input_path` in the script with the full path to your Excel file.
2. Run `python process_excel_dates.py`.

Your processed Excel file will be saved in the same directory with "_Processed" appended to the original file name.

## Examples

**Before Running the Script**

| 发布日期           |
|-------------------|
| 2005.11.1         |
| 2002发布，2005及2010修订 |
| 2008              |

**After Running the Script**

| 发布日期    |
|------------|
| 2005/11/01 |
| 2002/2005/2010 |
| 2008       |

## Contributing

Feel free to open issues or pull requests if you have suggestions or bug-reports.

## License

MIT License
