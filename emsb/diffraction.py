import matplotlib.pyplot
import numpy
# import Bio.PDB

_parameters = {"C": [2.31, 20.8439, 1.02, 10.2075, 1.5886, 0.5687, 0.865, 51.6512, 0.2156],
               "N": [12.2126, 0.0057, 3.1322, 9.8933, 2.0125, 28.9975, 1.1663, 0.5826, -11.529],
               "O": [3.0485, 13.2771, 2.2868, 5.7011, 1.5463, 0.3239, 0.867, 32.9089, 0.2508],
               "P": [6.4345, 1.9067, 4.1791, 27.157, 1.78, 0.526, 1.4908, 68.1645, 1.1149],
               "S": [6.9053, 1.4679, 5.2034, 22.2151, 1.4379, 0.2536, 1.5863, 56.172, 0.8669]}

def structure_factor(element, s):
    if element not in _parameters:
        raise ValueError("Element {} is not recognized".format(element))
    s_A_half = s*1e-10/2
    p = _parameters[element]
    return (p[0]*numpy.exp(-p[1]*s_A_half**2) +
            p[2]*numpy.exp(-p[3]*s_A_half**2) +
            p[4]*numpy.exp(-p[5]*s_A_half**2) +
            p[6]*numpy.exp(-p[7]*s_A_half**2) + p[8])

    
# def read_pdb(file_name):
#     parser = Bio.PDB.PDBParser()
#     structure = parser.get_structure("Protein", file_name)
#     pos_x = [a.coord[0]*1e-10 for a in structure.get_atoms()]
#     pos_y = [a.coord[1]*1e-10 for a in structure.get_atoms()]
#     pos_z = [a.coord[2]*1e-10 for a in structure.get_atoms()]
#     element = [a.element for a in structure.get_atoms()]
#     return pos_x, pos_y, pos_z, element

def read_pdb(file_name):
    pos_x = []
    pos_y = []
    pos_z = []
    element = []
    with open(file_name) as file_handle:
        for line in file_handle.readlines():
            if (line[:4] == "ATOM" or
                line[:6] == "HEATOM"):
                pos_x.append(float(line[30:38])*1e-10)
                pos_y.append(float(line[38:46])*1e-10)
                pos_z.append(float(line[46:54])*1e-10)
                element.append(line[13])
    return pos_x, pos_y, pos_z, element
            
