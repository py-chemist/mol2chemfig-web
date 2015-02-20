Mol2chemfig Web is a web interface built on top of Mol2chemfig program maintained by Prof. M. Palmer(a huge THANK YOU!). The main goal of the project is to provide a user-friendly interface for generating and modifying chemical structures depicted in chemfig format for LaTeX documents. Web application includes the following features: 

**Integrated database search:**

    Finds an inquired coumpound by name and returns a smiles string.

**Integrated Chemdoodle sketcher:**
If a requested compound was not found in the database, a user draws the structure and mol format is generated.

##### Embeded pdfviewer
After converting of smiles or mol format to chemfig, a pdf file with a resulted structure will be displayed in the pdfviewer.

**"Select - Apply" fuctionality:**
A user can modify the structure by selecting and applying desired options. A newly generated pdf displays all modifications. Currently ten options are present. Other options can be added upon request.

**Live updates on chemfig code modifications:**
A user can modify chemfig code directly (i.e. to change the angle of a bond or to change a functional group). Every single modification is synchronized with pdfviewer.
