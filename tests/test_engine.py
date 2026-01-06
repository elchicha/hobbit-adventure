"""
Tests for game engine
"""
import pytest
import os
from game.engine import GameEngine
from dotenv import load_dotenv

load_dotenv()


class TestGameEngine:

    @pytest.fixture
    def engine(self):
        return GameEngine(
            api_token=os.getenv("NOTION_API_TOKEN"),
            locations_db=os.getenv("NOTION_LOCATIONS_DB")
        )

    def test_engine_initializes(self, engine):
        """Engine should initialize with Notion credentials"""
        assert engine is not None

    def test_get_location(self, engine):
        """Should retrieve a location from Notion"""
        if not os.getenv("NOTION_API_TOKEN"):
            pytest.skip("No API token")

        # This will fail - method doesn't exist yet
        location = engine.get_location("some_location_id")

        assert location is not None
        assert "name" in location
        assert "description" in location

        print(f"\n✅ Location loaded: {location['name']}")