"""
Meal Suggestion Generator Module
Suggests healthier food alternatives based on a product's ingredients.
"""


class MealSuggestionGenerator:
    """Generates healthier meal alternatives based on a product's ingredients."""

    def generate(self, product):
        """
        Build a list of healthier alternatives based on the product's ingredients.

        :param product: A FoodProduct object containing an 'ingredients' attribute.
        :return: A list of recommended healthier meals.
        """
        # Convert ingredients to lowercase so the search is case-insensitive
        ingredients = product.ingredients.lower()

        # Start with an empty list to collect our suggestions
        suggestions = []

        # If the product contains sugar, add low-sugar alternatives
        if "sugar" in ingredients:
            suggestions.append("Fruit Salad")
            suggestions.append("Oatmeal")
            suggestions.append("Greek Yogurt")

        # If the product contains salt, add low-salt alternatives
        if "salt" in ingredients:
            suggestions.append("Vegetable Soup")
            suggestions.append("Fresh Salad")
            suggestions.append("Boiled Rice with Vegetables")

        # If nothing was added, the list is still empty — give general suggestions
        if not suggestions:
            suggestions.append("Fresh Fruits")
            suggestions.append("Grilled Chicken")
            suggestions.append("Vegetable Stir Fry")

        # Return the finished list so other parts of the program can use it
        return suggestions

    def display(self, product):
        """
        Print the healthier alternatives for a product.

        :param product: A FoodProduct object to generate suggestions for.
        """
        # Call our own generate() method to get the list of suggestions
        suggestions = self.generate(product)

        print("\n===== HEALTHIER ALTERNATIVES =====")

        # Loop through each suggestion and print it
        for item in suggestions:
            print(item)