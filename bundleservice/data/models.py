"""
ORM Model definitions
"""
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Bundle(Base):
    """
    SQLAlchemy model for a Bundle
    """
    __tablename__ = 'bundle'

    id = sa.Column(sa.Integer, primary_key=True)
    device_uuid = sa.Column(sa.String)
    sensor_type = sa.Column(sa.String)
    sensor_value = sa.Column(sa.Float)
    sensor_reading_time = sa.Column(sa.Integer)

def init_db():
    """
    Initialize the sqlite db for demo purposes
    """
    engine = sa.create_engine('sqlite:///tmp.db')
    Base.metadata.create_all(engine)
    db_session = sessionmaker(bind=engine)()
    # Seed the DB with some records
    bundles = [
        Bundle(
            device_uuid='b21ad0676f26439482cc9b1c7e827de4',
            sensor_type='temperature',
            sensor_value=50.0,
            sensor_reading_time=1510093202,
        ),
        Bundle(
            device_uuid='b21ad0676f26439482cc9b1c7e827de4',
            sensor_type='temperature',
            sensor_value=65.4,
            sensor_reading_time=1510993202,
        ),
        Bundle(
            device_uuid='8389dc5da8174a8e9efc99be5104fdc1',
            sensor_type='temperature',
            sensor_value=49.9,
            sensor_reading_time=1510093202,
        ),
        ]
    db_session.add_all(bundles)
    return db_session

db_session = init_db()
