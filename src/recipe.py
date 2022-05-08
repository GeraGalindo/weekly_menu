class Recipe:
    def __init__(self, name):
        self._name = name
        self._ingredients = {}
        self._instructions = ""
        self._nutritional_facts = {"Calories":0, "Carbs":0, "Fats":0, "Protein":0}

    def set_name(self, new_name):
        self._name = new_name

    def get_name(self):
        return self._name

    def add_ingeredient(self, ingredient, quantity):
        self._ingredients[ingredient] = quantity

    def remove_ingredient(self, ingredient):
        # TODO: Implement method
        pass

    def get_ingredients(self):
        return self._ingredients

    def add_instructions(self, instructions):
        self._instructions = instructions

    def get_instructions(self):
        return self._instructions

    def delete_instructions(self):
        self._instructions = ""

    def set_calories(self, calories):
        self._nutritional_facts["Calories"] = calories

    def set_carbs(self, carbs):
        self._nutritional_facts["Carbs"] = carbs

    def set_fats(self, fats):
        self._nutritional_facts["Fats"] = fats

    def set_protein(self, protein):
        self._nutritional_facts["Protein"] = protein

    def get_calories(self):
        return self._nutritional_facts["Calories"]

    def get_carbs(self):
        return self._nutritional_facts["Carbs"]

    def get_fats(self):
        return self._nutritional_facts["Fats"]

    def get_protein(self):
        return self._nutritional_facts["Protein"]

    def get_recipe_totals(self):
        return self._nutritional_facts
