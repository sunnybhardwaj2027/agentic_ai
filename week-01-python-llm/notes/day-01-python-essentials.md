# Day 1: Python essentials

## Type hints

### Concept (my own words)
Type hints are labels that say what type each parameter, variable and return value should be. Python ignores them when the program runs. Tools like `mypy` read them without running the code and report mismatches. Pydantic and FastAPI also use them, which matters later for validating LLM output.

### Key points
- Syntax: `name: str`, `def f(x: int = 1) -> str`, `list[float]`, `dict[int, str]`
- `X | None` means a value that may be missing (Python 3.10+)
- Python runs `greet(123)` without error because the f-string turns anything into text; `mypy` flags it because 123 is an `int`, not a `str`
- `dict.get(key)` returns `None` when the key does not exist, which is why `find_user` returns `str | None`
- Hints help editors, catch bugs before running, and document intent

### Minimal code example
```python
def find_user(user_id: int, users: dict[int, str]) -> str | None:
    return users.get(user_id)

name = find_user(3, {1: "Alice"})
if name is not None:   # handle the None case before using the value
    print(name.upper())
```

### Common mistakes
- Writing `println(...)` (Java) instead of `print(...)`
- Naming a variable `sum`, which hides Python's built-in `sum()`
- Using `;` at the end of lines (not needed in Python)
- Saving code inside `.venv` instead of the project folder
- Using `for l in list(scores)`: unnecessary copy and a confusing name (`l`); use `for score in scores`
- Expecting hints to stop bad calls at runtime (they don't)

### My questions and answers
- Why did Python not crash on `greet(123)` but `mypy` complained? Python ignores hints at runtime; `mypy` compares hints with the call without running the code.
- Why `str | None` and not `str`? `dict.get()` returns `None` for a missing key, and the hint warns callers to handle that.

### Recall questions (answer without looking, one week later)
1. Does Python enforce type hints at runtime? What checks them instead?
2. What does `-> str | None` tell the caller of a function?
3. What would `mypy` say about `count_passed(["a", "b"])`, and why?