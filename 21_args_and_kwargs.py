def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1))

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123 Fake St",
              apt="100",
              city="Detroit",
              state="MI",
              zip="54321")
