# amazon-scraper

A toy web app I've created during the "Obtenez 3 au prix de 2." (3 for 2) promotion on Amzn FR site where you could buy great LEGO sets at a bargain price.

The whole idea was to monitor what sets go in and out as the item list was changing during the promotion.

## Steps

* Analyze the browser requests using Dev tools and `HTTPie`
* Identify API endpoint(s)
* Build the minimum-working request payload
* Turn incoming data structure into models (see `static/example_response.json`)
* Create single-route `Flask` web app
* Host on `Render`
* Hunt!

## Outcome

Hopefully the offer was not so interesting to me, therefore I haven't bought another new set this year 😅