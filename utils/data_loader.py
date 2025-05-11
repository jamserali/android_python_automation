
import pandas as pd
import os

def get_file_path(relative_path: str) -> str:
    """
    Returns the absolute path to a file relative to the project's content root.
    :param relative_path: Path relative to the project root (e.g., 'data/testdata.csv')
    :return: Absolute path to the file
    """
    project_root = os.path.dirname(os.path.abspath(__file__))  # path of current file
    content_root = os.path.abspath(os.path.join(project_root, os.pardir))  # move up to root
    return os.path.join(content_root, relative_path)

def load_test_data(file_path, sheet_name=None):
    """
    Load test testdata from a CSV or XLSX file.
    :param file_path: Path to the file.
    :param sheet_name: Sheet name for XLSX files (ignored for CSV).
    :return: List of dictionaries containing row testdata.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    ext = os.path.splitext(file_path)[1].lower()

    if ext == '.csv':
        df = pd.read_csv(file_path)
    elif ext in ['.xlsx', '.xls']:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
    else:
        raise ValueError("Unsupported file format. Use .csv or .xlsx")
    return df.to_dict(orient='records')
