import elementos as Element
from circuito import Circuit
from time import time

AV = Element.ACVoltageSource(1, 1e3)
Vcc = Element.VoltageSource(12)
Rs = Element.Resistance(560)
R1 = Element.Resistance(33e3)
R2 = Element.Resistance(100)
Rl = Element.Resistance(1e3)
TR1 = Element.Q2N3904()
TR2 = Element.Q2N3906()

circuito = [[AV,[1, 0]],
            [Rs, [1, 2]],
            [R1, [2, 3]],
            [R1, [2, 4]],
            [Vcc, [3, 0]],
            [Vcc, [0, 4]],
            [TR1, [2, 6],[2, 5]],
            [TR2, [2, 7],[2, 5]],
            [R2, [6, 3]],
            [R2, [7, 4]],
            [Rl, [5, 0]]]

t1=time()
x=Circuit(circuito)
x.timeAnalysis([10, 0, 6], [0, 0, 0], ["voltage", "voltage", "voltage"], 
               0, 0.001, 30)
print(time()-t1)


