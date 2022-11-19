import re

import orjson
import requests
from flask import Flask, render_template

from models import LegoSet, StoreItems

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Amazing scraper!"


@app.route("/3for2")
def three_for_two():

    url = "https://www.amazon.fr/promotion/psp/productInfoList"

    payload = "promotionId=A2KA67KJQ3R6VT&anti-csrftoken-a2z=hAMgDSD9FYYkbhw8hXtRSjxJGnRAlUmbeOptdWdAFBC%2FAAAAAGN400gAAAAB"

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'www.amazon.fr',
        'User-Agent': 'HTTPie'
    }

    cookies = {
        'session-id': '258-8434095-1415205',
        'ubid-acbfr': '260-4128488-8114845',
    }

    response = requests.post(
        url,
        data=payload,
        headers=headers,
        cookies=cookies
    )

    asobj = orjson.loads(response.content)

    product_list = asobj['viewModels']['PRODUCT_INFO_LIST']

    store_items = StoreItems()

    for product in product_list:
        LS = LegoSet(**product)
        s = re.search(r"(\d{4,6})", LS.title)
        LS.setNumber = s.group() if s else "unknown"
        store_items.items.append(LS)

    # return jsonify(store_items.dict()), 200
    return render_template(
        "show.jinja2",
        items=store_items.items
    )


if __name__ == "__main__":
    app.run()
