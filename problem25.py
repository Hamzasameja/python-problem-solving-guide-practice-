def print_profile(**kwargs):
    if 'name' not in kwargs:
        print("Error: 'name' is a required argument.")
        return

    parts = []
    for key, value in kwargs.items():
        parts.append(f"{key.title()}: {value}")
    print(" | ".join(parts))

print_profile(name="Talha", age=22, city="Lahore")
print_profile(age=22, city="Lahore")  # This will print an error message