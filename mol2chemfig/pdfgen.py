'''
generate a pdf from a parsed mol2chemfig molecule.
return the result in a string.
'''
import os, shutil
from tempfile import mkdtemp
from pathlib import Path

latexfn = 'molecule.tex'
pdfname = 'molecule.pdf'
latexcmd = 'pdflatex -interaction=nonstopmode -verbose %s' % latexfn

m2pkg_path = 'mol2chemfig'
pkg = 'mol2chemfig.sty'

def pdfgen(mol):
    tempdir = mkdtemp()
    shutil.copy(Path(m2pkg_path) / pkg, Path(tempdir) / pkg)
	

    chemfig = mol.render_server()    
    width, height = mol.dimensions()

    atomsep = 35
    fixed_extra = 30
    
    width = round(atomsep * width) + fixed_extra
    height = round(atomsep * height) + fixed_extra
    
    global width_all, height_all
    width_all = width
    height_all = height
    
    latex = latex_template % locals()
    
    curdir = os.getcwd()
    os.chdir(tempdir)

    open(latexfn, 'w').write(latex)
    os.system(latexcmd)

    try:
        pdfstring = open(pdfname, "rb").read()
    except IOError:
        return False, None
    finally:
        os.chdir(curdir)
        shutil.rmtree(tempdir)

    return True, pdfstring
    
def update_pdf(mol):
    tempdir = mkdtemp()
    # create the symlink to the mol2chemfig package
    os.symlink(m2pkg_path + pkg, tempdir + pkg)

    chemfig = "\chemfig {"+ mol +"}"
    
    atomsep = 16
    fixed_extra = 28    

    width = width_all
    height = height_all
    
    latex = latex_template % locals()

    curdir = os.getcwd()
    os.chdir(tempdir)

    open(latexfn, 'w').write(latex)
    os.system(latexcmd)

    try:
        pdfstring = open(pdfname).read()
    except IOError:
        return False, None
    finally:
        os.chdir(curdir)
        shutil.rmtree(tempdir)

    return True, pdfstring



latex_template = r'''
\documentclass{minimal}
\usepackage{xcolor, mol2chemfig}
\usepackage[margin=(margin)spt,papersize={%(width)spt, %(height)spt}]{geometry}

\usepackage[helvet]{sfmath}
\setcrambond{2.5pt}{0.4pt}{1.0pt}
\setbondoffset{1pt}
\setdoublesep{2pt}
\setatomsep{%(atomsep)spt}
\renewcommand{\printatom}[1]{\fontsize{8pt}{10pt}\selectfont{\ensuremath{\mathsf{#1}}}}

\setlength{\parindent}{0pt}
\setlength{\fboxsep}{0pt}
\begin{document}
\vspace*{\fill}
\vspace{-8pt}
\begin{center}
%(chemfig)s
\end{center}
\vspace*{\fill}
\end{document}
'''
