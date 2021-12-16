import os 
from itertools import product 


def make_parameters_files(path):

    '''
    Test problem CTP8
        # of real variables = 2
        # of bin variables = 0
        # of objectives = 2
        # of constraints = 2

    popsize: This variable stores the population size (a multiple of 4)  (20 - 8.000)
    ngen: Number of generations                                          (25 - 500)                                         
    
        nobj: Number of objectives                                  2
        ncon: Number of constraints                                 2
        nreal: Number of real variables                             2

    min_realvar[i]: minimum value of i^{th} real variable           0 -> 1
    max_realvar[i]: maximum value of i^{th} real variable           0 -> 10

    pcross_real: probability of crossover of real variable          (0.6 - 1.0)

    pmut_real: probability of mutation of real variable             (0.4 - 0.6)

    eta_c: distribution index for real variable SBX crossover       (5 - 20)
    eta_m: distribution index for real variable polynomial mutation (5 - 50)

    nbin: number of binary variables                                 0
    choice: option to display the data realtime using gnuplot        0
    
    '''


    folder = '/input_file'
    parameters = [-1, -1, 2, 2, 2, 0, 1, 0, 10, -1, -1, -1, -1, 0, 0]
    index = 0

    if not os.path.exists(path + folder):
        os.makedirs(path + folder)

    parameter_ranges = [
        [i for i in range(20, 4000, 320)], #popsize
        [i for i in range(25, 400, 50)],   #ngen
        [i * 0.1 for i in range(6, 10)],   #pcross_real
        [i * 0.1 for i in range(4, 6)],    #pmut_real
        [i for i in range(5, 20, 8)],      #eta_c
        [i for i in range(5, 50, 10)]      #eta_m
    ]


    for popsize, ngen, pcross_real, pmut_real, eta_c, eta_m in product(*parameter_ranges): 

        parameters[0]  = popsize
        parameters[1]  = ngen
        parameters[9] = pcross_real
        parameters[10] = pmut_real
        parameters[11] = eta_c
        parameters[12] = eta_m

        write_file(path + folder, index, parameters)
        
        index += 1



def write_file(path, index, parameters):

    f = open(path + '/ctp8' + '_' + str(index) + '.in', 'x')
    
    for parameter in parameters:
        f.write(str(parameter) + ' ')
        f.write("\n")
    f.close()


def main(path):
    make_parameters_files(path)
    print("Done")

if __name__ == '__main__':
    path = '.'
    main(path)