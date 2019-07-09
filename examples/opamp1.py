import elementos as Element
from circuito import Circuit
from time import time

# la clase Circuit es capaz de encontrar una solución al circuito que se 
# presenta en este circuito, sin embargo los tiempos de ejecución son muy
# elevados. No se recomienda su ejecución.

Q1 = Element.Q2N3904()
Q2 = Element.Q2N3904()
Q3 = Element.Q2N3904()
Q7 = Element.Q2N3904()
Q8 = Element.Q2N3904()
Q13 = Element.Q2N3904()
Q12 = Element.Q2N3904()
Q14 = Element.Q2N3904()
Q17 = Element.Q2N3904()
Q15 = Element.Q2N3904()
Q16 = Element.Q2N3904()
Q18 = Element.Q2N3904()
Q20 = Element.Q2N3904()

Q6 = Element.Q2N3906()
Q5 = Element.Q2N3906()
Q4 = Element.Q2N3906()
Q9 = Element.Q2N3906()
Q10 = Element.Q2N3906()
Q11 = Element.Q2N3906()
Q19 = Element.Q2N3906()

R1 = Element.Resistance(1e3)
R2 = Element.Resistance(50e3)
R3 = R1
R4 = Element.Resistance(5e3)
R5 = R2
R6 = Element.Resistance(50)
R7 = Element.Resistance(7.5e3)
R8 = Element.Resistance(4.5e3)
R9 = Element.Resistance(25)
R10 = R6

c = Element.Capacitor(60e-12)

r1 = Element.Resistance(2e3)
rf = Element.Resistance(1e3)
ro = Element.Resistance(500)

Vs = Element.ACVoltageSource(1, 1e3)

FT1 = Element.VoltageSource(10)#Vcc+
FT2 = Element.VoltageSource(-10)#Vcc-
FT3 = Element.VoltageSource(0)#Vin+
FT4 = Element.VoltageSource(-1)#Vin-
FT5 = Element.VoltageSource(5)#Vout

FT6 = Element.VoltageSource(0)
FT7 = Element.VoltageSource(0)
FT8 = Element.VoltageSource(0)


circuito = [[FT1, [1, 0]], [FT2, [26, 0]], [r1, [3, 27]],
            [Q1, [2, 5], [2, 6]], [Q2, [3, 5], [3, 7]], 
            [Q3, [9, 1], [9, 11]], [Q4, [28, 5], [28, 1]], 
            [Q5, [8, 10], [8, 7]],
            [Q6, [8, 9], [8, 6]], [Q7, [11, 9], [11, 12]], 
            [Q8, [11, 10], [11, 14]], [Q9, [28, 15], [28, 1]], 
            [Q10, [30, 18], [30, 1]],
            [Q11, [30, 19], [30, 1]], [Q12, [29, 17], [29, 26]], 
            [Q13, [29, 15], [29, 16]], [Q14, [20, 19], [20, 21]],
            [Q15, [22, 21], [22, 23]], 
            [Q16, [10, 21], [10, 22]], [Q17, [23, 10], [23, 26]], 
            [Q18, [19, 1], [19, 24]], [Q19, [21, 26], [21, 25]], 
            [Q20, [24, 19], [24, 4]],
            [R1, [12, 26]], [R2, [13, 26]], [R3, [14, 26]], 
            [R4, [16, 26]], [R5, [22, 26]], [R6, [23, 26]], 
            [R7, [20, 21]],
            [R8, [20, 19]], [R9, [24, 4]], [R10, [4, 25]], 
            [c, [19, 10]], [ro, [4, 0]], [rf, [3, 4]], [vs, [27, 0]],
            [FT3, [2, 0]], [FT6, [5, 28]], [FT7, [17, 29]], [FT8, [18, 30]]]

stime = time()
c = Circuit(circuito)
c.timeAnalysis([34, 36], [0, 0], ["voltage", "voltage"],
               0, 0.001, 100)
etime=time()-stime
print(etime)
