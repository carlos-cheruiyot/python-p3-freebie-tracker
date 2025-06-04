
#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

engine = create_engine('sqlite:///freebies.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Create company and devs if none exist
if not session.query(Company).first():
    c = Company(name="Google", founding_year=1998)
    d = Dev(name="Alice")
    session.add_all([c, d])
    session.commit()

    f = c.give_freebie(d, "Sticker", 1)
    session.add(f)
    session.commit()

# Testing
dev = session.query(Dev).first()
print(dev.companies)                 # list of companies
print(dev.received_one("Sticker"))  # True
print(dev.freebies[0].print_details())

oldest = Company.oldest_company(session)
print(f"Oldest company: {oldest.name}")

session.close()
