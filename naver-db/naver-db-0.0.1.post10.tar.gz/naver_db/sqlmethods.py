from sqlalchemy import create_engine
from sqlalchemy.orm import Session

uri = ""
engine = create_engine(uri)
stm = "SELECT 1"
#BY COM

def basicexecute():
    with engine.connect() as conn:        
        res = conn.execute(stm).all()
        return res

def directexecute():
    db = create_engine(uri)
    db.execute(stm)

def sessionexecute():
    engine = create_engine(uri)
    session = Session(engine)
    res= session.execute(stm)
    session.commit()
    res.fetchall()

def sessiontransac():
    engine = create_engine(uri)
    session = Session(engine)
    res= session.execute(stm)
    return {res,session}

