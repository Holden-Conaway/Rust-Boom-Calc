print("Hello, Welcome to the rust boom calculator!")
print("I am assuming you are using a mixing table")


craftingRecipes = {
    "Satchel Charge":{
        "sulfur": 480,
        "charcoal": 480,
        "metal frags": 80,
        "rope" : 1,
        "small stash": 1
    },
    "Explo Ammo":{
        "metal frag": 5,
        "gunpowder": 10,
        "sulfur": 5
    },
    "Rocket":{
        "metal frags" : 100,
        "low grade" : 30,
        "sulfur": 1400,
        "charcoal": 1400,
        "metal pipe": 2
    },
    "C4":{
        "charcoal": 2000,
        "metal frags" : 200,
        "low grade" : 60,
        "sulfur": 2200,
        "cloth": 5,
        "tech trash": 2
    }
}

def calcResources(exploType, quantity):
    if exploType not in craftingRecipes:
        return f"Error that isn't a explosive type"
    
    recipe = craftingRecipes[exploType]

    totalResources = {resource: amount * quantity for resource, amount in recipe.items()}

    result = f"To craft {quantity} {exploType}(s), you need :\n"
    for resource, amount in totalResources.items():
        result += f"- {amount} {resource}\n"
    
    return result

explosive = input("Enter type of explosive (satchelCharge, Rocket, Explo Ammo, C4): ").strip()
quantity = int(input("Enter the quantity you want to craft: "))

result =  calcResources(explosive, quantity)
print(result)