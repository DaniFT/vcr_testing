# VCR & Testing

This project contains simple usage of VCR and testing in python. WIP

## VCR
VCR is a tool that records and replays HTTP requests and responses. It is used to test APIs and other HTTP requests. VCR works by intercepting HTTP requests and responses and saving them to a file. When you run your tests, VCR will check to see if it has a saved response for the request you are making. If it does, it will return the saved response instead of making the request to the API. If it does not have a saved response, it will make the request to the API and save the response for future use.

## Testing

Run the following command from the root directory to run the tests:

```bash

$ pytest tests/data_fetcher_test.py  

```
