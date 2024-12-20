from fuzzywuzzy import fuzz
from fuzzywuzzy import process

s1="eatting"
s2="setting"
print(fuzz.ratio(s1,s2))


ss1="cat is sitting, on the table"
ss1="cat is sitting"
print(fuzz.partial_ratio(s1,s2))


print(fuzz.token_sort_ratio("fuzzy was a bear", "fuzzy fuzzy was a bear"))
print(fuzz.token_set_ratio("fuzzy was a bear", "fuzzy fuzzy was a bear"))


print(fuzz.WRatio("Happly Birthday, John", "John, Happy Birthday"))
print(fuzz.WRatio("Happly Birthday, John!!!!!", "Happly Birthday, John"))


query="It's Query for Testing"
choices = ["It's Testing for Query", "It's Query for Testing", "Query for Testing for fuzzy sets."]
print(process.extract(query,choices))
print(process.extractOne(query,choices))