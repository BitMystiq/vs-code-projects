import requests
book, chapter, verse = input("Enter the book chapter and verse ").split()
reference = f"{book} {chapter}:{verse}"
r = requests.get(f"https://bible-api.com/{reference}")
data = r.json()
verse = data['text']
print()
print(reference,end="\n")
print(verse)
