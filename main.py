import wmi
import psutil


def print_hi(name):
    ti = 0
    p_names = ['TiWorker.exe', 'SearchIndexer.exe', 'CompatTelRunner.exe', 'svchost.exe']
    f = wmi.WMI()
    for process in f.Win32_Process():
        if process.name in p_names:
            process.Terminate()
            print(f"P with name {process.name} is closed")
            ti += 1
    if ti == 0:
        print("Process not found!!!")


if __name__ == '__main__':
    print('The CPU usage is: ', psutil.cpu_percent(5))
    print_hi('PyCharm')
