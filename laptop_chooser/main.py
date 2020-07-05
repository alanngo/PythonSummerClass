from laptop_chooser.specs import *
import matplotlib.pyplot as plt
import numpy as np


def general_score(cpu, ram, storage):
    return (cpu + ram + storage) / 3


def gaming_score(cpu, ram, storage, gpu):
    return (cpu + ram + storage + gpu) / 4


def graph(cpu, ram, ssd, gpu):
    objects = ('General Score', 'Gaming Score')

    general = general_score(cpu, ram, ssd)
    gaming = gaming_score(cpu, ram, ssd, gpu)

    y_pos = np.arange(len(objects))
    performance = [general, gaming]

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Usage')
    plt.title('Programming language usage')

    plt.show()


def main():
    cpu = get_cpu(input("Enter CPU: "))
    ram = get_ram(int(input("Enter RAM amount: ")))
    ssd = get_storage(int(input("Enter SSD amount: ")))
    gpu = get_gpu(input("Enter GPU: "))

    score = gaming_score(cpu, ram, ssd, gpu)
    print(str(score))
    graph(cpu, ram, ssd, gpu)


main()
