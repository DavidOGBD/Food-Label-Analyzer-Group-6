class NutritionAnalyzer:

    def __init__(self, food_product):
        self.food_product = food_product
        self.nutriments = getattr(food_product, "nutrition", {})

    def get_nutrient_value(self, nutrient_key, default=0.0):

        value = (
            self.nutriments.get(f"{nutrient_key}_100g")
            or self.nutriments.get(nutrient_key)
        )

        try:
            return float(value) if value is not None else default

        except (ValueError, TypeError):
            return default

    def determine_sugar_level(self):

        sugars = self.get_nutrient_value("sugars")

        if sugars >= 22.5:
            return "High"

        elif sugars >= 5.0:
            return "Medium"

        return "Low"

    def determine_fat_level(self):

        fat = self.get_nutrient_value("fat")

        if fat >= 17.5:
            return "High"

        elif fat >= 3.0:
            return "Medium"

        return "Low"

    def determine_salt_level(self):

        salt = self.get_nutrient_value("salt")

        if salt >= 1.5:
            return "High"

        elif salt >= 0.3:
            return "Medium"

        return "Low"

    def analyze_nutrition(self):

        return {
            "sugar_level": self.determine_sugar_level(),
            "fat_level": self.determine_fat_level(),
            "salt_level": self.determine_salt_level(),
            "sugars_100g": round(
                self.get_nutrient_value("sugars"),
                2
            ),
            "fat_100g": round(
                self.get_nutrient_value("fat"),
                2
            ),
            "salt_100g": round(
                self.get_nutrient_value("salt"),
                2
            ),
            "energy_kcal_100g": round(
                self.get_nutrient_value("energy-kcal"),
                1
            ),
            "proteins_100g": round(
                self.get_nutrient_value("proteins"),
                2
            ),
            "carbohydrates_100g": round(
                self.get_nutrient_value("carbohydrates"),
                2
            ),
        }

    def generate_nutrition_report(self):

        analysis = self.analyze_nutrition()

        product_name = getattr(
            self.food_product,
            "name",
            "Unknown Product"
        )

        report_lines = [
            "",
            "===== NUTRITION ANALYSIS =====",
            "",
            f"Product: {product_name}",
            "",
            "Key Nutrients (per 100g):",
            f"- Calories: {analysis['energy_kcal_100g']} kcal",
            f"- Sugars: {analysis['sugars_100g']}g ({analysis['sugar_level']})",
            f"- Total Fat: {analysis['fat_100g']}g ({analysis['fat_level']})",
            f"- Salt: {analysis['salt_100g']}g ({analysis['salt_level']})",
            f"- Proteins: {analysis['proteins_100g']}g",
            f"- Carbohydrates: {analysis['carbohydrates_100g']}g",
            "",
            "Health Insights:"
        ]

        insights = []

        if analysis["sugar_level"] == "High":
            insights.append(
                "⚠️ High in sugars - may contribute to energy spikes."
            )

        if analysis["fat_level"] == "High":
            insights.append(
                "⚠️ High in fat - consider lower-fat options."
            )

        if analysis["salt_level"] == "High":
            insights.append(
                "⚠️ High in salt - watch for blood pressure impact."
            )

        if not insights:
            insights.append(
                "✅ Generally balanced profile."
            )

        for insight in insights:
            report_lines.append(
                f"- {insight}"
            )

        report_lines.append("")
        report_lines.append(
            "Note: Based on Open Food Facts data."
        )

        return "\n".join(report_lines)