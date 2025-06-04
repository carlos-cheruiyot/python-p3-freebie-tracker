
#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create tables (if not already created)
Base.metadata.create_all(engine)

# Clear existing data
session.query(Freebie).delete()
session.query(Dev).delete()
session.query(Company).delete()
session.commit()

# Create some companies
google = Company(name="Google", founding_year=1998)
apple = Company(name="Apple", founding_year=1976)

# Create some devs
alice = Dev(name="Alice")
bob = Dev(name="Bob")

session.add_all([google, apple, alice, bob])
session.commit()

# Give freebies
freebie1 = google.give_freebie(alice, "Sticker", 1)
freebie2 = apple.give_freebie(bob, "T-Shirt", 20)
freebie3 = google.give_freebie(bob, "Mug", 10)

session.add_all([freebie1, freebie2, freebie3])
session.commit()

print("Seed data inserted!")

session.close()
