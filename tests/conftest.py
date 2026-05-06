import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base


@pytest.fixture(scope="module")
def test_client():
    DATABASE_URL = "sqlite:///:memory:"  # In-memory database for testing
    engine = create_engine(DATABASE_URL)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Create the database tables
    Base.metadata.create_all(bind=engine)
    app.dependency_overrides[get_db] = lambda: TestingSessionLocal()

    with TestClient(app) as client:
        yield client

    # Cleanup
    Base.metadata.drop_all(bind=engine)