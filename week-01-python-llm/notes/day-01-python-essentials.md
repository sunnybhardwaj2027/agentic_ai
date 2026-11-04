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


## Dataclasses

### Concept (my own words)
`@dataclass` writes the boilerplate (`__init__`, `__repr__`, `__eq__`) for a class from its type-hinted fields, so I can group related data without writing it all by hand. It does not check types at runtime.

### Key points
- Fields without defaults must come before fields with defaults
- Simple defaults use `= value` (`True`, `0`, `"abc"`, `None`)
- Lists, dicts and sets use `field(default_factory=list)` (or `dict`, `set`)
- `==` compares by field values, and `print(obj)` shows a readable representation
- `frozen=True` makes an object read-only after creation
- `Student("Test", "not a number")` runs in Python; `mypy` flags it. Runtime validation needs Pydantic.

### Understanding `field(default_factory=list)`
```python
marks: list[int] = field(default_factory=list)
#  1        2              3
```
1. `marks` is the field name
2. `list[int]` is the type hint (a list of integers)
3. `field(default_factory=list)` is the default: "when no marks are given, create a new empty list for this object"

**Why not `= []`?** A list is mutable (it can change), and a default value is created once, when the class is defined, not each time an object is created. A plain `[]` would be one list shared by every object, so one student's marks could show up in another's record. Python raises a `ValueError` if I try it in a dataclass.

The same bug in a plain function:
```python
def add_mark(mark, marks=[]):   # the [] is created once
    marks.append(mark)
    return marks

add_mark(90)   # [90]
add_mark(80)   # [90, 80]  <- the old list was reused
```

**`default_factory`** means "a function that makes the value." `default_factory=list` calls `list()` for every new object, so each one gets its own separate list. It is `list` without brackets: I pass the function itself, I don't call it.

**Rule of thumb:** immutable defaults (`True`, `0`, `"abc"`, `None`) use `= value`. Mutable defaults (list, dict, set) use `field(default_factory=...)`.

### Minimal code example
```python
from dataclasses import dataclass, field

@dataclass
class Task:
    title: str
    done: bool = False
    tags: list[str] = field(default_factory=list)

    def summary(self) -> str:
        box = "[x]" if self.done else "[ ]"
        tags = ", ".join(self.tags) if self.tags else "none"
        return f"{box} {self.title} (tags: {tags})"
```

### Common mistakes
- Writing `tags: list[str] = []` (error: mutable default)
- Putting a field with a default before one without
- Writing `default_factory=list()` instead of `default_factory=list`
- Assuming a dataclass validates types when the program runs
- Ending lines with `;` (not needed in Python)
- Printing `(tags: )` for an empty list instead of handling the empty case

### My questions and answers
- Why can't I write `marks: list[int] = []`? The default is created once and shared by every object; `default_factory` gives each object its own new list.
- Did Python crash on a wrong type in a dataclass? No. Only `mypy` flagged it.

### Recall questions (answer without looking, one week later)
1. What three methods does `@dataclass` generate for you?
2. When do you need `field(default_factory=...)`, and why?
3. Does a dataclass check types at runtime? What will?
4. Why is it `default_factory=list` and not `default_factory=list()`?