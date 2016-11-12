from net_system.models import NetworkDevice
import django

def main():
    device1 = NetworkDevice.objects.get(device_name='pynet-tst1')
    device2 = NetworkDevice.objects.get(device_name='pynet-tst2')
    all_devices = NetworkDevice.objects.all()
    device1.delete()
    device2.delete()
    print all_devices
if __name__ == "__main__":
    main()