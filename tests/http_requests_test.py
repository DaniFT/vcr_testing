import vcr

from src.http_requests import get_data, post_data


@vcr.use_cassette('tests/cassettes/http_cassette.yaml')
def test_fetch_data():
    # When we call fetch_data, it will use the cassette file
    data = get_data()

    # Assert the data is as expected
    assert data == {"key": "value"}

@vcr.use_cassette('tests/cassettes/http_cassette.yaml')
def test_post_data():
    # When we call post_data, it will make a real HTTP request
    data = post_data({"key": "value"})

    # Assert the data is as expected
    assert data == {"message": "value updated"}
