from Address import Address
from Mailing import Mailing

from_address = Address('214525', 'Смоленск', 'Новые Батеки', '4', '11')
to_address = Address('432054', 'Ульяновск', 'Камышинская', '6', '56')
mail = Mailing(to_address, from_address, 459, 'TRACK43')
print(mail)
