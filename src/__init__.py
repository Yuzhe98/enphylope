"""
enphylope
------------
A Python package for calculations with physical quantities.

Features:
- Quantity creation with units
- Unit conversion
- Basic arithmetic with physical quantities
- Common physical constants
"""

# Import main classes/functions
from .core import PhysicalQuantity
from .constants import (
    e,
    c,
    mol_to_num,
    c,
    u,
    kB,
    h_Planck,
    hbar,
    m_e,
    m_p,
    m_n,
    mu_B,
    mu_0,
    mu_N,
    g_p,
    I_p,
    mu_p,
    gamma_p,
    mu_Xe129,
    gamma_Xe129,
)

# Optional: define __all__ to control what is exposed
__all__ = [
    "PhysicalQuantity",
    "e",
    "c",
    "mol_to_num",
    "u",
    "kB",
    "h_Planck",
    "hbar",
    "m_e",
    "m_p",
    "m_n",
    "mu_B",
    "mu_0",
    "mu_N",
    "g_p",
    "I_p",
    "mu_p",
    "gamma_p",
    "mu_Xe129",
    "gamma_Xe129",
]

# Package version
__version__ = "0.1.0"
