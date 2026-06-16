import tkinter

from openfoodfacts_client import OpenFoodFactsClient
from food_product import FoodProduct
from food_logger import FoodLogger
from validators import validate_barcode
from exceptions import InvalidBarcodeError
from exceptions import ProductNotFoundError
from ai_explainer import AIExplainer


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
            data["allergens"]
        )

        result.insert(
            tkinter.END,
            "===== PRODUCT INFORMATION =====\n\n"
        )

        result.insert(
            tkinter.END,
            f"Name: {product.name}\n"
        )

        result.insert(
            tkinter.END,
            f"Barcode: {product.barcode}\n\n"
        )

        result.insert(
            tkinter.END,
            f"Ingredients:\n{product.ingredients}\n\n"
        )

        result.insert(
            tkinter.END,
            f"Allergens:\n{product.allergens}\n\n"
        )

        nutrients = product.nutrients

        sugar = nutrients.get(
            "sugars_100g",
            0
        )

        fat = nutrients.get(
            "fat_100g",
            0
        )

        salt = nutrients.get(
            "salt_100g",
            0
        )

        result.insert(
            tkinter.END,
            "===== NUTRITION ANALYSIS =====\n"
        )

        if sugar > 15:
            result.insert(
                tkinter.END,
                "High Sugar\n"
            )
        else:
            result.insert(
                tkinter.END,
                "Sugar Level Acceptable\n"
            )

        if fat > 10:
            result.insert(
                tkinter.END,
                "High Fat\n"
            )
        else:
            result.insert(
                tkinter.END,
                "Fat Level Acceptable\n"
            )

        if salt > 1:
            result.insert(
                tkinter.END,
                "High Salt\n"
            )
        else:
            result.insert(
                tkinter.END,
                "Salt Level Acceptable\n"
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