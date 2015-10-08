from options.vanilla.src.vanilla_european_option import VanillaEuropeanOption

option = VanillaEuropeanOption('call', 10.0, 12.0, 0.1, 0.05, 0.25, 0.23)
print(option.get_value())