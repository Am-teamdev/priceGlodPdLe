import requests


class API:
    def __init__(self, api_key: str, url: str, *args):
        self.apiKey = api_key
        self.url =  url + '/' if url[-1] != '/' else url
        if args:
            for arg in args:
                self.url += '/' + arg


