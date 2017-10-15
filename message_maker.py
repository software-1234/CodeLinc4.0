import distance
import database

def getReply(message, from_number):
    message = message.lower().strip() 
    answer = ""

    if "transaction" in message:
        answer  = "here is your latest transaction"
    elif " near " in message:
        typeOfResource = message.split("near",1)[0]
        location = message.split("near",1)[1]
        catagory = ""
        if "food pantry" in typeOfResource:
            catagory = "Food Pantry"
        elif "summer meal" in typeOfResource:
            catagory = "Summer Meals"
        elif "education" in typeOfResource or "school" in typeOfResource:
            catagory = "Educational Resource"
        elif "free meal" in typeOfResource or "meal" in typeOfResource:
            catagory = "Free Meal"
        elif "convenience strore" in typeOfResource:
            catagory = "Convenience Store"
        elif "garden" in typeOfResource:
            catagory = "Community Garden"
        elif "backpack" in typeOfResource:
            catagory = "BackPack Program"
        elif "grocery" in typeOfResource or "coop" in typeOfResource or "co-op" in typeOfResource:
            catagory = "Grocery/Co-Op"
        elif "farm" in typeOfResource or "csa" in typeOfResource:
            catagory = "CSA Program"
        elif "mobile" in typeOfResource:
            catagory = "Mobile market"
        else:
            catagory = "all"
        
        latlng = database.get_home_address_by_phone(from_number)
        result = distance.get_distance(latlng, catagory)
        print(catagory)
        
        answer = "Closest "+ result[1][3] +" is "+result[1][1]+" on "+result[1][8]+", "+result[1][9]+". "
#        if result[1][7] != "":
#            answer += "Phone # is " +str(result[1][7]) + ". "
#        if result[1][12] != "":
#            answer += "Open on " +str(result[1][12]) + " "
#        if result[1][12] != "":
#            answer += " " +str(result[1][13])
    else:
        answer = "please try another question?"
    return answer
