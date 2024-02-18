import optparse

from src.core.universe import universe
from src.core.activevolume import activevolume



if __name__ == "__main__":

    parser = optparse.OptionParser(usage='usage: %prog [options] path', version='%prog 1.0')
    parser.add_option('-i', '--input', action='store', type='string', dest='inputFile', default='input.root', help='Source file')
    (opts, args) = parser.parse_args()

    activeVol = activevolume(0.0, 0.0, 0.0, 260.0, 260.0, 300.0, 52, 52, 30)
    myUniverse = universe(0.0, 0.0, 0.0, 270.0, 270.0, 310.0, activeVol)
    #myUniverse.print()

    myUniverse.loadData(opts.inputFile)
    #myUniverse.makePlot3D('caca.png')
    myUniverse.makeAllSlices('XZProj', 'XZ', 3, 1.0e-2, 1.0e-1)





