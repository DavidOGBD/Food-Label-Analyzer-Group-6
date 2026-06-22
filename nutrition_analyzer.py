class NutritionAnalyzer:
    def __init__(self, product):
        self.product = product

    def _format_value(self, value):
        if value is None or value == "":
            return "N/A"
        try:
            value = float(value)
            if value.is_integer():
                return str(int(value))
            return f"{value:.1f}"
        except (TypeError, ValueError):
            return str(value)

    def _get_energy(self, nutrients):
        return (
            nutrients.get("energy-kcal_100g")
            or nutrients.get("energy_100g")
            or nutrients.get("energy-kcal_value")
            or nutrients.get("energy_value")
            or 0
        )

    def generate_nutrition_report(self):
        nutrients = getattr(self.product, "nutrients", {}) or {}
        energy = self._get_energy(nutrients)
        sugar = nutrients.get("sugars_100g", 0)
        fat = nutrients.get("fat_100g", 0)
        salt = nutrients.get("salt_100g", 0)
        proteins = nutrients.get("proteins_100g", 0)
        carbs = nutrients.get("carbohydrates_100g", 0)

        report = ""
        report += "Nutrition (per 100g):\n\n"
        report += f"- Calories: {self._format_value(energy)}kcal\n"
        report += f"- Sugars: {self._format_value(sugar)}g\n"
        report += f"- Total Fat: {self._format_value(fat)}g\n"
        report += f"- Salt: {self._format_value(salt)}g\n"
        report += f"- Proteins: {self._format_value(proteins)}g\n"
        report += f"- Carbohydrates: {self._format_value(carbs)}g\n\n"

        insights = ["Generally Balanced Profile"]
        if sugar and float(sugar) > 15:
            insights = ["High Sugar may require moderation"]
        elif fat and float(fat) > 10:
            insights = ["High Fat may require moderation"]
        elif salt and float(salt) > 1:
            insights = ["High Salt may require moderation"]

        report += "Health Insights:\n"
        for insight in insights:
            report += f"- {insight}\n"

        report += "\nNote: Based on Open Food Facts data\n\n"
        return report
