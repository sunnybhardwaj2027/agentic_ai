import json


def get_with_retry(attempts: list[str], max_tries: int = 3) -> dict | None:
    for i in range(max_tries):
        if i >= len(attempts):
            print("No more attempts left")
            return None
        attempt = attempts[i]
        try:
            return json.loads(attempt)
        except json.JSONDecodeError:
            print(f"Attempt {i + 1} failed")
    return None  # outside the loop: runs only after every try has failed


# Test 1: should succeed on attempt 3
print(get_with_retry(["oops", "{bad", '{"city": "Delhi"}']))

# Test 2: every reply is broken
print(get_with_retry(["oops", "{bad", "still bad"]))

# Test 3: good reply is the 3rd, but we only allow 2 tries
print(get_with_retry(["oops", "{bad", '{"city": "Delhi"}'], max_tries=2))