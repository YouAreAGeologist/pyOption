from src.options.types.option import Option

params = {
    'option': {
        'option_type': 'vanilla_european',
        'flag': 'call',
        's': 120,
        'x': 120,
        'r': 0.1,
        'b': 0.05,
        't': 0.5,
        'sigma': 0.25
    },
    'greeks': (
        'delta',
        'gamma',
        'theta'
    )
}

option = Option(params)
option.calculator.get_values()
print(option)
