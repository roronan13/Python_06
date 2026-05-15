from ..elements import create_air
from elements import create_fire
import alchemy


def lead_to_gold() -> str:
    return (f"Recipe transmutting Lead to Gold : brew '{create_air()}' \
and '{alchemy.strength_potion()}' mixed with '{create_fire()}'")
