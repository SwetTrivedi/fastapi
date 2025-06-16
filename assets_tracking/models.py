# database.py
from typing import Dict, Any, List

# --- Mock Database (In-Memory) ---
# This dictionary will hold all our application data while the server is running.
# IMPORTANT: Data stored here is LOST when the server restarts.
mock_db: Dict[str, List[Dict[str, Any]]] = {
    "users": [],         # Stores user dictionaries for asset users
    "admin_users": [],   # Stores user dictionaries for admin users
    "assets": [],        # Stores asset dictionaries
    "location_updates": [] # Stores location update dictionaries
}

# You can add helper functions here if needed,
# e.g., to find a user, find an asset, etc.
# For now, we'll just expose mock_db directly.
class UserInDB:
    """Represents a user stored in our mock database."""
    def __init__(self, username: str, hashed_password: str, role: str):
        self.username = username
        self.hashed_password = hashed_password
        self.role = role # "asset_user" or "admin"

    def to_dict(self):
        """Converts the user object to a dictionary for storage in mock_db."""
        return {"username": self.username, "hashed_password": self.hashed_password, "role": self.role}