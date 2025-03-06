from smartphone import Smartphone


catalog = [
    Smartphone("Samsung", "S25_Ultra", "+79938543765"),
    Smartphone("Samsung", "S24_FE", "+79938975345"),
    Smartphone("Nokia", "G22", "+79517865475"),
    Smartphone("Infinix", "Note12", "+79963457693"),
    Smartphone("Infinix", "Note30", "+79938846355"),
]

for smartphone in catalog:
    print(f"{smartphone.phone_brand} - {smartphone.phone_model}."
          f" {smartphone.phone_number}.")
