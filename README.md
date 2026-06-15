# Food Label Analyzer – Group Project

## Project Description

The Food Label Analyzer is a Python application that allows users to enter a food product barcode and retrieve detailed information about the product using the Open Food Facts API.

The application analyzes ingredients and nutritional information, identifies allergens, explains food labels in simple language, suggests healthier alternatives, and stores scanned products in a food log file for future reference.

This project demonstrates the use of:

- Object-Oriented Programming (OOP)
- File Handling (JSON)
- Exception Handling
- Regular Expressions (Regex)
- API Integration
- Data Analysis
- Team Collaboration using Git and GitHub

---

## Project Features

- Barcode validation using Regex
- Product retrieval from Open Food Facts API
- Nutrition analysis (Sugar, Fat, Salt)
- Allergen detection
- AI-style food label explanation
- Healthy meal suggestions
- Food log storage
- Error handling for invalid inputs and missing products

---

## Project Structure

Food-Label-Analyzer-Group-6/

├── main.py  
├── food_product.py  
├── openfoodfacts_client.py  
├── nutrition_analyzer.py  
├── ai_explainer.py  
├── meal_suggestion_generator.py  
├── food_logger.py  
├── validators.py  
├── exceptions.py  
├── requirements.txt  
└── README.md  

---

# Team Responsibilities

Each team member is responsible for a specific module.

## Member 1 – Project Leader

### Files:
- main.py
- requirements.txt

### Responsibilities:

- Integrate all project modules together
- Manage application workflow
- Handle user interaction
- Test the final application
- Maintain project dependencies in requirements.txt
- Manage GitHub repository
- Review and merge Pull Requests
- Ensure all modules work together correctly

---

## Member 2 – API Integration Developer

### File:
openfoodfacts_client.py

### Responsibilities:

- Connect to Open Food Facts API
- Send barcode requests
- Process API responses
- Handle API communication errors
- Extract product information

---

## Member 3 – Product Model Developer

### File:
food_product.py

### Responsibilities:

- Create the FoodProduct class
- Store product information
- Display product details
- Manage product attributes and methods

---

## Member 4 – Nutrition Analysis Developer

### File:
nutrition_analyzer.py

### Responsibilities:

- Analyze nutritional values
- Determine sugar levels
- Determine fat levels
- Determine salt levels
- Generate nutrition reports

---

## Member 5 – AI Explanation Developer

### File:
ai_explainer.py

### Responsibilities:

- Explain food labels in simple language
- Generate health summaries
- Interpret ingredient information
- Provide user-friendly recommendations

---

## Member 6 – Meal Suggestion Developer

### File:
meal_suggestion_generator.py

### Responsibilities:

- Suggest healthier alternatives
- Recommend meals based on product ingredients
- Generate food improvement suggestions
- Create alternative food recommendations

---

## Member 7 – Data Logging Developer

### File:
food_logger.py

### Responsibilities:

- Save scanned products to JSON files
- Maintain food history records
- Retrieve previously scanned products
- Manage file operations

---

## Member 8 – Validation & Exception Handling Developer

### Files:
- validators.py
- exceptions.py

### Responsibilities:

- Validate barcode inputs using Regular Expressions
- Detect invalid user inputs
- Create custom exception classes
- Handle application errors
- Improve program reliability
- Ensure invalid data is properly managed

---

# GitHub Workflow

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Food-Label-Analyzer-Group-6.git
```

### Step 2: Enter the Project Folder

```bash
cd Food-Label-Analyzer-Group-6
```

### Step 3: Get Latest Changes

```bash
git pull origin main
```

### Step 4: Create Your Branch

```bash
git switch -c your-name-module
```

Example:

```bash
git switch -c david-main
```

### Step 5: Open VS Code

```bash
code .
```

### Step 6: Complete Your Assigned Module

Edit only the file(s) assigned to you.

### Step 7: Save Your Work

```bash
git add .
git commit -m "Completed assigned module"
```

### Step 8: Push Your Branch

```bash
git push origin your-name-module
```

### Step 9: Create a Pull Request

- Open GitHub
- Select your branch
- Click **Compare & Pull Request**
- Submit the Pull Request to the Project Leader

---

# Contribution Requirements

Every member must:

- Create a GitHub account
- Clone the repository
- Create a personal branch
- Work on assigned file(s)
- Commit their changes
- Push their branch to GitHub
- Submit a Pull Request

This ensures every member's contribution can be tracked and verified by the Project Leader and Instructor.

---

# Expected Outcome

The completed application should allow users to:

1. Enter a product barcode
2. Retrieve food product information
3. Analyze nutrition content
4. Receive a simplified food label explanation
5. View healthier food alternatives
6. Detect allergens
7. Save products to a food log

The final project will demonstrate teamwork, software development practices, API integration, data processing, and Python programming concepts using a collaborative GitHub workflow.