import requests
from bs4 import BeautifulSoup
import json

class BidFood:
    def __init__(self, product, productId):
        self.product = product
        self.productId = productId
    
    def scrap_product(self):
        # Define the url
        URL = "https://www.bidfood.nl/webshop/product/"+self.product+"/_/A-productId-"+self.productId+"?singleResult=true"
        
        try:
            response = requests.get(URL)
            # Parse the html using beautiful soup and store in variable `soup`
            soap = BeautifulSoup(response.text, 'html.parser')
        except requests.exceptions.RequestException as e:
            print(e)
            return {}
        
        # Parse the product name
        productName = self.get_product_name(soap)
        # Parse the product description
        productDescription = self.get_product_description(soap)
        # Parse the nutrient table
        nutrients = self.get_product_nutrients(soap)
        # Combine all the data into BidFoodProduct object
        bidFoodProduct = BidFoodProduct(productName, productDescription, nutrients)
        # return json string
        return bidFoodProduct.toJSON()
    
    def get_product_name(self, soup):
        try:
            product_general_info = soup.find('div', attrs={'id': 'product-general-information'})
            productTitleHeader = product_general_info.find('header', attrs={'class': 'row-fluid page'})
            productTitle = productTitleHeader.find('h1')
            return productTitle.get_text()
        except Exception as e:
            print(e)
            return ""
    
    def get_product_description(self, soup):
        try:
            product_additional_info = soup.find('div', attrs={'id': 'product-additional-information'})
            productDescription = product_additional_info.find('div', attrs={'class': 'span9'})
            return productDescription.get_text()
        except Exception as e:
            print(e)
            return ""

    def get_product_nutrients(self, soup):
        try:
            nutrient_table = soup.find('table', attrs={'class': 'nutrient-list'})
            table_rows = nutrient_table.find_all('tr')
            nutrients = []
            for row in table_rows[1:]:
                cols = row.find_all('td')
                if len(cols) == 4:
                    nutrient = cols[0].text.strip()
                    quantity = cols[2].text.strip()
                    quantity = quantity.replace('\n', ' ')
                    nutrients.append(NutritionalValues(nutrient, quantity))
            return nutrients
        except Exception as e:
            print(e)
            return []
    
class BidFoodProduct:
    def __init__(self, title, description, nutritionalValues):
        self.title = title
        self.description = description 
        self.nutritionalValues = nutritionalValues
    
    def toJSON(self):
        try:
            return json.dumps(self, default=lambda o: o.__dict__, ensure_ascii=False)
        except Exception as e:
            print("An error occurred while converting object to JSON:", e)
            return "{}"

    
class NutritionalValues:
    def __init__(self, name, value):
        self.name = name
        self.value = value