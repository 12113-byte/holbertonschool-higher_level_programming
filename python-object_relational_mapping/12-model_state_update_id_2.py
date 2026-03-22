#!/usr/bin/python3
"""changes the name of a state object from database hbtn_0e_6_usa"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State

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

    state = session.query(State).filter(State.id == 2).first()
    state.name = 'New Mexico'
    session.commit()

    session.close()
