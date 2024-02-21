import optparse

from src.core.universe import universe
from src.core.activevolume import activevolume
import numpy as np
import sys
import glob


def parse(tag):

    if 'file:' not in tag:
        print('Write file: before the path')
        sys.exit()
    thefiles = tag[5:len(tag)]
    return glob.glob(thefiles)
    


if __name__ == "__main__":

    parser = optparse.OptionParser(usage='usage: %prog [options] path', version='%prog 1.0')
    parser.add_option('-i', '--input', action='store', type='string', dest='inputFile', default='input.root', help='Source file')
    (opts, args) = parser.parse_args()

    fileList = parse(opts.inputFile)
    activeVol = activevolume(0.0, 0.0, 0.0, 260.0, 260.0, 300.0, 104, 104, 60)
    myUniverse = universe(0.0, 0.0, 0.0, 270.0, 270.0, 310.0, activeVol)
    #activeVol = activevolume(0.0, 0.0, 0.0, 90.0, 90.0, 30.0, 45, 45, 15)
    #myUniverse = universe(0.0, 0.0, 0.0, 100.0, 100.0, 35.0, activeVol)
    #myUniverse.print()


    myUniverse.loadData(fileList)
    #myUniverse.makePlot3D('caca.png')
    #myUniverse.make2AllSlices('XZProj', 'XZ', 3, 1.0e-2, 1.0e-1)
    
    myUniverse.makeAllProjections("Project", 5, 1.0e-3, 0.5)
    



