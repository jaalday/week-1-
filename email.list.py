ramit = {
    "name": "Ramit",
    "email": "ramit@yourmom.com",
    "interests": ["movies", "tennis"],
    "friends": [
        {
            "name": "jasmine",
         "email": "jasmine@poop.com",
         "interests": ["Pics", "tennis"]
            
        },
        {
            "name": "jan",
            "email": "poopoopeepee@gmail.com",
            "interests": ["movies", "your mom"]
        }
    ]
    
}
print(ramit["email"])
print(ramit["interests"][0])
print(ramit ["friends"][0]["email"])
print(ramit["friends"][1]["interests"][1])

def friend_count(dictionary):
    total= len(dictionary["friends"])
    return total


ramit["friend_count"] = friend_count(ramit)

print(ramit)


    
    


# for friend in ramit:
    # print("Friend")