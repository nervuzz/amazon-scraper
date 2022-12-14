import orjson
import requests
from flask import Flask, render_template

from models import StoreItems

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Amazing scraper!"


@app.route("/3for2")
def three_for_two():
    """Landing page."""

    from config import url, payload, headers, cookies

    data_source = "ONLINE"
    response = requests.post(
        url,
        data=payload,
        headers=headers,
        cookies=cookies
    )

    try:
        asobj = orjson.loads(response.content)
    except orjson.JSONDecodeError:
        with open(r"static/example_response.json", "r") as fh:
            asobj = orjson.loads(fh.read())
        data_source = "EXAMPLE"
    finally:
        product_list = asobj["viewModels"]["PRODUCT_INFO_LIST"]

    store_items = StoreItems()
    store_items.from_product_list(product_list)

    return render_template(
        "show.jinja2",
        items=store_items.items,
        data_source=data_source
    )


if __name__ == "__main__":
    app.run()
