import json
import random
import faker

fake = faker.Faker()

def generate_isbn():
    prefix = '978'
    middle = ''.join([str(random.randint(0, 9)) for _ in range(9)])
    return f"{prefix}-{middle}"

books = []
for _ in range(30):
    book = {
        "title": fake.catch_phrase(),
        "author": fake.name(),
        "ISBN": generate_isbn(),
        "price": round(random.uniform(10, 150), 2),
        "quantity_in_stock": random.randint(0, 500)
    }
    books.append(book)

f = open("books.json", "w")
f.write(json.dumps({"books": books}, indent=4))
f.close()
