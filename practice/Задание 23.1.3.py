
cities = {"Риверхейвен": 458230, "Санстоун": 987124, "Эмберхолм": 572891}
largest_city = max(cities, key=cities.get)
print(f"Город с наибольшим населением: {largest_city}, население: {cities[largest_city]}")
