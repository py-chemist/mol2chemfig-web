from flask import Flask, render_template, url_for, request, jsonify
from chemistry.chemfig import smiles_mol_to_chemfig, get_name, update_chemfig
import os

app = Flask(__name__)

@app.route('/mol_2_chemfig')
def home():    
    return render_template('home.html', pdflink = "static/files/welcome.pdf")

@app.route('/mol_2_chemfig/links')
def links():
    return render_template("links.html")
    
@app.route('/mol_2_chemfig/about')
def about():
    return render_template("about.html")

@app.route("/mol_2_chemfig/_get_smiles")
def get_smile():
    chemical = request.args.get('chemical')
    name = get_name(chemical)
    return  jsonify(smiles = name)

# Keeps track of the last content in the text area
last_data = ["text"]
    
@app.route("/mol_2_chemfig/smiles_to_chemfig")
def smiles_to_chemfig():
    smiles_mol = request.args.get("smiles_mol")
    last_data[0] = smiles_mol
    check = request.args.getlist('check')
    check = check[0].split(',')
    angle = request.args.get('angle')
    angle = " -a " + angle
    lst = ' '.join(check) + angle
    hydrogens = request.args.get("hydrogens")
    if len(smiles_mol) < 200:
        chemfig, pdflink = smiles_mol_to_chemfig(lst,'-i direct', "-y {}".format(hydrogens), smiles_mol)
        return jsonify(chem_fig = chemfig, pdf_link = pdflink)        
    else:
         with open('static/files/molecule.mol', 'w') as f:
             f.write(smiles_mol)
         mol = 'static/files/molecule.mol'
         last_data[0] = mol
         chemfig, pdflink  = smiles_mol_to_chemfig(lst, "-y {}".format(hydrogens), mol)
         return jsonify(chem_fig = chemfig, pdf_link = pdflink)

@app.route("/mol_2_chemfig/update")
def check_update():    
    check = request.args.getlist('check')
    check = check[0].split(',')
    angle = request.args.get('angle')
    angle = " -a " + angle
    lst = ' '.join(check) + angle
    smiles_mol = last_data[0]
    hydrogens = request.args.get("hydrogens")
    if 'molecule.mol' not in smiles_mol:
        chemfig, pdflink = smiles_mol_to_chemfig(lst,'-i direct', "-y {}".format(hydrogens), smiles_mol) 
        return jsonify(chem_fig = chemfig, pdf_link = pdflink)
        
    else:
        chemfig, pdflink = smiles_mol_to_chemfig(lst, "-y {}".format(hydrogens), smiles_mol)
        return jsonify(chem_fig = chemfig, pdf_link = pdflink)
        
@app.route("/mol_2_chemfig/update_chemfig")
def chemfig_update():
    smiles_mol = request.args.get("smiles_mol")
    pdflink = update_chemfig(smiles_mol)         
    return jsonify(pdf_link = pdflink)
    

if __name__ == '__main__':
    app.run(debug=True)
    
