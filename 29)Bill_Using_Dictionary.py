""" Usinf Functions create a dictionary of products purchased and their MRPs. Calculate the bill and display to the customer."""

def Bill(prod):
    print("------------------ Product : MRP ------------------")
    for product, price in prod.items():
        print("--------------------" + product + " : " + str(price) + " --------------------")
    bill = 0
    for product, price in prod.items():
        bill += price
    print("Total Bill: ", bill)

products = {'Milk': 40, 'Bread': 30, 'Butter': 50, 'Cheese': 80, 'Eggs': 20}
Bill(products)