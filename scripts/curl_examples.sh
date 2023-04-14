curl -XPOST localhost:5000/addresses -d '{"name": "Whole Foods", "street": "100 Van Ness Avenue", "city": "San Francisco"}'
curl -XGET localhost:5000/addresses

curl -XPOST localhost:5000/packages -d '{"name": "Apples", "weight": 100, "addressId": 1}'
curl -XGET localhost:5000/packages
