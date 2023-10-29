import datetime
import customtkinter as ctk
import tkinter as tk
import wmi
import threading
from psutil import disk_partitions,disk_usage,virtual_memory,cpu_percent 

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


#Settings

app = ctk.CTk()

app.title("Neoz")
app.geometry("900x400")

#End Settings
def getCpuValues():
    pc = wmi.WMI()
    while True:
        # processorData = pc.Win32_Processor()[0]
        # processorData = retrieveData()
        videoControllerData = pc.Win32_VideoController()[0]
        osData = pc.Win32_OperatingSystem()[0]
        computerSysData = pc.Win32_ComputerSystem()[0]
        diskData = pc.Win32_DiskDrive()[0]
        logicalDisk = pc.Win32_LogicalDisk()[0]
        # groupsData = pc.Win32_Group()[0]
        # printerData = pc.Win32_Printer()[0]
        processorData = pc.Win32_Processor()[0]
        
        processorName = processorData.Name
        processorCores = processorData.NumberOfCores
        numberOfLogicalProcessors = processorData.NumberOfLogicalProcessors
        osNameData = osData.Caption
        osUserData = osData.CSName
        videoControllerName = videoControllerData.Caption
        videoControllerRam = videoControllerData.AdapterRam * -1/1024**3
        diskSize = int(diskData.Size) /1024**3
        logicalDiskName = logicalDisk.CreationClassName
        logicalDiskDeviceId = logicalDisk.DeviceID
        logicalDiskFreeSpace = logicalDisk.FreeSpace
        logicalDiskSize = int(logicalDisk.Size) 
        computerSysOwnerEmail = computerSysData.PrimaryOwnerName 
        
        processorNameTk.set(f'{processorName}')
        processorCoresValueTk.set(f'{processorCores}')
        processorThreadsValueTk.set(f"{numberOfLogicalProcessors}")
        osNameValueTk.set(f"{osNameData}")
        osUserValueTk.set(f"{osUserData}")
        videoControllerNameTk.set(f"{videoControllerName}")
        videoControllerRamTk.set(f"{videoControllerRam} Gb")
        diskSizeTk.set(f"{diskSize}")
        logicalDiskNameTk.set(f"{logicalDiskName}")
        logicalDiskDeviceIdTk.set(f"{logicalDiskDeviceId}")
        logicalDiskFreeSpaceTk.set(f"{logicalDiskFreeSpace}")
        logicalDiskFreeSpaceTk.set(f"{logicalDiskSize}")
        logicalDiskFreeSpaceTk.set(f"{logicalDiskFreeSpace}")  
        computerSysOwnerEmailTk.set(f"{computerSysOwnerEmail}")
              
        cpuPercentTk.set(f"{cpu_percent(interval=1)}")
        virtualMemoryTk.set(f"{dict(dict(virtual_memory()._asdict()))}")    
        app.update()  # Manually update the GUI
        app.after(100) # Wait for 1 second

#TK VAR
processorNameTk = ctk.StringVar(value = "Loading...") 
processorCoresValueTk = ctk.StringVar(value = "Loading...")
processorThreadsValueTk = ctk.StringVar(value = "Loading...")
osNameValueTk = ctk.StringVar(value = "Loading...")
osUserValueTk = ctk.StringVar(value = "Loading...")
videoControllerNameTk = ctk.StringVar(value = "Loading...")
videoControllerRamTk = ctk.StringVar(value="Loading...")
diskSizeTk = ctk.StringVar(value="Loading...")
logicalDiskNameTk = ctk.StringVar(value="Loading...")
logicalDiskDeviceIdTk = ctk.StringVar(value="Loading...")
logicalDiskFreeSpaceTk = ctk.StringVar(value="Loading...")
logicalDiskSizeTk = ctk.StringVar(value="Loading...")
logicalDiskFreeSpaceTk = ctk.StringVar(value="Loading...")
computerSysOwnerEmailTk = ctk.StringVar(value="Loading...")

cpuPercentTk = ctk.StringVar(value="Loading...") 
virtualMemoryTk = ctk.StringVar(value="Loading...") 

#END TK VAR


#CREATING WIDGETS

processorTitle = ctk.CTkLabel(app, text="Processor: ")
processorTitle.place(x=20,y=10)
processorValue = ctk.CTkLabel(app,width=20, textvariable= processorNameTk,  fg_color="#3F2E3E", corner_radius=6)
processorValue.place(x=100,y=10)

processorCoresTitle = ctk.CTkLabel(app, text="Cores: ")
processorCoresTitle.place(x=20,y = 40)
processorCoresValue = ctk.CTkLabel(app,width=20,textvariable= processorCoresValueTk,  fg_color="#3F2E3E", corner_radius=6)
processorCoresValue.place(x=100,y = 40)

