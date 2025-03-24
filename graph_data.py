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