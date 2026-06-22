class MealSuggestionGenerator:

    def generate(self, product):

        ingredients = product.ingredients.lower()

        print("\n===== HEALTHIER ALTERNATIVES =====")

        if "sugar" in ingredients:

            print("Fruit Salad")
            print("Oatmeal")
            print("Greek Yogurt")

        elif "salt" in ingredients:

            print("Vegetable Soup")
            print("Fresh Salad")
            print("Boiled Rice with Vegetables")

        else:

            print("Fresh Fruits")
            print("Grilled Chicken")
            print("Vegetable Stir Fry")