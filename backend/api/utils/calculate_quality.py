from ..models import FertilizerQualityChance

def calculate_quality(fertilizer, farming_level):
    regular_chance = silver_chance = gold_chance = iridium_chance = 0

    if fertilizer:
        fertilizer = None if fertilizer == "0" else int(fertilizer)

    farming_level = 0 if not farming_level else int(farming_level)

    qualities = FertilizerQualityChance.objects.filter(fertilizer__id=fertilizer).filter(farming_level=farming_level).values_list('regular_chance', 'silver_chance', 'gold_chance', 'iridium_chance', named=True)

    for row in qualities:
        regular_chance = row.regular_chance
        silver_chance = row.silver_chance
        gold_chance = row.gold_chance
        iridium_chance = row.iridium_chance
   
    return { "Regular": regular_chance, "Silver": silver_chance, "Gold": gold_chance, "Iridium": iridium_chance }