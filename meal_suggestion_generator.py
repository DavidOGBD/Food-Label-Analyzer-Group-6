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
        ingredients = product.ingredients.lower()
        suggestions = []

        if "sugar" in ingredients:
            suggestions.extend(["Fruit Salad", "Oatmeal", "Greek Yogurt"])

        if "salt" in ingredients:
            suggestions.extend(["Vegetable Soup", "Fresh Salad", "Boiled Rice with Vegetables"])

        if not suggestions:
            suggestions.extend(["Fresh Fruits", "Grilled Chicken", "Vegetable Stir Fry"])

        return suggestions

    def display(self, product):
        """
        Print the healthier alternatives for a product.

        :param product: A FoodProduct object to generate suggestions for.
        """
        suggestions = self.generate(product)
        print("\n===== HEALTHIER ALTERNATIVES =====")
        for item in suggestions:
            print(f"• {item}")

