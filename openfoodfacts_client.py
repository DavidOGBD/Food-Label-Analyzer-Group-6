import requests


class OpenFoodFactsClient:

    def get_product(self, barcode):

        url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"

        headers = {
            "User-Agent": "FoodLabelAnalyzer/1.0"
        }

        response = requests.get(
            url,
            headers=headers
        )

        print("Status Code:", response.status_code)

        if response.status_code != 200:
            raise Exception(
                f"API Request Failed ({response.status_code})"
            )

        data = response.json()

        if data["status"] == 0:
            return None

        product = data["product"]

        return {
            "name": product.get(
                "product_name",
                "Unknown Product"
            ),

            "ingredients": product.get(
                "ingredients_text",
                "No Ingredients Found"
            ),

            "nutrients": product.get(
                "nutriments",
                {}
            ),

            "allergens": product.get(
                "allergens_tags",
                []
            )
        }
