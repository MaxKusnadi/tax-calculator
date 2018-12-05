import math

TAX_TIERS = {
    '0': {
        "accumulated_tax": 0,
        "lower_limit": 0,
        "upper_limit": 20000,
        "tax_rate": 0
    },
    '1': {
        "accumulated_tax": 0,
        "lower_limit": 20000,
        "upper_limit": 30000,
        "tax_rate": 0.02
    },
    '2': {
        "accumulated_tax": 200,
        "lower_limit": 30000,
        "upper_limit": 40000,
        "tax_rate": 0.035
    },
    '3': {
        "accumulated_tax": 550,
        "lower_limit": 40000,
        "upper_limit": 80000,
        "tax_rate": 0.07
    },
    '4': {
        "accumulated_tax": 3350,
        "lower_limit": 80000,
        "upper_limit": 120000,
        "tax_rate": 0.115
    },
    '5': {
        "accumulated_tax": 7950,
        "lower_limit": 120000,
        "upper_limit": 160000,
        "tax_rate": 0.15
    },
    '6': {
        "accumulated_tax": 13950,
        "lower_limit": 160000,
        "upper_limit": 200000,
        "tax_rate": 0.18
    },
    '7': {
        "accumulated_tax": 21150,
        "lower_limit": 200000,
        "upper_limit": 240000,
        "tax_rate": 0.19
    },
    '8': {
        "accumulated_tax": 28750,
        "lower_limit": 240000,
        "upper_limit": 280000,
        "tax_rate": 0.195
    },
    '9': {
        "accumulated_tax": 36550,
        "lower_limit": 280000,
        "upper_limit": 320000,
        "tax_rate": 0.20
    },
    '10': {
        "accumulated_tax": 44550,
        "lower_limit": 320000,
        "upper_limit": math.inf,
        "tax_rate": 0.22
    },
}
