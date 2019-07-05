from cirve import elementos as Element
from cirve.circuito import Circuit
from time import time

Q1 = Element.Q2N3906(v=[-0.7, -0.7])
Q2 = Element.Q2N3906(v=[-0.7, -0.7])
Q8 = Element.Q2N3906(v=[-0.7, -0.7])

Q3 = Element.Q2N3904(v=[-0.7, -0.7])
Q4 = Element.Q2N3904(v=[-0.7, -0.7])
Q5 = Element.Q2N3904(v=[-0.7, -0.7])
Q6 = Element.Q2N3904(v=[-0.7, -0.7])
Q7 = Element.Q2N3904(v=[-0.7, -0.7])

D1 = Element.D1N4002(2.68e-9, v=[-0.01])
D2 = Element.D1N4002(2.68e-9, v=[-0.01])

C = Element.Capacitor(60e-12, -8)
R = Element.Resistance(50e3)

Ia = Element.CurrentSource(7.53e-14)
Ic = Element.CurrentSource(1.62e-15)

FT1 = Element.VoltageSource(0)
FT2 = Element.VoltageSource(-1)
FT3 = Element.VoltageSource(10)
FT4 = Element.VoltageSource(-10)
FT = Element.VoltageSource(0)
FT6 = Element.Resistance(1e6)

r1 = Element.Resistance(2e3)
rf = Element.Resistance(1e3)
ro = Element.Resistance(500)

Vs = Element.ACVoltageSource(1, 1e3)

circuito = [[Q1, [2, 8], [2, 7]], [Q2, [1, 6], [1, 7]], 
            [Q3, [13, 8], [13, 4]],[Q4, [13, 6], [13, 4]], 
            [Ia, [3, 7]], [C, [6, 10]], [Q5, [6, 3], [6, 9]],
            [R, [9, 4]], [Q6, [9, 10], [9, 4]], [D1, [11, 10]], 
            [D2, [12, 11]],[Ic, [3, 12]], [Q7, [12, 3], [12, 5]], 
            [Q8, [10, 4], [10, 5]],[FT1, [1, 0]], 
            [FT3, [3, 0]], [FT4, [4, 0]], [FT, [8, 13]], [r1, [14, 2]], 
            [Vs, [14, 0]], [rf, [2, 5]],
            [ro, [5, 0]]]

          
stime=time()
x=Circuit(circuito)
x.timeAnalysis([19, 21], [0, 0], ["voltage", "voltage"],
               0, 0.004, 60)

etime=time()-stime
print(etime)
c=Circuit(circuito)
print(c.solution())
