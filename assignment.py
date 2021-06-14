"""
Given a list of dictionaries containing data such as productName, exclPrice
passed to a function as a parameter, together with the Tax Rate.
Calculate the inclPrice of each products.
Then RETURN a list of dictionaries containing the product and their respective incl prices.
e.g 
#input
products = [
    {
        "productName" : "Milk",
        "exclPrice": 50
    },
    {
        "productName" : "Bread",
        "exclPrice": 40
    }
]

#Output
[
    {
        "productName" : "Milk",
        "inclPrice": 50
    },
    {
        "productName" : "Bread",
        "inclPrice": 40
    }
]"""

def calculateInclusivePrice(products,rate):
    incl={}
    for product in products:
        VAT=product["exclusive_price"]*rate
        incl=product["exclusive_price"]+VAT
        print(product,  " inclusive price: " + str(incl)+ " ")
       
p=[{
    "product_name":"milk",
    "exclusive_price":50

},
{
    "product_name":"bread",
    "exclusive_price":40

},
{
    "product_name":"sugar",
    "exclusive_price":130
}  ]      


calculateInclusivePrice(p,0.16)


