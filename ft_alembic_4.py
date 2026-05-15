import alchemy

if __name__ == "__main__":
    print(" === Alembic 4 === ")

    print(f"Testing create_air : {alchemy.create_air()}")

    print("\nTesting the hidden create_earth : ", end="")
    print(f"{alchemy.create_earth()}")
