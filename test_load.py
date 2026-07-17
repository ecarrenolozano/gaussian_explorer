#!/usr/bin/env python3

"""Test script for CSV loading functionality."""

from gaussian_explorer.data import load_uploaded_csv

def test_csv_loading():
    """Test loading a simple CSV file."""
    try:
        dataset = load_uploaded_csv('test.csv')
        print('SUCCESS: Dataset loaded successfully!')
        print(f'Columns: {dataset.columns}')
        print(f'Rows: {dataset.row_count}')
        print('First row:', dataset.rows[0])
        return True
    except Exception as e:
        print(f'ERROR: {e}')
        return False

if __name__ == "__main__":
    test_csv_loading()