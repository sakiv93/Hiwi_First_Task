##### Parameters for gauss integration####
# coordinate of integration point

ipcoor= 0.7745966692414834

# gauss weights
gweight_1 = 0.8888888888888889 #gauss weight for coordinate 0
gweight_2 = 0.5555555555555556 #gauss weight for coordinate 0.7745966692414834

#For gauss weight multiplication purpose

gweight_xi =  [ -gweight_2, gweight_1, gweight_2, -gweight_2, gweight_1, gweight_2, -gweight_2, gweight_1, gweight_2, -gweight_2, gweight_1, gweight_2, -gweight_2, gweight_1, gweight_2, -gweight_2, gweight_1, gweight_2, -gweight_2, gweight_1, gweight_2, -gweight_2, gweight_1, gweight_2, -gweight_2, gweight_1,, gweight_2]
gweight_eta = [ -gweight_2, -gweight_2, -gweight_2, gweight_1, gweight_1, gweight_1, gweight_2, gweight_2, gweight_2, -gweight_2, -gweight_2, -gweight_2, gweight_1, gweight_1, gweight_1, gweight_2, gweight_2, gweight_2, -gweight_2, -gweight_2, -gweight_2, gweight_1, gweight_1, gweight_1, gweight_2, gweight_2, gweight_2]
gweight_eta = [ -gweight_2, -gweight_2, -gweight_2, -gweight_2, -gweight_2, -gweight_2, -gweight_2, -gweight_2, -gweight_2, gweight_1, gweight_1, gweight_1, gweight_1, gweight_1, gweight_1, gweight_1, gweight_1, gweight_1, gweight_2, gweight_2, gweight_2, gweight_2, gweight_2, gweight_2, gweight_2, gweight_2, gweight_2]



# initialize local coordinates of integration points
allxi =  [ -ipcoor, 0, ipcoor, -ipcoor, 0, ipcoor, -ipcoor, 0, ipcoor, -ipcoor, 0, ipcoor, -ipcoor, 0, ipcoor, -ipcoor, 0, ipcoor, -ipcoor, 0, ipcoor, -ipcoor, 0, ipcoor, -ipcoor, 0,, ipcoor]
alleta =  [ -ipcoor, -ipcoor, -ipcoor, 0, 0, 0, ipcoor, ipcoor, ipcoor, -ipcoor, -ipcoor, -ipcoor, 0, 0, 0, ipcoor, ipcoor, ipcoor, -ipcoor, -ipcoor, -ipcoor, 0, 0, 0, ipcoor, ipcoor, ipcoor]
allzeta = [ -ipcoor, -ipcoor, -ipcoor, -ipcoor, -ipcoor, -ipcoor, -ipcoor, -ipcoor, -ipcoor, 0, 0, 0, 0, 0, 0, 0, 0, 0, ipcoor, ipcoor, ipcoor, ipcoor, ipcoor, ipcoor, ipcoor, ipcoor, ipcoor]


# initialize local coordinates of nodes

allnodexi = [ -1., 1., 1., -1., -1., 1., 1., -1., 0., 1., 0., -1., 0., 1., 0., -1., -1., 1., 1., -1. ]
allnodeeta = [ -1., -1., 1., 1., -1., -1., 1., 1., -1., 0., 1., 0., -1., 0., 1., 0., -1., -1., 1., 1. ]
allnodezeta = [ -1., -1., -1., -1., 1., 1., 1., 1., -1., -1., -1., -1., 1., 1., 1., 1., 0., 0., 0., 0. ]