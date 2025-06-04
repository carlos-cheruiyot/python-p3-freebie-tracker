#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

print("Testing data...")

dev = session.query(Dev).filter_by(name="Alice").first()
print(f"Dev: {dev}")
print(f"Freebies collected: {[f.item_name for f in dev.freebies]}")
print(f"Companies for dev: {[c.name for c in dev.companies]}")
print(f"Received 'Sticker'? {dev.received_one('Sticker')}")

company = session.query(Company).filter_by(name="Google").first()
print(f"Company: {company}")
print(f"Freebies given: {[f.item_name for f in company.freebies]}")
print(f"Devs who collected freebies: {[d.name for d in company.devs]}")

freebie = dev.freebies[0]
print(freebie.print_details())

oldest = Company.oldest_company(session)
print(f"Oldest company: {oldest.name}")

# Testing give_away method
bob = session.query(Dev).filter_by(name="Bob").first()
print(f"Bob's freebies before give_away: {[f.item_name for f in bob.freebies]}")

alice.give_away(bob, dev.freebies[0])
session.commit()

print(f"Bob's freebies after give_away: {[f.item_name for f in bob.freebies]}")

session.close()
