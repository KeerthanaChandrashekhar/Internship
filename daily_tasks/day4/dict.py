karnataka_foods = {
    "Mysore": "Mysore Pak",  
    "Bangalore": "Bisi Bele Bath",
    "Hubli": "girmit"
}
print(karnataka_foods)

print(karnataka_foods["Mysore"])


print(karnataka_foods.get("Mangaluru", "Food not found"))

karnataka_foods["Mangaluru"] = "Fish"
print("Updated Foods:", karnataka_foods)

karnataka_foods["Bangalore"] = "Dosa"
print("After Modification:", karnataka_foods)

print("Keys:", list(karnataka_foods.keys()))

del karnataka_foods['Hubli']
print("After deleting Hubli:", karnataka_foods)

mysore_food = karnataka_foods.pop("Mysore")
print("Popped food:", mysore_food)

new_foods = {"udupi": "Idli", "Shimoga": "Ragi Mudde"}

karnataka_foods.update(new_foods)
print("After adding new foods:", karnataka_foods)