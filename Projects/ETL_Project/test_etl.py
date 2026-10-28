import pandas as pd
import os
import sys

# Ensure etl_pipeline can be imported
sys.path.append(os.path.dirname(__file__))
from etl_pipeline import extract_data, transform_data


def test_transform_data():
    raw_df = pd.DataFrame({
        'Title': ['Book A', 'Book B'],
        'Price_GBP': [12.99, 25.50],
        'Rating': ['Three', 'Five'],
        'Availability': ['In stock', 'In stock']
    })
    transformed = transform_data(raw_df)

    assert 'title' in transformed.columns
    assert 'price' in transformed.columns
    assert 'author' in transformed.columns
    assert list(transformed['title']) == ['Book A', 'Book B']
    assert list(transformed['price']) == [12.99, 25.50]
    assert list(transformed['author']) == ['Unknown', 'Unknown']


def test_extract_data(tmp_path):
    csv_file = tmp_path / "test_data.csv"
    sample_df = pd.DataFrame({'Title': ['Sample Book'], 'Price_GBP': [9.99]})
    sample_df.to_csv(csv_file, index=False)

    extracted = extract_data(str(csv_file))
    assert len(extracted) == 1
    assert extracted.iloc[0]['Title'] == 'Sample Book'
