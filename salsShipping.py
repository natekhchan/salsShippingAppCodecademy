#Sal's Shipping Project
# Codecademy Project by Nathan Chan 
# Date Submitted:  December 8, 2022

from decimal import Decimal

weight = 41.5
costOfPremiumGround = 125.00

# Ground Shipping

if weight <= 2:
  groundPricePerPound = 1.50
  groundFlatCharge = 20.00
elif weight > 2 and weight <= 6:
  groundPricePerPound = 3.00
  groundFlatCharge = 20.00
elif weight > 6 and weight <= 10:
  groundPricePerPound = 4.00
  groundFlatCharge = 20.00
else:
  groundPricePerPound = 4.75
  groundFlatCharge = 20.00

# Drone Shipping

if weight <= 2:
  dronePricePerPound = 4.50
  droneFlatCharge = 0  
elif weight > 2 and weight <= 6:
  dronePricePerPound = 9
  droneFlatCharge = 0  
elif weight > 6 and weight <= 10:
  dronePricePerPound = 12
  droneFlatCharge = 0
else:
  dronePricePerPound = 14.25
  droneFlatCharge = 0

groundCost = (weight * groundPricePerPound) + groundFlatCharge
droneCost = (weight * dronePricePerPound) + droneFlatCharge

print("Ground Shipping: $ ", Decimal(groundCost).quantize(Decimal('1.00')))
print("Ground Shipping Premium $ ", Decimal(costOfPremiumGround).quantize(Decimal('1.00')))
print("Drone Shipping: $ ", Decimal(droneCost).quantize(Decimal('1.00')))
