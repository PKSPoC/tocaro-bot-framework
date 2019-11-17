import random


class QuoteProviderByFile:
    def __init__(self):
        with open("./HarukasQuotes.txt", "r") as f:
            self.haruka_quotes = f.readlines()

    def get_quote(self):
        quote = random.choice(list(enumerate(self.haruka_quotes)))
        quote_dict = {
            "number": quote[0] + 1,
            "content": quote[1]
        }
        return quote_dict


if __name__ == '__main__':
    q = QuoteProviderByFile()
    print(q.get_quote())
