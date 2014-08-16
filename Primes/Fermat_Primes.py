# -*- coding: utf-8 -*-
"""
Author: Alejandro Cardenas-Avendano & Sebastían Mancipe

email: alejandro.cardenasa@konradlorenz.edu.co
Website: https://github.com/alejandroc137
License: BSD
Please feel free to use and modify this, but keep the above information. Thanks!
"""

n = 20
for i in xrange(0,n,1):
  print 'Entero: '
  print ((2**(2**i))+1)
  print '========================================'
  print 'Binario: '
  print bin((2**(2**i))+1)
  print '========================================'
  print 'Fin del (%i) número de Fermat' %(i)

