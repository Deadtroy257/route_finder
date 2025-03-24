# Graph configuration for the transport system
TRANSPORT_GRAPH = {
    'connections': [
        ('a', 'b', 5),
        ('b', 'c', 2),
        ('c', 'd', 10),
        ('a', 'e', 3),
        ('e', 'f', 2),
        ('f', 'd', 3),
        ('c', 'e', 1),
        ('b', 'f', 4),
        ('d', 'g', 2),
        ('e', 'g', 5)
    ]
}

KNOWLEDGE_BASE = {
    "rush_hour": True,   # Suponemos que es “hora pico”
    "holiday": False     # No estamos en día feriado
}

RULES = {
    "rush_hour_cost_increase": {
        "condition": lambda kb: kb["rush_hour"] is True,
        "action": lambda base_cost: base_cost * 1.2  # Aumenta 20%
    },
    "holiday_discount": {
        "condition": lambda kb: kb["holiday"] is True,
        "action": lambda base_cost: base_cost * 0.9  # Disminuye 10%
    }
}