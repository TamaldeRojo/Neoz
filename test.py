import platform
import os
# import sys
# import cpuinfo
# import psutil
import wmi

# print(os.path)
# print(os.name)
#print(os.getcwd()) #Dir actual ruta
# print(os.chdir("..")) 
# print(os.listdir())
# os.mkdir("dir")

# print(sys.platform) #win32
# # sys.exit() #terminar programa
# # print(sys.getwindowsversion())
# # print(sys.modules)
# # print(sys.version) #python version
# # print(sys.version_info)

# print(platform.machine()) #arquitectura del procesador
# print(platform.processor())
# print(platform.platform())
# print(platform.system())
# print(platform.uname())

# c = cpuinfo.get_cpu_info()
pc = wmi.WMI()

# # Hardware
# processor = c['brand_raw']
# processorInfo = platform.processor()
# processorFrecFriendly = c['hz_actual_friendly']
# processorFrecAdvertised = c['hz_advertised_friendly']

# arch = c['arch']

# memoryRamTotal = psutil.virtual_memory().total / 1024 ** 3
# memoryRamCurrent = psutil.virtual_memory().used / 1024 ** 3
# memoryRamAvailable = psutil.virtual_memory().free / 1024 ** 3
# #OS
# sysOs = sys.platform


# prints
# print(f"Processor: {processor}")
# print(f"Processor Info: {processorInfo}")
# print(f"Processor Frequency: {processorFrecAdvertised}")
# print(f"Processor Frequency: {processorFrecFriendly}")

# print(f"Architecture: {c['arch']}")

# print(f"Total Ram: {memoryRamTotal:.3f} GB")
# print(f"Ram in use: {memoryRamCurrent:.3f} GB")
# print(f"Ram available: {memoryRamAvailable:.3f} GB")

# print(f"Operating System: {sysOs}")

# print("----------------------------------------")
#print(pc.Win32_OperatingSystem()[0])
#print(pc.Win32_Processor()[0])
#print(pc.Win32_VideoController()[0])
# print(pc.Win32_NetworkAdapterConfiguration()[0])
# print(pc.Win32_Share()[0]) #nose
# print(pc.Win32_Printer()[0]) 
#print(pc.Win32_DiskDrive()[0]) 
# print(pc.Win32_Desktop()[0]) 
# print(pc.Win32_LogicalDisk()[0])
#print(pc.Win32_ComputerSystem()[0])
#print(pc.Win32_Group()[0]) 
#print(pc.Win32_Group()[0]) 




