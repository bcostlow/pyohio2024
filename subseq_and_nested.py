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

print("first, second, (*extra, [inner_first, inner_last]) = nested")
first, second, (*extra, [in_first, in_last]) = nested

print(first)
print(second)
print(extra)
print(in_first)
print(in_last)
