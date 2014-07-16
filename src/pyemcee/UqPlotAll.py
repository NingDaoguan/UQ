#
#  UQBox plotter code (pronounced like "jukebox" without the "j")
#
# chief software engineer: Marcus Day
# helper elf programmers:  Jonathan Goodman (goodman@cims.nyu.edu)
#                          John Bell
#                          Matthias Morzfeld

#  Read a datafile and make plots

import numpy             as np
import matplotlib.pyplot as pl
import sys

#    Unpack the data, see "test.py" to see how it's packed

import cPickle as pc

infile = sys.argv[1]

with open(infile, 'rb') as ResultsFile:
  Output = pc.load( ResultsFile)

OutNames = Output[0]
OutDict  = Output[1]

for name in OutNames:
  CommString = name + " =  OutDict['" +  name + "']"
  exec CommString


# Compute and plot auto-correlation functions for each variable

maxLag = 2000   # Length of the auto-correlation series to calculate and plot
hAxis  = np.arange(0, maxLag)  # horizontal axis values
import acor as ac

pl.figure()
for k in range(0,ndim):
  C = ac.acor( x[0,:,k], maxLag)
  labelString = "var " + str(k)
  pl.plot( hAxis, C, label = labelString)

titleString = "Autocorrelations for first walker"
titleString = titleString + ", T = " + str(nChainLength)
titleString = titleString + ", L = " + str(nwalkers)

pl.title(titleString)
pl.legend()
pl.grid('on')
pl.savefig(infile + '_AcorVars.pdf')

pl.figure()
maxWalker = 5
var       = 0
for walker in range(0,maxWalker):
  C = ac.acor( x[ walker, : , var], maxLag)
  labelString = "walker " + str(walker)
  pl.plot( hAxis, C, label = labelString)

titleString = "Autocorrelations for variable " + str(var)
titleString = titleString + ", T = " + str(nChainLength)
titleString = titleString + ", L = " + str(nwalkers)

pl.title(titleString)
pl.legend()
pl.grid('on')
pl.savefig(infile + '_AcorWalkers.pdf')

pl.figure()
v0 = np.reshape( x[:,:,0], [nwalkers*nChainLength])
v1 = np.reshape( x[:,:,1], [nwalkers*nChainLength])

stride = 127
v0p = v0[0:nwalkers*nChainLength:stride]   # subsample for plotting
v1p = v1[0:nwalkers*nChainLength:stride]

pl.plot(v0p,v1p,'.')
pl.xlabel('var 0')
pl.ylabel('var 1')
pl.title('scatterplot, var 0 vs. var 1')
pl.grid('on')
pl.savefig(infile + '_Scatterplot.pdf')

pl.figure()
stride = 29
v0p = v0[0:nwalkers*nChainLength:stride]   # subsample for plotting
v1p = v1[0:nwalkers*nChainLength:stride]
pl.hist2d( v0p,v1p, bins=80)
pl.colorbar()
pl.xlabel('var 0')
pl.ylabel('var 1')
pl.title('scatterplot, var 0 vs. var 1')
pl.savefig(infile + '_Histogram2d.pdf')



