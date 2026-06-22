# food_product.py - Member 3: Product Model

class FoodProduct:
    def __init__(self, barcode, name, brand, ingredients, allergens, nutrition, nutriscore=None, image_url=None):
        self.barcode = barcode
        self.name = name or "Unknown Product"
        self.brand = brand or "Unknown Brand"
        self.ingredients = ingredients or "No ingredients listed."
        self.allergens = allergens or []
        self.nutrition = nutrition or {}
        self.nutriscore = nutriscore.upper() if nutriscore else "N/A"
        self.image_url = image_url or "No image available."

    def _get_nutrient(self, key):
        value = self.nutrition.get(key)
        return f"{value}g" if value is not None else "N/A"

    def get_summary(self):
        return f"{self.name} by {self.brand} (Barcode: {self.barcode})"

    def get_nutrition_info(self):
        calories = self.nutrition.get("energy_kcal_100g", "N/A")
        return (
            f"  Calories : {calories} kcal\n"
            f"  Sugar    : {self._get_nutrient('sugars_100g')}\n"
            f"  Fat      : {self._get_nutrient('fat_100g')}\n"
            f"  Salt     : {self._get_nutrient('salt_100g')}"
        )

    def get_allergens(self):
        return ", ".join(self.allergens) if self.allergens else "No common allergens detected."

    def is_high_sugar(self):
        sugar = self.nutrition.get("sugars_100g")
        return sugar > 22.5 if sugar is not None else False

    def is_high_fat(self):
        fat = self.nutrition.get("fat_100g")
        return fat > 17.5 if fat is not None else False

    def is_high_salt(self):
        salt = self.nutrition.get("salt_100g")
        return salt > 1.5 if salt is not None else False

    def get_health_flags(self):
        flags = []
        if self.is_high_sugar(): flags.append("⚠️  High in Sugar")
        if self.is_high_fat(): flags.append("⚠️  High in Fat")
        if self.is_high_salt(): flags.append("⚠️  High in Salt")
        return flags

    def to_dict(self):
        return {
            "barcode": self.barcode,
            "name": self.name,
            "brand": self.brand,
            "ingredients": self.ingredients,
            "allergens": self.allergens,
            "nutrition": self.nutrition,
            "nutriscore": self.nutriscore,
            "image_url": self.image_url
        }

    def display(self):
        divider = "=" * 50
        print(divider)
        print("          🍽️  FOOD PRODUCT DETAILS")
        print(divider)
        print(f"  Product    : {self.name}")
        print(f"  Brand      : {self.brand}")
        print(f"  Barcode    : {self.barcode}")
        print(f"  Nutri-Score: {self.nutriscore}")
        print(f"\n📋 INGREDIENTS:\n  {self.ingredients}")
        print(f"\n⚠️  ALLERGENS:\n  {self.get_allergens()}")
        print(f"\n📊 NUTRITION (per 100g):\n{self.get_nutrition_info()}")

        flags = self.get_health_flags()
        if flags:
            print("\n🚦 HEALTH FLAGS:")
            for flag in flags: print(f"  {flag}")

        print(f"\n🖼️  Image: {self.image_url}")
        print(divider)


if __name__ == "__main__":
    product = FoodProduct(
        barcode="5000112548167",
        name="Chocolate Digestive Biscuits",
        brand="McVitie's",
        ingredients="Wheat flour, sugar, vegetable oil, cocoa powder, milk solids, soy lecithin.",
        allergens=["Milk", "Gluten", "Soy"],
        nutrition={"energy_kcal_100g": 450, "sugars_100g": 25.0, "fat_100g": 20.0, "salt_100g": 1.8},
        nutriscore="d",
        image_url="https://images.openfoodfacts.org/sample.jpg"
    )
    product.display()
