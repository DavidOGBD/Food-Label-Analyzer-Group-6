import os 
from dotenv import load_dotenv
import google.generativeai as genai
from exceptions import AIServiceError

class AIExplainer:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("GEMINI_API_KEY")
        print("API Key loaded successfully.")

        if not api_key:
            raise Exception("GEMINI_API_KEY not found in .env file.")
        
        self.model = genai.GenerativeModel("gemini-2.0-flash")

    def explain(self, product):
        """
        try Gemini AI first.
        if it fails, use offline fallback explanation.
        """
        try:
            return self._online_explanation(product)
        except Exception as e:
            print("Gemini Error:")
            # fallback instead of crashing the app
            return self._offline_explanation(product)
        
    # ONLINE AI (Gemini)
    def _online_explanation(self, product):
        prompt = f"""
                Explain the following product in simple language
                Product Name: {product.name}
                Ingredients: {product.ingredients}
                Allergens: {product.allergens}
                Nutritional Information: {product.nutrients}

                Please explain:
                - Whether the product is healthy or not
                - Sugar concerns
                - Fat concerns
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

        explanation = f"""
                OFFLINE ANALYSIS (AI Unavailable)
                Product: {product.name}
            """
        # Sugar Analysis
        if sugar > 15:
            explanation += "- High sugar content. This may contribute to weight gain and tooth decay.\n"
        elif sugar > 5:
            explanation += "- Moderate sugar content. Consume in moderation.\n"
        else:
            explanation += "- Low sugar content. This is generallygood for your health.\n"
            
        # Fat Analysis
        if fat > 10:
            explanation += "- High fat content. May not be ideal for frequent consumtion.\n"
        elif fat > 3:
            explanation += "- Moderate fat content.\n"
        else:
            explanation += "- Low fat content.\n"

        # Salt Analysis
        if salt > 1:
            explanation += "- High salt content. Can affect blood pressure if consumed often.\n"
        else:
            explanation += "- Salt levels are acceptable.\n"
            
        # Allergen Check
        if product.allergens:
            explanation += f"- Contains allergens: {product.allergens}. Be cautious if you have allergies.\n"

        # Simple Ingredient warnings
            if "sugar" in ingredients:
                explanation += "- Contains added sugar ingredients.\n"
                
            if "palm oil" in ingredients:
                explanation += "Contains palm oil, which is high in saturated fat.\n"

            explanation += """
                    GENERAL ADVICE:
                    - Try to eat processed foods in moderation.
                    - Drink plenty of water.
                    - Prefer fresh fruits and vegetables when possible.
                """
        return explanation