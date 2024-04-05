import vcr

from src.data_fetcher import fetch_data


@vcr.use_cassette('tests/cassettes/fetch_data_cassette.yaml')
def test_fetch_data():
    # When we call fetch_data, it will use the cassette file
    data = fetch_data()

    # Assert the data is as expected
    assert data == {"key": "value"}
