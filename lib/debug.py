#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

engine = create_engine('sqlite:///freebies.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Add sample data if none exists
if not session.query(Company).first():
    c = Company(name="Google", founding_year=1998)
    d = Dev(name="Alice")
    session.add_all([c, d])
    session.commit()

    f = c.give_freebie(d, "Sticker", 1)
    session.add(f)
    session.commit()

# Test queries
dev = session.query(Dev).first()
print("Companies for dev:", dev.companies)
print("Received 'Sticker'?", dev.received_one("Sticker"))
print("Freebie details:", dev.freebies[0].print_details())

oldest = Company.oldest_company(session)
print(f"Oldest company: {oldest.name}")

session.close()
