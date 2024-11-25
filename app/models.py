from .database import db

class Flavor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text)
    season = db.Column(db.String(20))
    active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    ingredients = db.relationship('FlavorIngredient', back_populates='flavor')

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    unit = db.Column(db.String(20), nullable=False)
    min_stock_level = db.Column(db.Float, nullable=False)
    flavors = db.relationship('FlavorIngredient', back_populates='ingredient')

class FlavorIngredient(db.Model):
    flavor_id = db.Column(db.Integer, db.ForeignKey('flavor.id'), primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'), primary_key=True)
    quantity_required = db.Column(db.Float, nullable=False)
    flavor = db.relationship('Flavor', back_populates='ingredients')
    ingredient = db.relationship('Ingredient', back_populates='flavors')

class CustomerFeedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    suggestion_type = db.Column(db.String(50))
    description = db.Column(db.Text, nullable=False)
    allergy_concern = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)