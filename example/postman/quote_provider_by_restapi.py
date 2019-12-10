from http_client import HttpClient


class QuoteProviderByRestApi:
    def __init__(self, base_url):
        # base_url="http://localhost:8000/api/"
        headers = {"Content-type": "application/json"}
        self.all_users = HttpClient.get(base_url + "users/", headers=headers)
        self.all_quotes = HttpClient.get(base_url + "quotes/", headers=headers)

    def get_author(self, author_id):
        return [i["name"] for i in self.all_users if i["id"] == author_id][0]

    def get_quote(self):
        import random
        quote_src = random.choice(self.all_quotes)
        author = self.get_author(quote_src["author"])
        quote = {
            "content": quote_src["quote"],
            "number": quote_src["id"],
            "author": author
        }
        return quote


def main():
    q = QuoteProviderByRestApi("http://localhost:8000/api/")
    print(q.get_quote())


if __name__ == '__main__':
    main()
