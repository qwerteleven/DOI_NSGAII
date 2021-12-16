import glob
import os
from shutil import copyfile

def run_command(command):
    print(command)
    os.system('cmd /c ' + command)


def read_parameters_files(path):
    return glob.glob(path + "/*.in")


def save_results(path, parameters_file):
    if not os.path.exists(path):
        os.makedirs(path)

    if not os.path.exists(path + parameters_file):
        os.makedirs(path + parameters_file)

    copyfile("./all_pop.out",     path + parameters_file + '\\' + "all_pop.out")
    copyfile("./best_pop.out",    path + parameters_file + '\\' + "best_pop.out")
    copyfile("./final_pop.out",   path + parameters_file + '\\' + "final_pop.out")
    copyfile("./hyperstats.out",  path + parameters_file + '\\' + "hyperstats.out")
    copyfile("./hypervolume.out", path + parameters_file + '\\' + "hypervolume.out")
    


def main (path, random_seed):
    folder_parameters = '\\input_file'
    parameters_files = read_parameters_files(path + folder_parameters)

    for parameters_file in parameters_files:
        print('process: ', parameters_file)
        command = ".\\nsga2-gnuplot-v1.1.6\\nsga2r.exe"+ " " + str(random_seed) + " < " + parameters_file
        run_command(command)

        save_results(".\\results", '\\' + parameters_file.split('\\')[-1].split('.')[0])

    print("Done")

if __name__ == '__main__':
    path = '.'
    random_seed = 0.52
    main(path, random_seed)