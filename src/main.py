from recipe import Recipe
from day import Day

pollito = Recipe("Pollito")
huevito = Recipe("Huevito")

pollito.set_calories(500)
pollito.set_carbs(2)
pollito.set_fats(10)
pollito.set_protein(60)

huevito.add_ingeredient("Huevo", "4 Huevos")
huevito.add_ingeredient("Aceite", "7 g")
huevito.set_calories(360)
huevito.set_carbs(1)
huevito.set_fats(25)
huevito.set_protein(27)
print(huevito.get_ingredients())

day = Day("Monday")
day.add_recipe(pollito)
day.add_recipe(huevito)

print(day.get_day_totals())
