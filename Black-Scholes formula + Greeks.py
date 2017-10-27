# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 11:44:30 2017

@author: marco
"""

#Black-Scholes model in Python
import numpy as np
import scipy.stats as ss
import time
#Data for input in Black-Scholes formula:
    T=2.0  #supposed in years. It is not the maturity, but the time to maturity
    S=100.0
    K=105.0
    r=0.075
    vol=0.20  #supposing it is annual
    option_type='P' #for the put insert 'P'
    #dividend yield assumed to be 0
#Compute d1 and d2
d1=(np.log(S/K)+(r+0.5*vol)*T)/(vol*np.sqrt(T))
d2=d1-vol*np.sqrt(T)
if option_type in ['C','P']:
    if option_type in ['C']:
        Opt_Price=S*ss.norm.cdf(d1)-K*np.exp(-r*T)*ss.norm.cdf(d2)
        Delta=ss.norm.cdf(d1)
        Gamma=ss.norm.cdf(d1)/(S*vol*np.sqrt(T))
        Vega=S*ss.norm.cdf(d1)*np.sqrt(T)
        Theta=-(S*ss.norm.cdf(d1)*vol)/(2*np.sqrt(T))-r*K*np.exp(-r*T)*ss.norm.cdf(d2)
        Rho=K*T*np.exp(-r*T)*ss.norm.cdf(d2)
    else:
        Opt_Price=K*np.exp(-r*T)*ss.norm.cdf(-d2)-S*ss.norm.cdf(-d1)
        Delta=-ss.norm.cdf(-d1)
        Gamma=ss.norm.cdf(d1)/(S*vol*np.sqrt(T))
        Vega=S*ss.norm.cdf(d1)*np.sqrt(T)
        Theta=-(S*ss.norm.cdf(d1)*vol)/(2*np.sqrt(T))+r*K*np.exp(-r*T)*ss.norm.cdf(-d2)
        Rho=-K*T*np.exp(-r*T)*ss.norm.cdf(-d2)
else:
    Opt_Price= 'Error: option type incorrect. Choose P for a put option or C for a call option.'
print Opt_Price
print 'Delta = {}'.format(Delta)
print 'Gamma = {}'.format(Gamma)
print 'Vega = {}'.format(Vega)
print 'Theta = {}'.format(Theta)
print 'Rho = {}'.format(Rho)