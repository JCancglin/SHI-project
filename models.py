class breweryModel:
    def __init__(self, brewery):
        self.breweryId = brewery.get('id')
        self.breweryName = brewery.get('name')
        self.breweryType = brewery.get('brewery_type')
        self.street = brewery.get('street')
        self.city = brewery.get('city')
        self.website = brewery.get('website_url')
    



