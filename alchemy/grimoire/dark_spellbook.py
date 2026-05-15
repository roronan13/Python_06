import alchemy.grimoire.dark_validator


def dark_spell_allowed_ingredients() -> list[str]:
    return (["bats", "frog", "arsenic", "eyeball"])

def dark_spell_record(spell_name: str, ingredients: str) -> str:
    print("Testing record dark spell : ", end="")

    ingredient_validation: str = alchemy.grimoire.dark_validator.validate_ingredients(ingredients)

    if "INVALID" in ingredient_validation:
        return (f"Spell rejected: {spell_name} ({ingredient_validation})")
    else:
        return (f"Spell recorded: {spell_name} ({ingredient_validation})")
