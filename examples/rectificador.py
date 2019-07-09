import elementos as Element
from circuito import Circuit
from time import time

AV = Element.ACVoltageSource(50, 60)
R = Element.Resistance(1e3)
C = Element.Capacitor(60e-7)
D = Element.D1N4002()

circuito = [[AV,[1, 0]], 
            [D, [1, 2]],
            [C, [2, 0]],
            [R, [2, 0]]]

t1 = time()
x = Circuit(circuito)
x.timeAnalysis([0, 3], [0, 0], ["voltage", "voltage"], 0, 0.025, 1200)
print(time()-t1)
