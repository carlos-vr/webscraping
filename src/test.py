import requests
import json


# Test petición madrid londres. 

headers = {
    'x-skyscanner-devicedetection-istablet': 'false',
    'origin': 'https://www.skyscanner.net',
    'accept-encoding': 'gzip, deflate, br',
    'x-skyscanner-mixpanelid': '169bc319f42ec-0682fa1b8bf5ca-36657905-1fa400-169bc319f4534f',
    'accept-language': 'es-ES,es;q=0.9,en;q=0.8,ca;q=0.7',
    'x-skyscanner-traveller-context': '330e3ad6-38be-47db-9b7a-997aa890dc1d',
    'x-skyscanner-viewid': '9f702099-0bf0-45b4-98d7-d603f9851375',
    'x-requested-with': 'XMLHttpRequest',
    'skyscanner-utid': '330e3ad6-38be-47db-9b7a-997aa890dc1d',
    'x-distil-ajax': 'azezcavtdrrxfqrtbw',
    'x-skyscanner-channelid': 'website',
    'x-skyscanner-devicedetection-ismobile': 'false',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'content-type': 'application/json; charset=UTF-8',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'referer': 'https://www.skyscanner.net/transport/flights/mad/lond/190331/?adults=1&children=0&adultsv2=1&childrenv2=&infants=0&cabinclass=economy&rtn=0&preferdirects=true&outboundaltsenabled=false&inboundaltsenabled=false&ref=home',
    'authority': 'www.skyscanner.net',
}

params = (
    ('geo_schema', 'skyscanner'),
    ('carrier_schema', 'skyscanner'),
    ('response_include', 'query;deeplink;segment;stats;fqs;pqs'),
)

data = '{"market":"UK","currency":"GBP","locale":"en-GB","cabin_class":"economy","prefer_directs":true,"trip_type":"one-way","legs":[{"origin":"MAD","destination":"LOND","date":"2019-03-31","add_alternative_origins":false,"add_alternative_destinations":false}],"origin":{"id":"MAD","airportId":"MAD","name":"Madrid","cityId":"MADR","cityName":"Madrid","countryId":"ES","type":"Airport","centroidCoordinates":[-3.563333,40.472222]},"destination":{"id":"LOND","name":"London","cityId":"LOND","cityName":"London","countryId":"UK","type":"City","centroidCoordinates":[-0.0943465343,51.5041174139]},"outboundDate":"2019-03-31","adults":1,"child_ages":[],"options":{"include_unpriced_itineraries":true,"include_mixed_booking_options":true},"state":{}}'

response = requests.post('https://www.skyscanner.net/g/conductor/v1/fps3/search/', headers=headers, params=params, data=data)



# parse to json:
response_json = json.loads(response.text)
#print(response_json)
#min_price = response_json[0]["stats"]["itineraries"]


print('min price:')
min_price = response_json["stats"]["itineraries"]["stops"]["direct"]["ticket"]["single_ticket"]["min_price"]
print(min_price)
