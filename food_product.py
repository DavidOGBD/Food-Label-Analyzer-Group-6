class FoodProduct:

    def __init__(
        self,
        name,
        barcode,
        ingredients,
        nutrients,
        allergens,
        brand="Unknown Brand",
        nutriscore="N/A"
    ):
        self.name = name
        self.barcode = barcode
        self.ingredients = ingredients
        self.nutrients = nutrients
        self.allergens = allergens
        self.brand = brand
        self.nutriscore = nutriscore

    def display(self):

        print("\n===== PRODUCT INFORMATION =====")
        print("Name:", self.name)
        print("Brand:", self.brand)
        print("Barcode:", self.barcode)
        print("Nutri-Score:", self.nutriscore)
        print("Ingredients:", self.ingredients)

        if self.allergens:
            print("Allergens:", ", ".join(self.allergens))
        else:
            print("Allergens: None Listed")