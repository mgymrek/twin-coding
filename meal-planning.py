#!/usr/bin/env python3

# classes of things we need:
# Meal
# Recipes
# Ingredients
# Menu
# TODO: menu cost, add standard items to grocery list, ability to exclude some items from cost if we have them already

class Ingredient:
    def __init__(self, name, cost=0.0, unitsize=0.0, store="TBD"):
        self.name = name
        self.store = store
        self.cost = cost # cost per unit
        self.unitsize = unitsize # TBD. maybe g?
        
class Recipe:
    def __init__(self, name, ingredients={}):
        self.name = name
        self.ingredients = ingredients # ingredient -> number of units

    def GetCost(self):
        cost = 0.0
        for ing, amount in self.ingredients.items():
            cost += ing.cost*amount
        return cost
    
class Meal:
    def __init__(self, recipes=[]):
        self.recipes = recipes
        
    def GetCost(self):
        return sum([item.GetCost() for item in self.recipes])

class Menu:
    def __init__(self, meals=[]):
        self.meals = meals # List of meals
        self.UpdateIngredientTotals()

    def GetCost(self):
        return sum([item.GetCost() for item in self.meals])

    def UpdateIngredientTotals(self):
        self.ingredient_totals = {} # ingredient->total amount
        for meal in self.meals:
            for recipe in meal.recipes:
                for ingredient, amount in recipe.ingredients.items():
                    if ingredient in self.ingredient_totals:
                        self.ingredient_totals[ingredient] += amount
                    else: self.ingredient_totals[ingredient] = amount

    def PrintGroceryList(self):
        # Update ingredient list
        self.UpdateIngredientTotals()

        # Gather the ingredients for all stores
        store_lists = {} # store->list of ingredients
        for ingredient, amount in self.ingredient_totals.items():
            store = ingredient.store
            name = ingredient.name
            if store in store_lists.keys():
                store_lists[store].add(name)
            else:
                store_lists[store] = set([name])

        # Print the lists for each store
        for store in store_lists.keys():
            print("#### %s ######"%store)
            for ing in store_lists[store]:
                print(ing)

# Define stores
COSTCO = "costco"
TJ = "Trader Joe's"

# Define our ingredients
i_flour = Ingredient("flour", cost=0.0, unitsize=0.0, store=COSTCO)
i_eggs = Ingredient("eggs", cost=0.0, unitsize=0.0, store=COSTCO)
i_sugar = Ingredient("sugar", cost=0.0, unitsize=0.0, store=COSTCO)
i_orange_chicken = Ingredient("orange chicken", cost=0.0, unitsize=0.0, store=TJ)
i_rice = Ingredient("rice", cost=0.0, unitsize=0.0, store=COSTCO)
i_broccoli = Ingredient("broccoli", cost=0.0, unitsize=0.0, store=COSTCO)
i_salt = Ingredient("salt", cost=0.0, unitsize=0.0, store=TJ)

# Define our recipes
pancakes = Recipe("pancakes", ingredients={i_flour: 1, i_eggs: 1, i_sugar: 1, i_salt: 1})
orange_chicken = Recipe("orange chicken", ingredients={i_orange_chicken: 1})
rice = Recipe("rice", ingredients={i_rice: 1, i_salt: 1})
broccoli = Recipe("broccoli", ingredients={i_broccoli: 2})

# Define meals
test_meal = Meal(recipes=[pancakes, orange_chicken, broccoli, rice])

my_menu = Menu(meals=[test_meal])
my_menu.PrintGroceryList()
print("Total cost: %2.f"%my_menu.GetCost())
