product=[{
    "product_name":"milk",
    "eclusive_price":50

},
{
    "product_name":"bread",
    "exclusive_price":40

},
{
    "product_name":"sugar",
    "exclusive_price":130
}


]

def calculate_VAT(exclusive_price,rate):
    inclusive_price=[]
    VAtamount=[]

    for x in exclusive_price:
        vat=x*rate
        VAtamount.append(vat)
        inclusive_price.append(x+vat)
    return[inclusive_price,VAtamount]
print(calculate_VAT([50,40,130],0.16))

    
