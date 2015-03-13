**Mol2chemfig Web** is a web interface built on top of Mol2chemfig program maintained by [Prof. M. Palmer](http://science.uwaterloo.ca/~mpalmer/contact.html). The main goal of the project is to provide a user-friendly interface for generating and modifying chemical structures depicted in chemfig format for LaTeX documents. Web application includes the following features: 

**Integrated database search:**

Finds an inquired coumpound by name and returns a smiles string.

**Integrated Chemdoodle sketcher:**

If a requested compound was not found in the database, a user draws the structure in the [ChemDoodle sketcher](http://web.chemdoodle.com/tutorial/2d-structure-canvases/sketcher-canvas) and mol format will be generated.

**Embeded pdfviewer:**

After converting of smiles or mol format to chemfig, a pdf file with a resulted structure will be displayed in the pdfviewer.

**"Select - Apply" functionality:**

A user can modify the structure by selecting and applying desired options. A newly generated pdf displays all modifications. Currently ten options are present. Other options can be added upon request.

**Live updates on chemfig code modifications:**

A user can modify chemfig code directly (i.e. to change the angle of a bond or to change a functional group). Every single modification is synchronized with pdfviewer.

##### Local installation

If you want to run Mol2chemfig Web locally, you will need to install the following packages:

* [Flask](http://flask.pocoo.org/) -  ```pip install Flask ```

* [Pubchempy](https://github.com/mcs07/PubChemPy) - ```pip install pubchempy```

* Python-indigo  - ```sudo apt-get install python-indigo```

* Pdflatex

Also, you will need to modify a path to mol2chemfig.sty file (m2pkg_path in mol2chemfig/pdfgen.py) in order to get a pdf file generated. 

##### Acknowledgments

I would like to acknowledge the work of all the authors of programs/libraries (Chemfig, Mol2chemfig, ChemDoodle Web Components, PubchemPy, Indigo) I used to develop the web interface.

##### License

Mol2chemfig Web (web interface only) is licensed under version 3 of the [GNU GENERAL PUBLIC LICENSE](https://www.gnu.org/licenses/gpl-3.0.html)

##### Comments/suggestions/bug reports

Comments, suggestions, bug reports and constructive critic are very welcomed and can be sent to py.chemist@gmail.com
