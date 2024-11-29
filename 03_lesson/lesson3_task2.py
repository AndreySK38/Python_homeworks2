from smartphone import Smartphone


catalog = [
    Smartphone("Apple", "iPhone 13", "+79001234567"),
    Smartphone("Samsung", "Galaxy S21", "+79007654321"),
    Smartphone("Xiaomi", "Mi 11", "+79138942022"),
    Smartphone("Google", "Pixel 6", "+79835432123"),
    Smartphone("OnePlus", "9 Pro", "+79006789012")
]


for smartphone in catalog:
    print(smartphone)