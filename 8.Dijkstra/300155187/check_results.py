from dijkstra_tp import shortest, g

target = g.get_vertex('Johannesburg')
path = shortest(target)

expected = [
    'Toronto','New York','London','Paris',
    'Casablanca','Dakar','Lagos','Nairobi','Johannesburg'
]

if path == expected:
    print("✅ C’est excellent Mainouna, le chemin est correct !")
else:
    print("❌ Incorrect ")
    print("mon:", path)
    print("Chemin attendu:", expected)
