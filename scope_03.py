little_pig_count = 3

def knock():
    print(f"There are {little_pig_count} little pigs.")

    # shows the use of some local variables
    verse = "I built my house of "
    materials = [
        "hay",
        "sticks",
        "bricks"
    ]

    lines = []
    for material in materials:
        lines.append(f"{verse}{material}")
    print("\n".join(lines))

knock()


print(f"{little_pig_count=}")

# this line would error, since verse is a function variable
# print(f"{verse=}")
