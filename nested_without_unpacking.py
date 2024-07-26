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

first = nested[0]
middle_second = nested[2][1]
inner_second = nested[2][2][1]

print(first)
print(middle_second)
print(inner_second)