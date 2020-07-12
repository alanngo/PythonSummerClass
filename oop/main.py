from oop.student import *
from oop.Bank import *
from oop.Laptop import *

def main():
    # s = Student(20, 30, 40)
    # print(s.calc_avg())
    #
    # account = Bank(32)
    # account.deposit(42)
    # print(account.get_balance())

    eluktronics = Laptop(cpu="r7", ram=256, ssd=3000, gpu="titan RTX")
    gen_score = format(eluktronics.general_score(), ".3f")
    gaming_score = format(eluktronics.gaming_score(), ".3f")
    print("General Score "+str(gen_score))
    print("gaming score "+str(gaming_score))


main()
