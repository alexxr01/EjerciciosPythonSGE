#!/usr/bin/env python3
renta = float(input("Introduce tu renta anual en euros: "))

if renta <= 12450:
    impuesto = renta * 0.19
elif renta <= 20200:
    impuesto = 2365.5 + (renta - 12450) * 0.24
elif renta <= 35200:
    impuesto = 4195.5 + (renta - 20200) * 0.3
elif renta <= 60000:
    impuesto = 8675.5 + (renta - 35200) * 0.37
else:
    impuesto = 19822.5 + (renta - 60000) * 0.45

print("El IRPF a pagar es de", round(impuesto, 2), "euros.")
