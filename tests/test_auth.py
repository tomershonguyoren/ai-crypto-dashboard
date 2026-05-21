def test_signup(client):
    response = client.post("/signup", json={
        "email": "newuser@example.com",
        "name": "New User",
        "password": "newpassword123"
    })
    
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "newuser@example.com"
    assert data["name"] == "New User"
    assert "id" in data

def test_signup_duplicate_email(client, db_session):
    from app.models.user import User
    from app.core.security import get_password_hash
    
    # Pre-populate dummy duplicate element
    user = User(email="duplicate@example.com", name="Duplicate User", hashed_password=get_password_hash("pass"))
    db_session.add(user)
    db_session.commit()
    
    # Attempting to sign up same element
    response = client.post("/signup", json={
        "email": "duplicate@example.com",
        "name": "Another User Trying Same Mail",
        "password": "password123"
    })
    
    assert response.status_code == 400
    assert response.json()["detail"] == "Email already registered"

def test_login(client, db_session):
    from app.models.user import User
    from app.core.security import get_password_hash
    
    # Pre-populate exact payload needed
    user = User(email="login@example.com", name="Login", hashed_password=get_password_hash("password123"))
    db_session.add(user)
    db_session.commit()
    
    response = client.post("/login", json={
        "email": "login@example.com",
        "password": "password123"
    })
    
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
