import csv
from django.core.management.base import BaseCommand
from api.models import Crop, Season

# Handles migrations/data loading for crop and season models
class Command(BaseCommand):
    def handle(self, *args, **options):
        with open("api/data/crops.csv") as file:
            crop_reader = csv.DictReader(file)

            for row in crop_reader:
                season_names = row["season"].split("|")
                seasons = []

                for name in season_names:
                    season, _ = Season.objects.get_or_create(name=name.strip())
                    seasons.append(season)

                days_to_regrow = 0
                if row["days_to_regrow"]:
                    days_to_regrow = int(row["days_to_regrow"].strip())

                special_location = "None"
                if row["special_location"]:
                    special_location = row["special_location"].strip()

                crop, _ = Crop.objects.update_or_create(
                    name = row["name"].strip(),
                    defaults = {
                        "special_location": special_location,
                        "growth_time": int(row["growth_time"].strip()),
                        "sell_price": int(row["sell_price"].strip()),
                        "seed_price": int(row["seed_price"].strip()),
                        "multiharvest": bool(row["multiharvest"]),
                        "days_to_regrow": days_to_regrow,
                        "max_harvest": 1
                    }       
                )
                crop.season.set(seasons)

                