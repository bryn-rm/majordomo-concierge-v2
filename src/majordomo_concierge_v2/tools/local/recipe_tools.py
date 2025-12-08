"""Recipe utilities for the Concierge agent."""

from __future__ import annotations

from ...memory.recipe_store import RecipeStore

store = RecipeStore()


def add_recipe(title: str, ingredients: str, instructions: str, tags: str = "") -> str:
    """Add a recipe to the local store."""
    recipe_id = store.add_recipe(title, ingredients, instructions, tags)
    return f"Recipe {recipe_id} saved."


def find_recipe(keyword: str) -> str:
    """Search recipes by keyword."""
    recipes = store.search(keyword)
    if not recipes:
        return "No recipes found."
    lines = []
    for title, instructions in recipes:
        lines.append(f"- {title}: {instructions[:140]}...")
    return "\n".join(lines)
