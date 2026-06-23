import os
from dotenv import load_dotenv
import google.generativeai as genai


class AIExplainer:

    def __init__(self):
        load_dotenv()

        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise Exception("GEMINI_API_KEY not found in .env file.")

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-2.0-flash")

    def explain(self, product):
        """Try Gemini AI first. If it fails, use offline fallback explanation."""
        try:
            return self._online_explanation(product)
        except Exception as e:
            print("Gemini Error:", e)
            return self._offline_explanation(product)

    # ONLINE AI (Gemini)
    def _online_explanation(self, product):
        prompt = f"""
Explain this food product in simple language.

Product Name:
{product.name}

Ingredients:
{product.ingredients}

Allergens:
{product.allergens}

Nutrition Information:
{product.nutrients}

Please explain:
- Whether the product is healthy or unhealthy
- Sugar concerns
- Fat concerns
- Salt concerns
- Allergen concerns
- Give simple health advice
"""
        response = self.model.generate_content(prompt)
        return response.text

    # OFFLINE FALLBACK AI
    def _offline_explanation(self, product):
        nutrients = product.nutrients
        sugar = nutrients.get("sugars_100g", 0)
        fat = nutrients.get("fat_100g", 0)
        salt = nutrients.get("salt_100g", 0)

        ingredients = product.ingredients.lower()

        explanation = f"OFFLINE ANALYSIS (AI unavailable)\n\nProduct: {product.name}\n\n"

        if sugar > 15:
            explanation += "- Sugar content: High sugar content. This may contribute to weight gain and tooth decay.\n"
        elif sugar > 5:
            explanation += "- Sugar content: Moderate sugar content. Consume in moderation.\n"
        else:
            explanation += "- Sugar content: Low sugar content. This is generally good.\n"

        if fat > 10:
            explanation += "- Fat content: High fat content. May not be ideal for frequent consumption.\n"
        elif fat > 3:
            explanation += "- Fat content: Moderate fat content.\n"
        else:
            explanation += "- Fat content: Low fat content.\n"

        if salt > 1:
            explanation += "- Salt levels: High salt content. Can affect blood pressure if consumed often.\n"
        else:
            explanation += "- Salt levels: Salt levels are acceptable.\n"

        if product.allergens:
            explanation += f"- Allergens: {', '.join(product.allergens)}. Be cautious if you have allergies.\n"

        if "sugar" in ingredients:
            explanation += "- Contains added sugar ingredients.\n"

        if "palm oil" in ingredients:
            explanation += "- Contains palm oil, which is high in saturated fat.\n"

        explanation += "\nGENERAL ADVICE:\n- Try to eat processed foods in moderation.\n- Drink plenty of water.\n- Prefer fresh fruits and vegetables when possible.\n"
        return explanation