processorThreadsTitle = ctk.CTkLabel(app, text="Threads: ")
processorThreadsTitle.place(x=20,y = 70)
processorThreadsValue = ctk.CTkLabel(app,width=20,textvariable= processorThreadsValueTk,  fg_color="#3F2E3E", corner_radius=6)
processorThreadsValue.place(x=100,y = 70)

osName = ctk.CTkLabel(app, text="OS: ")
osName.place(x=20,y = 90)
osNameValue = ctk.CTkLabel(app,width=20,textvariable= osNameValueTk,  fg_color="#3F2E3E", corner_radius=6)
osNameValue.place(x=100,y = 90)

osUser = ctk.CTkLabel(app, text="OS User: ")
osUser.place(x=20,y = 110)
osUserValue = ctk.CTkLabel(app,width=20,textvariable= osUserValueTk,  fg_color="#3F2E3E", corner_radius=6)
osUserValue.place(x=100,y = 110)

videoControllerName = ctk.CTkLabel(app, text="GPU: ")
videoControllerName.place(x=20,y = 130)
videoControllerNameValue = ctk.CTkLabel(app,width=20,textvariable= videoControllerNameTk,  fg_color="#3F2E3E", corner_radius=6)
videoControllerNameValue.place(x=100,y = 130)

videoControllerRam = ctk.CTkLabel(app, text="GPU vRam: ")
videoControllerRam.place(x=20,y = 150)
videoControllerRamValue = ctk.CTkLabel(app,width=20,textvariable= videoControllerRamTk,  fg_color="#3F2E3E", corner_radius=6)
videoControllerRamValue.place(x=100,y = 150)

diskSize = ctk.CTkLabel(app, text="Disk Size: ")
diskSize.place(x=20,y = 170)
diskSizeValue = ctk.CTkLabel(app,width=20,textvariable= diskSizeTk,  fg_color="#3F2E3E", corner_radius=6)
diskSizeValue.place(x=100,y = 170)

logicalDisk = ctk.CTkLabel(app, text="Current Disk: ")
logicalDisk.place(x=20,y = 190)
logicalDiskValue = ctk.CTkLabel(app,width=20,textvariable= logicalDiskNameTk,  fg_color="#3F2E3E", corner_radius=6)
logicalDiskValue.place(x=100,y = 190)

logicalDiskId = ctk.CTkLabel(app, text="Current ID: ")
logicalDiskId.place(x=20,y = 210)
logicalDiskIdValue = ctk.CTkLabel(app,width=20,textvariable= logicalDiskDeviceIdTk,  fg_color="#3F2E3E", corner_radius=6)
logicalDiskIdValue.place(x=100,y = 210)

logicalDiskFreeSpace = ctk.CTkLabel(app, text="Free Space: ")
logicalDiskFreeSpace.place(x=20,y = 230)
logicalDiskFreeSpaceValue = ctk.CTkLabel(app,width=20,textvariable= logicalDiskFreeSpaceTk,  fg_color="#3F2E3E", corner_radius=6)
logicalDiskFreeSpaceValue.place(x=100,y = 230)

computerSysOwnerEmail = ctk.CTkLabel(app, text="Owner: ")
computerSysOwnerEmail.place(x=20,y = 250)
computerSysOwnerEmailValue = ctk.CTkLabel(app,width=20,textvariable= computerSysOwnerEmailTk,  fg_color="#3F2E3E", corner_radius=6)
computerSysOwnerEmailValue.place(x=100,y = 250)


cpuPercent = ctk.CTkLabel(app, text="CPU USAGE: ")
cpuPercent.place(x=20,y = 280)
cpuPercentValue = ctk.CTkLabel(app,width=20,textvariable= cpuPercentTk,  fg_color="#3F2E3E", corner_radius=6)
cpuPercentValue.place(x=100,y = 280)

virtualMemory = ctk.CTkLabel(app, text="vMemory: ")
virtualMemory.place(x=20,y = 300)
virtualMemoryValue = ctk.CTkLabel(app,width=20,textvariable= virtualMemoryTk,  fg_color="#3F2E3E", corner_radius=6)
virtualMemoryValue.place(x=100,y = 300)


#ENDING CREATING WIDGETS


# Last Settings
if __name__ == "__main__":
    cpu_thread = threading.Thread(target=getCpuValues)
    cpu_thread.daemon = True
    cpu_thread.start()
    #getCpuValues()   
    app.resizable(False,False)
    app.mainloop()


