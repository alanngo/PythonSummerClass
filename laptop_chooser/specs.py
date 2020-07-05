ENTRY_LEVEL = 1
MAINSTREAM = 2
PERFORMANCE = 3
ENTHUSIAST = 4


def get_cpu(sku):
    if "i3" in sku:
        return ENTRY_LEVEL
    if "i5" in sku:
        return MAINSTREAM
    if "i7" in sku:
        return PERFORMANCE
    if "i9" in sku:
        return ENTHUSIAST
    return 0


def get_ram(gb):
    if 4 <= gb < 8:
        return ENTRY_LEVEL
    if 8 <= gb < 16:
        return MAINSTREAM
    if 16 <= gb < 32:
        return PERFORMANCE
    if gb >= 32:
        return ENTHUSIAST
    return 0


def get_storage(gb):
    if 256 <= gb < 512:
        return ENTRY_LEVEL
    if 512 <= gb < 1000:
        return MAINSTREAM
    if 1000 <= gb < 2000:
        return PERFORMANCE
    if gb >= 2000:
        return ENTHUSIAST
    return 0


def get_gpu(sku):
    if "50" in sku:
        return ENTRY_LEVEL
    if "60" in sku:
        return MAINSTREAM
    if "70" in sku:
        return PERFORMANCE
    if "80" in sku:
        return ENTHUSIAST
    return 0
