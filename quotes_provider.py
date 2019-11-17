from quote_provider_by_file import QuoteProviderByFile


class QuoteProvider:
    def __init__(self, provider):
        self.provider = provider

    def get_quote(self):
        return self.provider.get_quote()
