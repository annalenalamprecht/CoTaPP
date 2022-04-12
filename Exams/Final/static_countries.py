import json

def get_country_names():
    with open('european_countries.txt', 'r') as f:
        countries = f.read()
    response_json = json.loads(countries)
    names = []
    for r in response_json:
        if r["subregion"] not in ("Western Europe", "Central Europe", "Northern Europe"):
            continue
        if r["population"] < 100000:
            continue
        names.append(r["name"]["common"])
    return sorted(names)

if __name__ == '__main__':
    print(get_country_names())
