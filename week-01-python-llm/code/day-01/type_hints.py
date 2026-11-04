def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()


def average(scores: list[float]) -> float:
    return sum(scores) / len(scores)


def find_user(user_id: int, users: dict[int, str]) -> str | None:
    return users.get(user_id)


def count_passed(scores: list[int], passing_score: int = 40) -> int:
    count = 0
    for score in scores:
        if score >= passing_score:
            count += 1
    return count


def longest_word(words: list[str]) -> str | None:
    if not words:
        return None
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


print(greet("Sunny", 3))
print(average([90.5, 85.0, 78.5]))
print(find_user(1, {1: "Alice", 2: "Bob"}))
print(find_user(3, {1: "Alice", 2: "Bob"}))
print(count_passed([30, 45, 50, 20, 60], 40))
print(longest_word(["apple", "banana", "cherry"]))
print(longest_word([]))

# Deliberate wrong type: Python runs it, mypy flags it
# print(greet(123))  # type: ignore[arg-type]