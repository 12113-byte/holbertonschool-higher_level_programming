import sys
from sqlalchemy as db

db_user = sys.argv[1]
db_password = sys.argv[2]
db_table = sys.argv[3]

# simple database connection script
engine = db.create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(db_user, db_password, db_table), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
