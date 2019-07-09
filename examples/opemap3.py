import elementos as Element
from circuito import Circuit
import subcircuit as SCir
from time import time

# En este caso Circuit es capaz de dar soluciones, sin embargo su solución 
# termina por diverger.

Vs = Element.ACVoltageSource(1, 10e3)
Vc1 = Element.VoltageSource(10)
Vc2 = Element.VoltageSource(-10)
r1 = Element.Resistance(2e3)
rf = Element.Resistance(1e3)
ro = Element.Resistance(500)
vc = Element.VoltageSource(0)
OPAMP = SCir.Opamp5()
FT = Element.VoltageSource(0)


circuito = [[Vs, [1, 0]],
            [ro, [3, 0]],
            [r1, [1, 2]],
            [rf, [2, 3]],
            [FT, [4, 0]],
            [OPAMP, [4, 0], [2, 0], [3, 0]]]

stime = time()
x = Circuit(circuito)
x.timeAnalysis([0, 5], [0, 2], ["voltage", "voltage"],
               0, 0.0005, 200)

etime = time()-stime
print(etime)
