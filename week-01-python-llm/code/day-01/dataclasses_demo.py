from dataclasses import dataclass, field


@dataclass
class Student:
    name: str
    age: int
    marks: list[int] = field(default_factory=list)  # new empty list for each object
    active: bool = True                             # simple default

    def average(self) -> float:
        if not self.marks:
            return 0.0
        return sum(self.marks) / len(self.marks)


@dataclass
class Task:
    title: str
    done: bool = False
    tags: list[str] = field(default_factory=list)

    def summary(self) -> str:
        box = "[x]" if self.done else "[ ]"
        tags = ", ".join(self.tags) if self.tags else "none"
        return f"{box} {self.title} (tags: {tags})"


# --- Student demo ---
s1 = Student("Sunny", 20, [85, 90, 70])
s2 = Student("Sunny", 20, [85, 90, 70])
s3 = Student("Rainy", 22)

print(s1)
print(s1 == s2)          # True: compared by field values
print(s3.average())      # 0.0: no marks yet
print(s1.average())

s3.marks.append(95)
print(s3)

# default_factory check: each object gets its own list
a = Student("A", 20)
b = Student("B", 21)
a.marks.append(100)
print(a.marks, b.marks)  # [100] []  -> b is not affected

# Deliberate wrong type: Python runs it, mypy flags it
wrong = Student("Test", "not a number")  # type: ignore[arg-type]
print(wrong)

# --- Task demo ---
task1 = Task("Write notes", True, ["python", "week-01"])
task2 = Task("Review code")

print(task1.summary())
print(task2.summary())
