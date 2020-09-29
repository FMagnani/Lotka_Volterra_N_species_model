#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 14:18:35 2020

@author: fede
"""

def create_Strings(N):
    """
    Creates the strings needed for the dynamical generation.
    
    Parameters
    ----------
        N: int
    The dimension of the system.

    Returns
    -------
        A tuple with 5 strings.
        return[0]: The string specifying the arguments for the function 
                   'system'.
        return[1]: The string specifying the arguments for the function
                   'odeint'.
        return[2]: The string for the definition of the variables inside the
                   function 'system'.
        return[3]: The string for the definition of the solution dydt inside
                   function 'system'.
        return[4]: The string defining the system of equations itself.
    
    """

    string_vars = ''
    string_args = ''
    string_n = ''
    string_dndt = ''
    string_sys = ''
    
    for i in range(N):
        string_vars += 'k' + str(i) + ','
        
        string_args += 'k[' + str(i) + '],'
        
        string_n += 'n' + str(i) + ','
        
        string_dndt += 'dn' + str(i) + 'dt,' 
    
        
    for i in range(N):
        string_vars += 'K' + str(i) + ','
        
        string_args += 'K[' + str(i) + '],'
        
    for i in range(N):
        string_vars += 'c' + str(i) + ','
        
        string_args += 'c[' + str(i) + '],'
        
    sys = []
        
    for i in range(N):
        sys.append( 'dn'+str(i)+'dt = k'+str(i)+'*n'+str(i)+' + A'+str(i)*2
                   +('*n'+str(i))*2+'/c'+str(i) )
    
        
    for i in range(N):
        for j in range(N)[i:]:
            string_vars += 'A' + str(i) + str(j) + ','
        
            string_args += 'A[' + str(i) + '][' + str(j) + '],'
            
            if not (i==j):
                sys[i] +=' + A'+str(i)+str(j)+'*n'+str(i)+'*n'+str(j)+'/c'+str(i)
                sys[j] +=' - A'+str(j)+str(i)+'*n'+str(j)+'*n'+str(i)+'/c'+str(j)
     
    for i in range(N):
        string_sys += sys[i] + '\n'          
    
        
    return (string_vars[:-1], string_args[:-1], string_n[:-1], 
            string_dndt[:-1], string_sys)
    
    
    
    
    
  