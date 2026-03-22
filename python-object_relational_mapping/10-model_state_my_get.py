#!/usr/bin/python3
"""prints the state object with the name passed as argument"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State

if __name__ == "__main__":
    # taking in args, assigning variables
    if len(sys.argv) != 5:
        print(
            f"Usage: {sys.argv[0]} "
            "<username> <password> <database> <state_name>"
            )
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)  # creates the class
    session = Session()  # creates the instance

    state = session.query(State).filter(
        State.name == state_name).first()

    if state:
        print(state.id)
    else:
        print("Not found")
    session.close()
