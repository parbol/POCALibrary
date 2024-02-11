from src.core.muon import muon
from src.core.voxel import voxel
from src.core.universe import universe
from src.core.activevolume import activevolume
from src.tools.vector import vector
from src.tools.line import line
from src.tools.plane import plane
from src.tools.confparser import confparser


if __name__ == "__main__":

    myconf = confparser('config.json')
    activeVol = activevolume(myconf)
    myUniverse = universe(myconf, activeVol)
    myUniverse.print()

    myUniverse.loadData('datos.root')
   



