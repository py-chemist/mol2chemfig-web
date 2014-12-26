# from http://www.dalkescientific.com/writings/diary/archive/2011/06/04/dealing_with_sssr.html
# I suppose we can find those bonds in the molecule somehow

def indigo_count_aromatic_rings(mol):
    count = 0
    mol.aromatize() # XXX missing from chemfp!
    for ring in mol.iterateSSSR():
        # bond-order == 4 means "aromatic"; all rings bonds must be aromatic
        if all(bond.bondOrder() == 4 for bond in ring.iterateBonds()):
            count += 1
    return count