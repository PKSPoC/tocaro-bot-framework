from quote_provider_by_file import QuoteProviderByFile
from quote_provider_by_restapi import QuoteProviderByRestApi


class QuoteProvider(QuoteProviderByRestApi):
    def __init__(self):
        super(QuoteProvider, self).__init__("http://localhost:8000/api/")

    def get_quote(self):
        return super().get_quote()
