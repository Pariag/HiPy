# Copyright ESIEE (2015) 
# 
# benjamin.perret@esiee.fr
# 
#
# This software is governed by the CeCILL license under French law and
# abiding by the rules of distribution of free software.  You can  use, 
# modify and/ or redistribute the software under the terms of the CeCILL
# license as circulated by CEA, CNRS and INRIA at the following URL
# "http://www.cecill.info". 

# As a counterpart to the access to the source code and  rights to copy,
# modify and redistribute granted by the license, users are provided only
# with a limited warranty  and the software's author,  the holder of the
# economic rights,  and the successive licensors  have only  limited
# liability. 

# In this respect, the user's attention is drawn to the risks associated
# with loading,  using,  modifying and/or developing or reproducing the
# software by the user in light of its specific status of free software,
# that may mean  that it is complicated to manipulate,  and  that  also
# therefore means  that it is reserved for developers  and  experienced
# professionals having in-depth computer knowledge. Users are therefore
# encouraged to load and test the software's suitability as regards their
# requirements in conditions enabling the security of their systems and/or 
# data to be ensured and,  more generally, to use and operate it in the 
# same conditions as regards security. 

# The fact that you are presently reading this means that you have had
# knowledge of the CeCILL license and that you accept its terms.

"""
Demonstration of a simple use of a Max Tree to perform an area filter.

Created on 9 juin 2015

@author: Benjamin Perret
"""
from HiPy.IO import *  # @UnusedWildImport
from HiPy.Structures import *  # @UnusedWildImport
from HiPy.Hierarchies.ComponentTree import *  # @UnusedWildImport
from HiPy.Processing.Attributes import *  # @UnusedWildImport


def testAreaFilter():
    """
    Performs a simple area filter on a sample image using a max tree.
    """
    print("Reading image")
    image = readImage('../samples/lennaGray256.png', grayScale=True)
    image.adjacency = AdjacencyNdRegular.getAdjacency2d4(image.embedding.size)

    print("Tree construction")
    tree = constructComponentTree(image, ComponentTreeType.MaxTree)
    addAttributeArea(tree)

    print("Filtering and reconstruction")
    reconstruction = tree.reconstructImage("level", lambda x: tree.area[x] <= 10000)

    resultName = 'Results/reconstructionAreaFilter_MaxTree.png'
    print("Saving result: " + resultName)
    saveImage(reconstruction, resultName)


def main():
    """
    Simple demo function launcher.
    :return: void
    """
    HiPyLogger.setLevel(logging.DEBUG)
    print("--- Area filter on the max tree")
    testAreaFilter()


if __name__ == '__main__':
    main()
