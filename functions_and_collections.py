from statistics import mean


def greet(name="student"):
    """Return a friendly greeting for the provided name."""
    return f"Hello, {name.title()}! Welcome back to Python practice."


def rectangle_area(width, height=1):
    """Calculate the area of a rectangle using a default height of 1."""
    return width * height


def convert_celsius_to_fahrenheit(celsius_values):
    """Convert a list of Celsius values to Fahrenheit using a list comprehension."""
    return [c * 9 / 5 + 32 for c in celsius_values]


def summarize_scores(scores):
    """Return summary statistics for a dictionary of student scores."""
    summary = {}
    for name, student_scores in scores.items():
        summary[name] = {
            "highest": max(student_scores),
            "lowest": min(student_scores),
            "average": mean(student_scores),
        }
    return summary


def inventory_demo():
    """Show common dictionary, tuple, and set operations."""
    inventory = {"apples": 3, "bananas": 1, "oranges": 2}
    inventory["bananas"] += 2
    inventory["grapes"] = 5

    sold_out = inventory.pop("oranges")
    unique_items = set(inventory.keys())

    favorite_languages = ("Python", "SQL", "Go")

    return {
        "inventory": inventory,
        "sold_out": sold_out,
        "unique_items": unique_items,
        "favorite_languages": favorite_languages,
    }


if __name__ == "__main__":
    print(greet())
    print(greet("alex"))

    print("\nRectangle areas:")
    print(f"Square with side 4: {rectangle_area(4)}")
    print(f"Rectangle 5x3: {rectangle_area(5, 3)}")

    print("\nTemperatures in Fahrenheit:")
    print(convert_celsius_to_fahrenheit([0, 20, 37, 100]))

    print("\nScore summary:")
    scores = {
        "Alice": [90, 85, 92],
        "Bob": [78, 81, 74],
        "Charlie": [88, 90, 86],
    }
    for name, data in summarize_scores(scores).items():
        print(f"{name}: highest={data['highest']}, lowest={data['lowest']}, average={data['average']:.1f}")

    print("\nCollections practice:")
    report = inventory_demo()
    print(f"Updated inventory: {report['inventory']}")
    print(f"Sold out count: {report['sold_out']}")
    print(f"Unique items: {sorted(report['unique_items'])}")
    print("Favorite languages:")
    for index, language in enumerate(report["favorite_languages"], start=1):
        print(f"  {index}. {language}")
