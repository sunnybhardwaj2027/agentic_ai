import json

def parse_age(text: str) -> int | None:
    try:
        age = int(text)
    except ValueError:
        print(f"'{text}' is not a number")
        return None
    if age < 0:
        raise ValueError(f"Age cannot be negative")
    return age

def safe_divide(a: float, b: float) -> float | None:
    try: 
        return a/b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None

def parse_json(text: str) -> dict | None:
    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        print(f"Bad JSON: {e}")
        return None

print(parse_age("21"))
print(parse_age("abc"))
print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(parse_json('{"name": "Alice", "age": 30}'))
print(parse_json("Not json"))

try:
    parse_age("-5")
except ValueError as e:
    print(f"Caught an error: {e}")