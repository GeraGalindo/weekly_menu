from recipe import Recipe

class Day:
    def __init__(self, day):
        self._name = day
        self._recipes = []
        self._day_totals = {"Calories": 0,"Carbs": 0,"Fats": 0,"Protein": 0}

    def change_day(self, new_day):
        self._name = new_day

    def set_calories(self, calories):
        self._day_totals["Calories"] = calories

    def set_carbs(self, carbs):
        self._day_totals["Carbs"] = carbs

    def set_fats(self, fats):
        self._day_totals["Fats"] = fats

    def set_protein(self, protein):
        self._day_totals["Protein"] = protein

    def add_calories(self, calories):
        self._day_totals["Calories"] += calories

    def add_carbs(self, carbs):
        self._day_totals["Carbs"] += carbs

    def add_fats(self, fats):
        self._day_totals["Fats"] += fats

    def add_protein(self, protein):
        self._day_totals["Protein"] += protein

    def get_day_totals(self):
        return self._day_totals

    def add_recipe(self, recipe):
        self._recipes.append(recipe)
        self.add_nutrients(recipe)

    def add_nutrients(self, recipe):
        self.add_calories(recipe.get_calories())
        self.add_carbs(recipe.get_carbs())
        self.add_fats(recipe.get_fats())
        self.add_protein(recipe.get_protein())
