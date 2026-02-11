from src.envelope import PhysicalQuantity, mu_Xe129, gamma_p
import numpy as np
solar_mass = PhysicalQuantity(1, 'solar_mass').convert_to('kg').value
parsec = PhysicalQuantity(1, 'parsec').convert_to('m').value  # 30856775814913673 m
# 30856775814913673
# 30856775814671916.000000
au = PhysicalQuantity(1, 'au').convert_to('m').value  # 149597870700
parsecFromAU = au * 648000. / (np.pi)
oneppm = PhysicalQuantity(1, 'ppm').convert_to('')
a = 1 + oneppm
# print(f'{parsec:22f}')
# print(f'{parsecFromAU:22f}')
print(f'{oneppm.value}')
cfreq = PhysicalQuantity(1.348570, "MHz")
print((cfreq / (gamma_p / (2 * np.pi))).convert_to("T"))
print(PhysicalQuantity(1.0, "ppb").convert_to(""))

# Dimensionless examples
x = PhysicalQuantity(1.0, "cm**3 m**(-3)")
print("np.exp(x)   =", np.exp(x))
print("np.tanh(x)  =", np.tanh(x))
print("np.sin(x)   =", np.sin(x))
print("np.cos(x)   =", np.cos(x))
print("np.sinh(x)  =", np.sinh(x))
print("np.cosh(x)  =", np.cosh(x))

# Arithmetic examples with units
a = PhysicalQuantity(3.0, "m")
b = PhysicalQuantity(2.0, "m")
c = PhysicalQuantity(5.0, "s")

print("\nnp.add(a, b)      =", np.add(a, b))  # m
print("np.subtract(a, b) =", np.subtract(a, b))  # m
print("np.multiply(a, b) =", np.multiply(a, b))  # m*m
print("np.divide(a, c)   =", np.divide(a, c))  # m/s

print(mu_Xe129.convert_to("J/T").unit)
induc = PhysicalQuantity(100, "henry")
print(induc.convert_to("nanohenry"))
print(induc.convert_to("nH"))

res = PhysicalQuantity(100, "ohm")
print(res.convert_to("kiloohm"))
# print(induc.convert_to("nH"))
