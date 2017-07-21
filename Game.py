def be_polite (sentence):
    words = sentence.split(" ")
    please = false
    for word in words:
        if word == "please":
            please = true
    if (please == false):
        print("How rude. You forgot to say please.")
        return sentence
    if (please == true):
        print("Cool")

def juice ():
    #type_of_juice = be_polite(input("Have some juice. Orange or apple? ->"))
    # be_polite(type_of_juice)
    type_of_juice = str(input("Have some juice. Orange or apple? ->"))
    if type_of_juice ==  "orange" or "orange juice" or "Orange juice" or "Orange" or "I would like orange juice" or "I would like some orange juice" or "I would like some orange juice, please":
        print ("You're out of store-bought orange juice, so you're going to have to squeeze it yourself.\nOUCH! You cut yourself squeezing the orange juice. Go get a band-aid!\nI guess you'll just have to drink apple juice.")
    if type_of_juice == "apple" or "apple juice" or "Apple" or "Apple juice" or "I would like apple juice" or "I would like some apple juice" or "I would like some apple juice, please":
        print ("You're in luck! You happen to have just enough apple juice left for one cup.\nYou're going to have to go to the store soon to buy more though.")

print ("Good morning! It's 10 AM on Saturday morning. What would you like to have for breakfast? ")
breakfast = str(input("eggs or bacon?->"))
if breakfast == "eggs" or "Eggs" or "I would like eggs" or "I want eggs" or "I would like some eggs" or "I would like some eggs, please":
    print ("Ok, that might take a while to cook.")
if breakfast == "bacon":
    print ("You forgot to buy bacon at the store yesterday so you're out of bacon.")
    store = str(input("Do you really want to go to the store just to buy bacon? Yes or no? ->"))
    if store == "yes" :
        print ("If you say so...\nYou get back a half hour later, starving and cranky. Time to fry that bacon.")
    if store == "no" :
        print ("You're very lazy... I guess you'll just have to eat eggs then.")
juice()
print("Finally, time to sit down for breakfast.")
