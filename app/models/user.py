import re

from app.models.base_model import BaseModel


EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.places = []
        self.reviews = []

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("first_name is required")
        if len(value) > 50:
            raise ValueError("first_name must be at most 50 characters")
        self._first_name = value.strip()

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("last_name is required")
        if len(value) > 50:
            raise ValueError("last_name must be at most 50 characters")
        self._last_name = value.strip()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not isinstance(value, str) or not EMAIL_RE.match(value):
            raise ValueError("email must be valid")
        self._email = value.strip().lower()

    @property
    def is_admin(self):
        return self._is_admin

    @is_admin.setter
    def is_admin(self, value):
        self._is_admin = bool(value)

    def add_place(self, place):
        if place not in self.places:
            self.places.append(place)
            self.save()

    def add_review(self, review):
        if review not in self.reviews:
            self.reviews.append(review)
            self.save()

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
        }
