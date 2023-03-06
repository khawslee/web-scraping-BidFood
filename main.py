from BidFood import BidFood

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--product", help="Specify the product")
parser.add_argument("-i", "--id", help="Specify the productId")
parser.add_argument("-o", "--output", help="Specify the output file")
args = parser.parse_args()

if args.product and args.id:
    bidFood = BidFood(args.product, args.id)
    scrapProduct = bidFood.scrap_product()
    print(scrapProduct)
    # If output file is specified, write the scraped product to the file
    if args.output:
        with open(args.output, 'w') as f:
            f.write(scrapProduct)
else:
    print("Please specify the product name and productId")

# Sample code to call in python function
# bigFood = BidFood("oude-kaas-salade-50-gr-per-cupje-tray-12-cupjes","009567TR")
# getproduct = bigFood.scrap_product()

# getproduct is a json string
# print(getproduct)
