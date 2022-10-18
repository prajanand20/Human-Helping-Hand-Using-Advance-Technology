import ctypes

SPI_WALLPAPER=0x14
SPIF_UPDATINGFILE =0x2

source=r"E:\c\my_assistant\images"

ctypes.windll.user32.SystemParametersInfoW(SPI_WALLPAPER,0,source,SPIF_UPDATINGFILE)
