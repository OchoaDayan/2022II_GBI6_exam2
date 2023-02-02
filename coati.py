
def fasta_downloader():
    """Carga el id_coati.txt en id_coatiy descargar en formato genbank la información correspondiente a los identificadores de accesión usando el ENTREZ de Biopythony se guardar en coati y en coati.gb."""
    sequence = ""  
    with open("data/coati.txt") as coati:
        name = coati.readline()[0:-1]
        for line in coati:
        sequence += line.replace("\n","")
    return [sequence]

def alignment():
    """Extrae solamente las secuencias de la variable coati y realiza un alineamiento usando clustalW. El resultado se guardan en los archivos coati.aln y coati.dnd que se guardan en su carpeta de trabajo."""
    return[aligment]

def tree():
    """Realiza el cálculo de las distancias utilizando coati.aln e imprime en la pantalla el árbol filogenético y guarda en su carpeta de trabajo el árbol"""
    return[treee]