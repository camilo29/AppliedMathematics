# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 12:11:13 2014

@author: juanmanlass
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

