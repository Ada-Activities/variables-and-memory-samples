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

    def sing(material):
        # verse is accessible due to enclosing scope
        return f"{verse}{material}"

    # sing could be expressed as a lambda
    # but it's even more pythonic to do this with a
    # list comprehension
        
    lines = map(sing, materials)
    print("\n".join(lines))

knock()


print(f"{little_pig_count=}")
