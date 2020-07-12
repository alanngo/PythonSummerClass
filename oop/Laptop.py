# score laptop based on cpu, gpu, ram, ssd
# claculate gaming score
# calculate general score
# 1: entry level, 2: mainstream, 3: performance, 4: enthusiast
# gaming score: avg of cpu gpu, ram, ssd
def score_cpu(cpu):
    if "3" in cpu:
        return 1
    if "5" in cpu:
        return 2
    if "7" in cpu:
        return 3
    if "9" in cpu:
        return 4
    if "xeon" in cpu:
        return 5
    if "threadripper" in cpu:
        return 5

def score_gpu(gpu):
    if "50" in gpu:
        return 1
    if "60" in gpu:
        return 2
    if "70" in gpu:
        return 3
    if "80" in gpu:
        return 4
    if "titan" in gpu:
        return 5


def score_ram(ram):
    if ram >= 4:
        return 1
    if ram >= 8:
        return 2
    if ram >= 16:
        return 3
    if ram >= 32:
        return 4
    raise RuntimeError("UPGRADE YOUR RAM!")

def score_ssd(ssd):
    if ssd >= 256:
        return 1
    if ssd >= 512:
        return 2
    if ssd >= 1000:
        return 3
    if ssd >= 2000:
        return 4
    raise RuntimeError("TOO LOW OF AN SSD")


class Laptop:
    def __init__(self, cpu, ram, ssd, gpu):
        cpu_score = \
            {
                "i3": 1,
                "i5": 2,
                "i7": 3,
                "i9": 4
            }
        self.cpu = score_cpu(cpu)
        self.gpu = score_gpu(gpu)
        ram_score = \
            {
                4: 1,
                8: 2,
                16: 3,
                32: 4
            }
        self.ram = score_ram(ram)
        ssd_score = \
            {
                256: 1,
                512: 2,
                1000: 3,
                2000: 4

            }
        self.ssd = score_ssd(ssd)

    def general_score(self):
        return (self.cpu + self.ram + self.ssd) / 3

    def gaming_score(self):
        return (self.cpu + self.ram + self.ssd + self.gpu) / 4
