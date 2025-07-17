# 3-5. Countries data analysis
print("\n3-5. Countries data analysis (commented - needs countries_data.py):")
"""
from data.countries_data import countries_data
from collections import defaultdict

# 3. Total languages
languages = set()
for country in countries_data:
    for lang in country['languages']:
        languages.add(lang)
print(f"\n3. Total number of languages: {len(languages)}")

# 4. Top 10 languages
lang_count = defaultdict(int)
for country in countries_data:
    for lang in country['languages']:
        lang_count[lang] += 1

sorted_langs = sorted(lang_count.items(), key=lambda x: x[1], reverse=True)
print("\n4. Top 10 most spoken languages:")
for lang, count in sorted_langs[:10]:
    print(f"{lang}: {count}")

# 5. Top 10 populated countries
sorted_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)
print("\n5. Top 10 most populated countries:")
for country in sorted_countries[:10]:
    print(f"{country['name']}: {country['population']}")
"""