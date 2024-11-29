# lesson_3_task_3.py

from Address import Address
from Mailing import Mailing

# Создаем адреса
to_address = Address("630061", "Новосибирск", "Гребенщикова", "1", "101")
from_address = Address("666902", "Бодайбо", "Артема Сергеева", "5а", "2")

# Создаем почтовое отправление
mailing = Mailing(to_address, from_address, 850, "TRK123456")

# Печатаем информацию об отправлении
print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
      f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, "
      f"{mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. "
      f"Стоимость {mailing.cost} рублей.")
