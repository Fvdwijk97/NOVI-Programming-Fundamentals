# ==========================================
# Opdracht:
# Kies een PyPI library 'humanize' of 'prettytable' en zoek uit hoe je deze kunt gebruiken op PyPI.
# 1 - Welke (basis) functionaliteiten heeft de library?
# 2 - Maak een korte demo applicatie met deze library.
# ==========================================

# 1: De library converteert getallen, data, tijden, specifieke eenheden naar menselijke spreektaal of wetenschappelijke
# notaties. Bijvoorbeeld:
# 123455913 -> 123.5 million (adhv .intword)
# seconds = 1001 -> 16 minutes (adhv .naturaldelta & datetime.timedelta)
# 1_000_000 -> 1 MB (ahdv .naturalsize)
# 20_000 -> 2.00 x 10⁴ (ahdv .scientific)

# 2:
import humanize as hum
import datetime as dt

day = hum.naturalday(dt.datetime.now())
date = hum.naturaldate(dt.date(2025, 12, 14))
time_spend = hum.naturaldelta(dt.timedelta(seconds=2100))

delta = dt.timedelta(seconds=1530)
time_left = hum.precisedelta(delta)

memory_left = hum.naturalsize(20_000_000)
picture_count = hum.intword(60000)
should_be_home = hum.naturaltime(dt.timedelta(minutes=15))

print(f"{day}, {date}, I was already waiting {time_spend} for my train,\n"
      f"when they announced the train would be delayed even more, {time_left} to be exact.\n"
      f"While I was waiting I decided to download some music to listen to, to kill the time...\n"
      f"Unfortunately, I only had {memory_left} left, because of the {picture_count} pictures I had on my phone!\n"
      f"My husband was annoyed, because he prepared dinner and I should have been home {should_be_home}!")