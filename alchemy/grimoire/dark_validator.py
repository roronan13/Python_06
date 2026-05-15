from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed_ingredients: list[str] = dark_spell_allowed_ingredients()
    low_ingredients: str = ingredients.lower()

    for allowed_ingredient in allowed_ingredients:
        if allowed_ingredient in low_ingredients:
            return (f"{ingredients} -- VALID")
    return (f"{ingredients} -- INVALID")
