def fuerza (G,m1,m2,d):
		F=(G*(m1*m2))/d**2
		return (F)

#wrapper
def luna(m1,m2,d):
	return fuerza(1.62,m1,m2,d)
def marte(m1,m2,d):
	return fuerza(3.711,m1,m2,d)
def jupiter(m1,m2,d):
	return fuerza(1.315,m1,m2,d)
def encelado(m1,m2,d):
	return fuerza(0.113,m1,m2,d)
def titan(m1,m2,d):
	return fuerza(1.352,m1,m2,d)
def venus(m1,m2,d):
	return fuerza(8.87,m1,m2,d)

F=luna(1,2,3)
print("luna",F,"newtons")
F=marte(1,2,3)
print("marte",F,"newtons")
F=jupiter(1,2,3)
print("jupiter",F,"newtons")
F=encelado(1,2,3)
print("encelado",F,"newtons")
F=titan(1,2,3)
print("titan",F,"newtons")
F=venus(1,2,3)
print("venus",F,"newtons")
