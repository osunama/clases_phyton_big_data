from decimal import Decimal
valor = Decimal('4.9999999999999').quantize(Decimal('1.0000000000000'))
print(valor)  