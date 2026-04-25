# Configuration for Fitness Management Portal

# Class Types
CLASSES = {
    'yoga': {'duration': 60, 'capacity': 20},
    'pilates': {'duration': 60, 'capacity': 15},
    'zumba': {'duration': 45, 'capacity': 25},
    'strength_training': {'duration': 60, 'capacity': 15},
}

# Room Configurations
ROOMS = {
    'studio_a': {'capacity': 30, 'equipment': ['mats', 'weights']},
    'studio_b': {'capacity': 20, 'equipment': ['mats', 'bikes']},
    'gym': {'capacity': 50, 'equipment': ['weights', 'machines']},
}

# Pricing
PRICING = {
    'yoga': 15.00,
    'pilates': 20.00,
    'zumba': 10.00,
    'strength_training': 25.00,
}

# Time Constraints
TIME_CONSTRAINTS = {
    'opening_hours': {'start': '06:00', 'end': '22:00'},
    'duration_constraints': {'min': 30, 'max': 120},
}