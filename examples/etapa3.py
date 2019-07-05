from cirve import elementos as Element
from cirve.circuito import Circuit
from time import time

R1 = Element.Resistance(1e3)
R2 = Element.Resistance(13e3)
R3 = Element.Resistance(20e3)
R4 = Element.Resistance(2e3)
R5 = Element.Resistance(5e3)
R6 = Element.Resistance(63.2e3)
R7 = Element.Resistance(5e3)
R8 = Element.Resistance(11e3)
R9 = Element.Resistance(1e3)
RA = Element.Resistance(33e3)
RB = Element.Resistance(33e3)
RC = Element.Resistance(100)
RD = Element.Resistance(100)
RE = Element.Resistance(1e3)
c1 = Element.Capacitor(60e-7)
c2 = Element.Capacitor(60e-7)
c3 = Element.Capacitor(60e-7)
c4 = Element.Capacitor(60e-7)
Q1 = Element.Q2N3904(v=[0.745, -0.0026])
Q2 = Element.Q2N3904(v=[0.76, 0.75])
Q3 = Element.Q2N3904(v=[-23.68, -0.46])
Q4 = Element.Q2N3906(v=[-0.77, -0.79])
D1 = Element.D1N4002(2.68e-9, v=[0.32])
D2 = Element.D1N4002(2.68e-9, v=[-0.0026])
vs = Element.ACVoltageSource(2, 1e3)
vc1 = Element.VoltageSource(12)
vc2 = Element.VoltageSource(-12)

circuito = [[R1, [2,3]], [R2, [4,1]], [R3, [4,16]], [R4, [5,1]], [R5, [6,16]], 
            [R6, [7,1]], [R7, [7,16]], [R8, [8,1]], [R9, [9,16]], [RA, [11,1]], 
            [RB, [12,16]], [RC, [13,1]], [RD, [15,16]], [RE, [14,0]], [c1, [3,4]], 
            [c2, [6,7]], [c3, [9,16]], [c4, [8,10]], [D1, [11, 10]], 
            [D2, [10,12]], [Q1, [4, 5], [4,6]], [Q2, [7, 8], [7,9]], 
            [Q3, [11, 13], [11,14]], [Q4, [10, 15], [10,14]], [vs, [2, 0]],
            [vc1, [1, 0]], [vc2, [16, 0]]]

stime = time()
c = Circuit(circuito)
c.timeAnalysis([24, 13], [0, 0], ["voltage", "voltage"],
               0, 0.004, 40)
etime=time()-stime
print(etime)


