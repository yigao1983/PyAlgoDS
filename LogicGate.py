class LogicGate(object):

    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA is None:
            return int(input("Enter Pin A input for gate " +
                             self.getLabel() + "-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB is None:
            return int(input("Enter Pin B input for gate " +
                             self.getLabel() + "-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA is None:
            self.pinA = source
        else:
            if self.pinB is None:
                self.pinB = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")


class UnaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pin = None

    def getPin(self):
        if self.pin is None:
            return int(input("Enter Pin input for gate " +
                             self.getLabel() + "-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin is None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a == 1 or b == 1:
            return 1
        else:
            return 0


class NotGate(UnaryGate):

    def __init__(self, n):
        UnaryGate.__init__(self, n)

    def performGateLogic(self):

        a = self.getPin()
        if a == 1:
            return 0
        else:
            return 1


class Connector(object):

    def __init__(self, fgate, tgate):

        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate


def main():

    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    print(g4.getOutput())


if __name__ == "__main__":

    main()
