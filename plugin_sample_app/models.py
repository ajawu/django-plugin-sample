import json
import random
from django.db import models
from django.utils import timezone


class Task:
    def __init__(
        self, id=None, title="", description="", is_completed=False, creation_date=None
    ):
        self.id = id or random.randint(1, 1000)
        self.title = title
        self.description = description
        self.is_completed = is_completed
        self.creation_date = creation_date or timezone.now()

    def serialize(self) -> dict:
        data = {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "is_completed": self.is_completed,
            "creation_date": self.creation_date,
        }
        return data

    def update(self, data: dict):
        self.id = data.get("id") or self.id
        self.title = data.get("title") or self.title
        self.description = data.get("description") or self.description
        self.is_completed = data.get("is_completed") or self.is_completed
        self.creation_date = data.get("creation_date") or self.creation_date
