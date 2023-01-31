#!/usr/bin/python
# -*- coding: utf-8 -*-

from mol2chemfig.processor import process
from mol2chemfig import pdfgen
from mol2chemfig.pdfgen import update_pdf
import os, base64
import pubchempy as pcp

def smiles_mol_to_chemfig(*args):
    all_args = ''
    for i in args:
        all_args += i + ' '
    success, result = process(rawargs = all_args, progname = 'mol2chemfig')
    if success:
        pdfsuccess, pdfresult = pdfgen.pdfgen(result)        
        if pdfsuccess:
            encoded = base64.b64encode(pdfresult).decode("utf-8")
            pdflink = "data:application/pdf;base64,{}".format(encoded)
        else:
            pdflink = 'pdf generation foobared'
    else:
        raise ValueError(result)

    try:    
        outcome = result.render_user()
        return outcome, pdflink 
    except AttributeError as e:
        print(e)
        error = "Chemfig cannot be generated"
        return None, error
        
def update_chemfig(data):
    pdfsuccess, pdfresult = update_pdf(data)           
    if pdfsuccess:
        encoded = base64.encodestring(pdfresult)
        pdflink = "data:application/pdf;base64,{}".format(encoded)
    else:
        pdflink = 'pdf generation foobared'
    
    return pdflink 

    
def get_name(name):
    chemical_name = pcp.get_compounds(name, 'name')
    try:
        return chemical_name[0].isomeric_smiles
    except IndexError:
        return "\n"
        
        
