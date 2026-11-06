def parse_age_bad(text: str) -> int | None:
    try:
        age = int(txt)  # type: ignore[name-defined]  # typo on purpose
        return age
    except:  # bare except catches EVERYTHING, including the typo
        print("not a number")
        return None


def parse_age_good(text: str) -> int | None:
    try:
        age = int(txt)  # type: ignore[name-defined]  # same typo
        return age
    except ValueError:  # only the error we expect
        print("not a number")
        return None


print(parse_age_bad("21"))  # wrongly prints "not a number": the bug is hidden

try:
    print(parse_age_good("21"))
except NameError as e:  # only here so the file finishes running
    print(f"Real bug exposed: {e}")