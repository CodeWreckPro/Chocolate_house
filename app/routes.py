from flask import current_app
import click
from .database import db
from .models import Flavor, Ingredient, CustomerFeedback, FlavorIngredient
from .utils import validate_season, validate_quantity

def init_cli(app):
    @app.cli.group()
    def chocolate():
        """Chocolate house management commands."""
        pass

    @chocolate.command()
    @click.argument('name')
    @click.argument('description')
    @click.argument('season')
    def add_flavor(name, description, season):
        """Add a new chocolate flavor."""
        if not validate_season(season):
            click.echo('Invalid season. Use Spring, Summer, Fall, or Winter.')
            return
        
        try:
            flavor = Flavor(name=name, description=description, season=season)
            db.session.add(flavor)
            db.session.commit()
            click.echo(f'Added flavor: {name}')
        except Exception as e:
            db.session.rollback()
            click.echo(f'Error adding flavor: {str(e)}')

    @chocolate.command()
    @click.argument('name')
    @click.argument('quantity', type=float)
    @click.argument('unit')
    @click.argument('min_stock', type=float)
    def add_ingredient(name, quantity, unit, min_stock):
        """Add a new ingredient to inventory."""
        if not validate_quantity(quantity):
            click.echo('Invalid quantity. Must be greater than 0.')
            return
        
        try:
            ingredient = Ingredient(
                name=name,
                quantity=quantity,
                unit=unit,
                min_stock_level=min_stock
            )
            db.session.add(ingredient)
            db.session.commit()
            click.echo(f'Added ingredient: {name}')
        except Exception as e:
            db.session.rollback()
            click.echo(f'Error adding ingredient: {str(e)}')

    @chocolate.command()
    @click.argument('description')
    @click.option('--allergy', help='Allergy concern')
    def add_feedback(description, allergy):
        """Add customer feedback or allergy concern."""
        try:
            feedback = CustomerFeedback(
                description=description,
                allergy_concern=allergy,
                suggestion_type='allergy' if allergy else 'suggestion'
            )
            db.session.add(feedback)
            db.session.commit()
            click.echo('Feedback recorded successfully')
        except Exception as e:
            db.session.rollback()
            click.echo(f'Error recording feedback: {str(e)}')

    @chocolate.command()
    def list_flavors():
        """List all chocolate flavors."""
        flavors = Flavor.query.all()
        if not flavors:
            click.echo('No flavors found')
            return
        
        for flavor in flavors:
            click.echo(f'{flavor.name} ({flavor.season}): {flavor.description}')

    @chocolate.command()
    def check_inventory():
        """Check current ingredient inventory."""
        ingredients = Ingredient.query.all()
        if not ingredients:
            click.echo('No ingredients found')
            return
        
        for ingredient in ingredients:
            status = 'LOW STOCK!' if ingredient.quantity <= ingredient.min_stock_level else 'OK'
            click.echo(f'{ingredient.name}: {ingredient.quantity} {ingredient.unit} ({status})')

    @chocolate.command()
    def view_feedback():
        """View all customer feedback."""
        feedback = CustomerFeedback.query.all()
        if not feedback:
            click.echo('No feedback found')
            return
        
        for item in feedback:
            click.echo(f'Type: {item.suggestion_type}')
            click.echo(f'Description: {item.description}')
            if item.allergy_concern:
                click.echo(f'Allergy: {item.allergy_concern}')
            click.echo('---')