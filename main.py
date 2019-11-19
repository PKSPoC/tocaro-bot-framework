from quotes_provider import QuoteProvider
from tocaro_handler import TocaroHandler


def lambda_handler(event, context):
    harukas = QuoteProvider()

    tocaro = TocaroHandler()
    quote = harukas.get_quote()

    tocaro.set_text("はるかの言い間違いコレクション No.{0}".format(str(quote["number"])))
    tocaro.set_color("danger")
    tocaro.set_attachments(
        [{
            "title:": "None",
            "value": quote["content"]
        }]
    )

    r = tocaro.send2tocaro()
    return r


if __name__ == '__main__':
    lambda_handler(None, None)
