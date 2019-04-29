import random
from lymphocyte import Lymphocyte

class Lymphocyte(object):

    def __init__(self, antibody):
        self.antibody = antibody[:]
        self.age = 0
        self.stimulation = 0
        self.searchTable = self._buildTable()

    def _buildTable(self):
        result = [False] * len(self.antibody)
        pos = 2
        cnd = 0
        result[0] = -1
        result[1] = 0
        while (pos < len(self.antibody)):
            if self.antibody[pos - 1] == self.antibody[cnd]:
                cnd += 1
                result[pos] = cnd
                pos += 1
            elif cnd > 0:
                cnd = result[cnd]
            else:
                result[pos] = 0
                pos += 1
        return result

    def detects(self, pattern):
        m = 0
        i = 0
        while (m + i < len(pattern)):
            if (self.antibody[i] == pattern[m + i]):
                if (i == len(self.antibody) - 1):
                    return True
                i += 1
            else:
                m = m + i - self.searchTable[i]
                if (self.searchTable[i] > -1):
                    i = self.searchTable[i]
                else:
                    i = 0
        return False

    def getHashCode(self):
        return ''.join(['1' if i else '0' for i in self.antibody])

    def toString(self):
        s = 'antibody = '
        for i, a in enumerate(self.antibody):
            s += '1 ' if (self.antibody[i]) else '0 '
        s += ' age = {0}'.format(self.age)
        s += ' stimulation = {0}'.format(self.stimulation)
        return s


class ArtificialImmuneSystemProgram(object):

    def __init__(self):
        print('\nBegin Artificial Immune System for Intrusion Detection demo\n')

        self.numPatternBits = 12
        self.numAntibodyBits = 4
        self.numLymphocytes = 3
        self.stimulationThreshold = 3

        print('Loading self-antigen set (\'normal\' historical patterns)')
        self.selfSet = self.loadSelfSet()
        self.showSelfSet(self.selfSet)

        print('\nCreating lymphocyte set using negative selection  and r-chunks detection')

        lymphocyteSet = self.createLymphocyteSet(self.selfSet,
                                                 self.numAntibodyBits,
                                                 self.numLymphocytes)
        self.showLymphocyteSet(lymphocyteSet)

        print('\nBegin AIS intrusion detection simulation\n')

        time = 0
        maxTime = 6

        while (time < maxTime):
            print('===============================================')

            incoming = self.randomBitArray(self.numPatternBits)
            print('Incoming pattern = {0}\n'.format(self.bitArrayAsString(incoming)))

            for i, ls in enumerate(lymphocyteSet):
                if ls.detects(incoming):
                    print('Incoming pattern detected by lymphocyte {0}'.format(i))
                    ls.stimulation += 1
                    if (ls.stimulation >= self.stimulationThreshold):
                        print('Lymphocyte {0} stimulated! Check incoming as possible intrusion!'.format(i))
                    else:
                        print('Lymphocyte {0} not over stimulation threshold'.format(i))

                else:
                    print('Incoming pattern not detected by lymphocyte {0}'.format(i))

            time += 1
            print('===============================================')

        print('\nEnd AIS IDS demo\n')


    @staticmethod
    def loadSelfSet():
        result = []
        result.append([True, False, False, True, False, True, True, False, True, False, False, True])
        result.append([True, True, False, False, True, False, True, False, True, True, False, False])
        result.append([True, False, True, True, False, False, True, True, False, True, False, True])
        result.append([False, False, True, True, False, True, False, True, True, False, True, True])
        result.append([False, True, False, True, False, True, False, False, True, True, False, True])
        result.append([False, False, True, False, True, False, True, False, False, True, False, False])
        return result

    @staticmethod
    def showSelfSet(selfSet):
        for idx, s in enumerate(selfSet):
            print(str(idx) + ': ' + ArtificialImmuneSystemProgram.bitArrayAsString(s))

    @staticmethod
    def bitArrayAsString(ba):
        s = ''
        for i in ba:
            s += '1 ' if i else  '0 '
        return s

    @staticmethod
    def createLymphocyteSet(selfSet, numAntibodyBits, numLymphocytes):
        result = []
        contents = {}

        while (len(result) < numLymphocytes):
            antibody = ArtificialImmuneSystemProgram.randomBitArray(numAntibodyBits)  # random antibody
            lymphocyte = Lymphocyte(antibody) # random lymphocte
            hash = lymphocyte.getHashCode() # assumes antibody length <= 32 bits
            if (not ArtificialImmuneSystemProgram.detectsAny(selfSet, lymphocyte) and hash not in contents):
                result.append(lymphocyte)
                contents[hash] = True
        return result

    @staticmethod
    def randomBitArray(numBits):
        bitArray = []
        for i in range(numBits):
            b = random.randrange(0, 2)
            bitArray.append(False if b == 0 else True)
        return bitArray

    @staticmethod
    def detectsAny(selfSet, lymphocyte):
        for ss in selfSet:
            if lymphocyte.detects(ss):
                return True
        return False

    @staticmethod
    def showLymphocyteSet(lymphocyteSet):
        for idx, ls in enumerate(lymphocyteSet):
            print('{0}: {1}'.format(idx, ls.toString()))

def main():
    ArtificialImmuneSystemProgram()


if __name__ == '__main__':
    main()
