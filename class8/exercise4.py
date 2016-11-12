from net_system.models import NetworkDevice
import django

def main():
    django.setup()

    #setup the variables for deletion
    device1 = NetworkDevice.objects.get(device_name='pynet-tst1')
    device2 = NetworkDevice.objects.get(device_name='pynet-tst2')

    #This will be used in verification later.  Not needed to delete objects in DB
    all_devices = NetworkDevice.objects.all()

    #delete devices from database
    device1.delete()
    device2.delete()

    #Verify devices are no longer present in database
    print all_devices
if __name__ == "__main__":
    main()