students = [('Ali', 85), ('Zara', 92), ('Bob', 78), ('Sara', 92)]

by_name = sorted(students, key=lambda x: x[0])
print(by_name)  # Sort by name

by_score_desc = sorted(students, key=lambda x: x[1], reverse=True)
print(by_score_desc)  # Sort by score in descending order

by_score_then_name = sorted(students, key=lambda x: (-x[1], x[0]))
print(by_score_then_name)  # Sort by score in descending order, then by name

