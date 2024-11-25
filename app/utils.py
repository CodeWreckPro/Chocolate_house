def validate_season(season):
    """Validate that the season is one of the four main seasons."""
    valid_seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    return season.capitalize() in valid_seasons

def validate_quantity(quantity):
    """Validate that the quantity is a positive number."""
    return quantity > 0

def check_allergen_conflicts(ingredients):
    """Check for common allergens in ingredients."""
    common_allergens = {
        'nuts': ['almond', 'hazelnut', 'peanut', 'walnut'],
        'dairy': ['milk', 'cream', 'butter', 'whey'],
        'soy': ['soy', 'lecithin'],
        'gluten': ['wheat', 'barley', 'rye']
    }
    
    found_allergens = []
    for ingredient in ingredients:
        for allergen, terms in common_allergens.items():
            if any(term in ingredient.lower() for term in terms):
                found_allergens.append(allergen)
    
    return list(set(found_allergens))