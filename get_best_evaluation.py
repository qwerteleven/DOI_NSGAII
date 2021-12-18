import glob


def read_stats_files(path):
    return glob.glob(path + "/*/hyperstats.out")

def get_final_value(file):
    X = 0
    f = open(file, "r")
    lines = f.readlines()
    X = float(lines[-2].split(' ')[-2])
    f.close()

    return X


def main(path):
    stats_files = read_stats_files(path)
    
    final_value = []

    for stats_file in stats_files:
        final_value.append((get_final_value(stats_file), stats_file))

    final_value.sort(key=lambda x: -x[0])

    print("best_values: ", [i for i in final_value[0:10]])

    print("worst_values: ", [i for i in final_value[-10:-1]])

    print("Done")


if __name__ == '__main__':
    path = './results'
    main(path)