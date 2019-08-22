##### Parameters for gauss integration####
# coordinate of integration point
ipcoor = 0.577350269189626
# gauss weight
gweight = 1.
#
##########################################
# initialize local coordinates of integration points
allxi =  [ -ipcoor, ipcoor, -ipcoor, ipcoor, -ipcoor, ipcoor, -ipcoor, ipcoor]
alleta =  [ -ipcoor, -ipcoor, ipcoor, ipcoor, -ipcoor, -ipcoor, ipcoor, ipcoor]
allzeta = [ -ipcoor, -ipcoor, -ipcoor, -ipcoor, ipcoor, ipcoor, ipcoor, ipcoor]
# initialize local coordinates of nodes
allnodexi = [ -1., 1., 1., -1., -1., 1., 1., -1.]
allnodeeta = [ -1., -1., 1., 1., -1., -1., 1., 1. ]
allnodezeta = [ -1., -1., -1., -1., 1., 1., 1., 1. ]