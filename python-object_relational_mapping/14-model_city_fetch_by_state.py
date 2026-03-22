#!/usr/bin/python3
"""deletes all State objects with name containing letter 'a' from db"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # taking in args, assigning variables
    if len(sys.argv) != 4:
        print(
            f"Usage: {sys.argv[0]} <username> <password> <database>"
            )
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)  # creates the class
    session = Session()  # creates the instance

    results = session.query(State, City).join(
        City, State.id == City.state_id
        ).order_by(City.id).all()

    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
