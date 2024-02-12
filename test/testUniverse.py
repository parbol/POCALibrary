import optparse

from src.core.universe import universe
from src.core.activevolume import activevolume



if __name__ == "__main__":

    parser = optparse.OptionParser(usage='usage: %prog [options] path', version='%prog 1.0')
    parser.add_option('-i', '--input', action='store', type='string', dest='inputFile', default='input.root', help='Source file')
    (opts, args) = parser.parse_args()

    activeVol = activevolume(0.0, 0.0, 0.0, 90.0, 90.0, 40.0, 10, 10, 10)
    myUniverse = universe(0.0, 0.0, 0.0, 100.0, 100.0, 50.0, activeVol)
    myUniverse.print()

    myUniverse.loadData(opts.inputFile)
   



