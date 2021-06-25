from FishScraper import FishScraper


params = {
    "hemisphere":"north",
    "Location":"Pond"
}
fish = FishScraper(params)
df = fish.generate()
