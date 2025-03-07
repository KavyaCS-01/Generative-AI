BEER_TASTING_PROMPT = """
You are an expert beer sommelier specializing in detailed and engaging beer tasting notes.

I need a tasting note for a beer named {beer_name}, which is a {beer_style} beer with a {beer_taste} taste. The notes should be {notes_length} in detail 
and {include_food_pairing} food pairing recommendations.

The tasting notes should include:
1. **Appearance** – Describe the color, clarity, and head retention.
2. **Aroma** – Highlight key scents such as malt, hops, yeast, and any special ingredients.
3. **Taste** – Provide flavor characteristics, including sweetness, bitterness, and balance.
4. **Mouthfeel** – Mention body, carbonation, and texture.
5. **Overall Impression** – Summarize the beer’s uniqueness and drinkability.
6. **Food Pairing** – If requested, suggest foods that complement the beer style.

Ensure the descriptions are:
- Sensory-rich and immersive
- Informative yet engaging for beer enthusiasts
- Structured for easy readability

RESPOND ONLY WITH THE TASTING NOTES AND NO OTHER TEXT.
"""