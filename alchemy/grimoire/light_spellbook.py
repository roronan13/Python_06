from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    return (["earth", "air", "fire", "water"])


def light_spell_record(spell_name: str, ingredients: str) -> str:
    ingredient_validation: str = validate_ingredients(ingredients)

    if "INVALID" in ingredient_validation:
        return (f"Spell rejected: {spell_name} ({ingredient_validation})")
    else:
        return (f"Spell recorded: {spell_name} ({ingredient_validation})")
