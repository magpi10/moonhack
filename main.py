#!/bin/python3
from classes import *

targetPlanet = input('"Type the name of a planet:')
capitalPlanet = str.capitalize(targetPlanet)

#print(targetPlanet)

myPlanet = ourSolarSystem.getPlanet(capitalPlanet)

if myPlanet is not None:
  moons = myPlanet.get_moons()
  if len(moons) > 0:
    print(moons)
  else:
    print(capitalPlanet + " has no moons!")
else:
  print(capitalPlanett + " is not a planet!")