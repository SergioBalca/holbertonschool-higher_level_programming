#!/usr/bin/python3

""" Adds the State object 'Louisiana' to the database hbtn_0e_6_usa """

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    old_state = session.query(State).filter(State.id == 2)
    old_state.update({State.name: 'New Mexico'}, synchronize_session=False)
    session.commit()
    session.close()
