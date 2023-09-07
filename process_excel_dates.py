import pandas as pd
import re
from datetime import datetime

def standardize_date(date_str):
    # Convert to string if date_str is not already a string
    if not isinstance(date_str, str):
        date_str = str(date_str)
        
    if pd.isnull(date_str) or date_str == '':
        return date_str
    numbers = re.findall(r'\d+', date_str)
    if not numbers:
        return date_str
    if len(numbers) == 1:
        return numbers[0]
    elif len(numbers) == 2:
        return f"{numbers[0]}/{numbers[1].zfill(2)}"
    elif len(numbers) >= 3:
        return f"{numbers[0]}/{numbers[1].zfill(2)}/{numbers[2].zfill(2)}"


def process_excel_file(input_path, output_path):
    # Read the first sheet of the Excel file
    df = pd.read_excel(input_path, sheet_name=0)
    
    # Standardize the dates in column 'D'
    df['发布日期'] = df['发布日期'].apply(standardize_date)
    # df['D'] = df['D'].apply(standardize_date)
    
    # Save the modified DataFrame back to Excel
    df.to_excel(output_path, index=False)

# Example usage:
input_path = r"C:\Users\xiaoc\OneDrive\桌面\国内ESG相关政策搜集-Xu.xlsx"

output_path = r"C:\Users\xiaoc\OneDrive\桌面\国内ESG相关政策搜集-Xu_Processed.xlsx"

process_excel_file(input_path, output_path)
