import tkinter

from openfoodfacts_client import OpenFoodFactsClient
from food_product import FoodProduct
from food_logger import FoodLogger
from validators import validate_barcode
from exceptions import InvalidBarcodeError
from exceptions import ProductNotFoundError
from ai_explainer import AIExplainer
from nutrition_analyzer import NutritionAnalyzer


def analyze_product():

    try:

        barcode = ent_barcode.get().strip()

        result.delete(
            "1.0",
            tkinter.END
        )

        if not validate_barcode(barcode):

            raise InvalidBarcodeError(
                "Invalid Barcode"
            )

        client = OpenFoodFactsClient()

        data = client.get_product(
            barcode
        )

        if data is None:

            raise ProductNotFoundError(
                "Product Not Found"
            )

        product = FoodProduct(
            data["name"],
            barcode,
            data["ingredients"],
            data["nutrients"],
            data["allergens"],
            data.get("brand", "Unknown Brand"),
            data.get("nutriscore", "N/A")
        )

        result.insert(
            tkinter.END,
            "===== FOOD PRODUCT DETAILS =====\n\n"
        )

        result.insert(
            tkinter.END,
            f"Product        : {product.name}\n"
        )

        result.insert(
            tkinter.END,
            f"Brand          : {product.brand}\n"
        )

        result.insert(
            tkinter.END,
            f"Barcode        : {product.barcode}\n"
        )

        result.insert(
            tkinter.END,
            f"Nutri-Score    : {product.nutriscore}\n\n"
        )

        result.insert(
            tkinter.END,
            f"Ingredients:\n{product.ingredients}\n\n"
        )

        result.insert(
            tkinter.END,
            f"Allergens:\n{product.allergens}\n\n"
        )

        result.insert(
            tkinter.END,
            NutritionAnalyzer(product).generate_nutrition_report()
        )

        result.insert(
            tkinter.END,
            "\n===== AI EXPLANATION =====\n\n"
        )

        try:

            ai = AIExplainer()

            explanation = ai.explain(
                product
            )

            result.insert(
                tkinter.END,
                explanation
            )

        except Exception as ai_error:
            result.insert(tkinter.END, f"AI temporarily unavailable:\n{ai_error}\n")

            result.insert(
                tkinter.END,
                f"AI Error:\n{ai_error}\n"
            )

        result.insert(
            tkinter.END,
            "\n\n===== HEALTHIER ALTERNATIVES =====\n"
        )

        ingredients = (
            product.ingredients.lower()
        )

        if "sugar" in ingredients:

            result.insert(
                tkinter.END,
                "• Fruit Salad\n"
            )

            result.insert(
                tkinter.END,
                "• Oatmeal\n"
            )

            result.insert(
                tkinter.END,
                "• Greek Yogurt\n"
            )

        elif "salt" in ingredients:

            result.insert(
                tkinter.END,
                "• Vegetable Soup\n"
            )

            result.insert(
                tkinter.END,
                "• Fresh Salad\n"
            )

            result.insert(
                tkinter.END,
                "• Boiled Rice with Vegetables\n"
            )

        else:

            result.insert(
                tkinter.END,
                "• Fresh Fruits\n"
            )

            result.insert(
                tkinter.END,
                "• Grilled Chicken\n"
            )

            result.insert(
                tkinter.END,
                "• Vegetable Stir Fry\n"
            )

        logger = FoodLogger()

        logger.save(
            product
        )

        result.insert(
            tkinter.END,
            "\n\nProduct saved successfully."
        )

    except InvalidBarcodeError as e:

        result.insert(
            tkinter.END,
            f"Error: {e}"
        )

    except ProductNotFoundError as e:

        result.insert(
            tkinter.END,
            f"Error: {e}"
        )

    except Exception as e:

        result.insert(
            tkinter.END,
            f"Error: {e}"
        )


screen = tkinter.Tk()

screen.title(
    "Food Label Analyzer"
)

screen.state(
    "zoomed"
)

heading = tkinter.Label(
    screen,
    text="FOOD LABEL ANALYZER"
)
heading.pack(
    pady=10
)

frame = tkinter.Frame(
    screen
)
frame.pack(
    pady=10
)

label = tkinter.Label(
    frame,
    text="Barcode"
)
label.pack(
    side="left"
)

ent_barcode = tkinter.Entry(
    frame,
    width=50
)
ent_barcode.pack(
    side="left",
    padx=10
)

button = tkinter.Button(
    frame,
    text="Analyze",
    command=analyze_product
)
button.pack(
    side="left"
)

result = tkinter.Text(
    screen
)
result.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)

screen.mainloop()