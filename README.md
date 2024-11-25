# Chocolate House Management System

A Python-based management system for a fictional chocolate house that handles seasonal flavors, ingredient inventory, and customer suggestions/allergies.

## Features
- Manage seasonal chocolate flavors
- Track ingredient inventory
- Handle customer suggestions and allergy concerns
- SQLite database for data persistence
- Simple CLI interface for interaction

## Prerequisites
- Python 3.8 or higher
- SQLite3
- Docker (optional)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/CodeWreckPro/Chocolate_house.git
cd Chocolate_house
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

### Method 1: Direct Python Execution
```bash
python run.py
```

### Method 2: Using Docker
1. Build the Docker image:
```bash
docker build -t chocolate_house .
```

2. Run the container:
```bash
docker run -it chocolate_house
```

## Usage Guide

The application provides a command-line interface with the following options:

1. Manage Seasonal Flavors:
   - View all flavors
   - Add new flavors
   - Update existing flavors
   - Remove flavors

2. Inventory Management:
   - Check current inventory
   - Add new ingredients
   - Update quantities
   - Set low stock alerts

3. Customer Feedback:
   - Record flavor suggestions
   - Log allergy concerns
   - View feedback history

To use the application:

Clone the repository and install dependencies
Create chocolate.db and place in the instance folder using MySQL with the MySQL Database Schema provided
Run with Python directly or use Docker
Use the CLI commands to manage the chocolate house:
```bash
flask chocolate add-flavor "Dark Truffle" "Rich dark chocolate ganache" "Winter"
flask chocolate add-ingredient "Cocoa powder" 1000 "grams" 200
flask chocolate add-feedback "Love the dark truffles!" --allergy "nuts"
```

## Assumptions Made
1. Seasons: Four main seasons (Spring, Summer, Fall, Winter)
2. Allergies: Common allergens tracked (nuts, dairy, soy, gluten)
3. Inventory: Minimum stock levels defined for each ingredient
4. Flavors: Each flavor can be marked as seasonal or permanent

## Edge Cases Handled
1. Out of stock ingredients
2. Duplicate flavor entries
3. Invalid seasonal dates
4. Allergen conflicts
5. Input validation for quantities and dates

## Database Schema
- Flavors: id, name, description, season, active
- Ingredients: id, name, quantity, unit, min_stock_level
- CustomerFeedback: id, suggestion_type, description, allergy_concern
- FlavorIngredients: flavor_id, ingredient_id, quantity_required

## Notes for Evaluators
- The application uses SQLAlchemy ORM for database operations
- Input validation is implemented for all user inputs
- Error handling is in place for database operations
- Logging is implemented for tracking operations
