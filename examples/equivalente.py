from cirve import elementos as Element
from cirve.circuito import Circuit

V = Element.VoltageSource(5)
R = Element.Resistance(20)
I1 = Element.CurrentSource(1)
I2 = Element.CCCS(5)
I3 = Element.CurrentSource(0)

circuito = [[V, [1, 0]],
            [R, [2, 1]],
            [I1, [3, 0]],
            [I2, [0, 3], [3, 2]]]

x = Circuit(circuito)
print(x.solution())
print(x.theveninEquivalent(0, 3))
print(x.nortonEquivalent(0, 3))