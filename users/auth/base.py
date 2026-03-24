from abc import ABC, abstractmethod

from users.dto import AuthResponseDTO


class BaseAuth(ABC):
    """Abstract base class for authentication backends."""

    @abstractmethod
    def register(self, validated_data: dict) -> AuthResponseDTO:
        """Register a new user and return auth tokens."""
        pass

    @abstractmethod
    def login(self, email: str, password: str) -> AuthResponseDTO:
        """Authenticate user by email and password, return auth tokens."""
        pass

    @abstractmethod
    def logout(self, credential: str) -> None:
        """Invalidate the given refresh token."""
        pass
