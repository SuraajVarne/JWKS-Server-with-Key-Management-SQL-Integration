# key_management.py
import logging
from sqlalchemy import create_engine, Column, String, Integer, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from config import DATABASE_URI

# Set up logging for key management operations
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

Base = declarative_base()

class RSAKey(Base):
    __tablename__ = 'rsa_keys'
    id = Column(Integer, primary_key=True, autoincrement=True)
    key_id = Column(String(64), unique=True, nullable=False, index=True)
    public_key = Column(String, nullable=False)

# Create a database engine with connection pooling for performance
engine = create_engine(DATABASE_URI, echo=False, pool_size=10, max_overflow=20)
SessionFactory = sessionmaker(bind=engine)
Session = scoped_session(SessionFactory)

# Ensure an index exists for fast lookups on key_id
Index('ix_rsa_keys_key_id', RSAKey.key_id)

# Create the table(s) if they do not exist
Base.metadata.create_all(engine)

def get_all_keys():
    """
    Retrieve all RSA keys from the database and format them for the JWKS response.
    """
    session = Session()
    try:
        keys = session.query(RSAKey).all()
        key_list = []
        for key in keys:
            key_list.append({
                "kid": key.key_id,
                "kty": "RSA",
                "use": "sig",
                "n": key.public_key,  # Assumes key stored as Base64 encoded modulus
                "alg": "RS256"
            })
        return key_list
    finally:
        session.close()

def add_key(key_id, public_key):
    """
    Add a new RSA key to the database.
    """
    session = Session()
    try:
        new_key = RSAKey(key_id=key_id, public_key=public_key)
        session.add(new_key)
        session.commit()
        logger.info("Key %s added successfully.", key_id)
    except Exception as e:
        session.rollback()
        logger.error("Error adding key %s: %s", key_id, e)
    finally:
        session.close()
