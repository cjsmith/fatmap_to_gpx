# FATMAP JSON to GPX

## Description

This is a simple Python script that converts FATMAP JSON to a GPX so you can create a GPX without being a Strava Premium member

### Running program

1. Checkout this repo or save the python file somewhere
1. Open up the route that you are interested in in FATMAP
1. In your brower's web developer tools network tab, look for a POST request to kraken.fatmap.com with a large size response JSON response in the body and confirm that the response has a format similar to the garibaldi_neve.json file in this repo.

1. Save the contents of that request to a JSON file

1. Run python3 fatmap_json_to_gpx.py FILE_NAME.json

## Help

File a ticket if you have a question or need help

## Authors

Colin Smith

https://github.com/cjsmith
