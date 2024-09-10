little_pig_count = 3

# little_pig_count is global scope, but print itself is
# built-in scope (there's no import of the name)

print(f"{little_pig_count=}")

