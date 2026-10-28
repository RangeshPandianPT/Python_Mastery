#L -> E -> G -> B

#Local
def order():
    food = "Curd Rice"
    print ("Your oder is ", food)

order()


#Enclosing
def card():
    dicount=10

    def checkout():
        print("Applying Discount :",dicount)

    checkout()
card()


#Gobal
user_id = "Rangesh"

def homepage():
    print("Welcome to the homepage" , user_id)

def profile():
    print("Welcome to the profile page" , user_id)

homepage()
profile()


#Bulti_in
print(__file__)



#Example Code using all the 3 scope methods
delivery_partner="swiggy"

def hotel():
    item="pizza"

    def order_now():
        quantity=2
        print(f"ordering {quantity} {item} using {delivery_partner}")
    order_now()
hotel()

print (__file__)
