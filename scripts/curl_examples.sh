# Create an address
curl -XPOST localhost:5000/addresses -d '{"name": "Whole Foods", "street": "100 Van Ness Avenue", "city": "San Francisco"}'

# Get addresses
curl -XGET localhost:5000/addresses

# Create a package
curl -XPOST localhost:5000/packages -d '{"name": "Apples", "weight": 100, "address_id": 1}'

# Get packages
curl -XGET localhost:5000/packages
