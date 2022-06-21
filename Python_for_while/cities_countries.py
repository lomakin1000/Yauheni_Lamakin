



amount_countries = int(input("Enter the amount of countries: "))
dict_cc = {}
query = []
for i in range(amount_countries):
    country = input("Enter a country: ")
    amount_cities = int(input("Enter the amount of cities: "))
    cities = []
    for i in range(amount_cities):
        cities.append(input("Enter a city: "))
        dct_cc = {country: cities}
    dict_cc.update(dct_cc)
amount_queries = int(input("Enter the amount of queries: "))
for i in range(amount_queries):
    query.append(input("Enter the query: "))
for i in query:
    print(", ".join([country for country in dict_cc if i in dict_cc[country]]))


