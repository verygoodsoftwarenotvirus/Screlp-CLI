from requests_oauthlib import OAuth1Session
import json

with open('creds.log', 'r') as creds:
    consumer_key = creds.readline().strip()
    consumer_secret = creds.readline().strip()
    token = creds.readline().strip()
    token_secret = creds.readline().strip()

yelp = OAuth1Session(consumer_key, consumer_secret, token, token_secret)

url = 'http://api.yelp.com/v2/search?category_filter=icecream&location=Austin'
response = yelp.get(url)
response = response.json()

with open('dump.txt', 'w') as file:
    json.dump(response, file, sort_keys=True, indent=4)


class Business:
    def __init__(self):
        self.name = None
        self.street = None
        self.city = None
        self.state = None
        self.zip = 00000
        self.rating = 0
        self.review_count = 0
        self.category = None

    def __repr__(self):
        return ("\nName: " + self.name + "\n" +
                "Address: " + self.address + "\n" +
                "City: " + self.city + "\n" +
                "State: " + self.state + "\n" +
                "Zip Code: " + self.zip + "\n" +
                "Rating: " + self.rating + "\n" +
                "Number of reviews = " + self.review_count + "\n"
                "Category: " + self.category + "\n")

results = []

for x in range(0, 40):
    business = Business()
    try:
        source = response['businesses'][x]
        business.name = source['name']
        if len(source['location']['display_address']) > 1:
            # handles addresses with things like unit or suite numbers
            business.address = source['location']['display_address'][0]
            business.address += "\n" + source['location']['display_address'][1]
        else:
            business.address = source['location']['display_address'][0]
        business.city = source['location']['city']
        business.state = source['location']['state_code']
        business.zip = source['location']['postal_code']
        business.rating = str(source['rating'])
        business.review_count = str(source['review_count'])
        business.category = source['categories'][0][0]
        results.append(business)
    except IndexError:
        break

print(results)
