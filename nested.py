
nested = [
    'outer_first',
    'outer_second',
    [
        'middle_first',
        'middle_second',
        [
            'inner_first',
            'inner_second',
        ]
    ]
]

# unpacking the outer list
print("Unpacking the outer list.")

first, second, third = nested

print(first)
print(second)
print(third)

# unpacking the outer and middle list

print("\nUnpacking the outer and middile list.")

first, second, (middle_first, middle_second, middle_third) = nested

print(first)
print(second)
print(middle_first)
print(middle_second)
print(middle_third)

print("\nUnpacking the outer, middile and inner list.")

first, second, (middle_first, middle_second, (inner_first, inner_second)) = nested

print(first)
print(second)
print(middle_first)
print(middle_second)
print(inner_first)
print(inner_second)

print("\nSquare brackets")

first, second, [middle_first, middle_second, [inner_first, inner_second]] = nested

print(first)
print(second)
print(middle_first)
print(middle_second)
print(inner_first)
print(inner_second)

print("\nParens & square brackets for clarity")

first, second, [middle_first, middle_second, (inner_first, inner_second)] = nested

print(first)
print(second)
print(middle_first)
print(middle_second)
print(inner_first)
print(inner_second)