class InvalidBarcodeError(Exception):
    def __init__(self, message="Invalid barcode entered. Please check and try again."):
        super().__init__(message)


class ProductNotFoundError(Exception):
    def __init__(self, message="Product not found in database."):
        super().__init__(message)


class AIServiceError(Exception):
    def __init__(self, message="AI service is currently unavailable. Please try again later."):
        super().__init__(message)


class IncompleteNutritionDataError(Exception):
    def __init__(self, message="Nutrition data is incomplete or missing for this product."):
        super().__init__(message)
