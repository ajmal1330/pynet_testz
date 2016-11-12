from net_system.models import NetworkDevice
import django

def main():
    django.setup()

    pynet_tst1 = NetworkDevice(
        device_name='pynet-tst1',
        device_type='cisco_ios',
        ip_address='1.1.1.1',
        port=22,
    )
    pynet_tst1.save()

    pynet_tst2 = NetworkDevice.objects.get_or_create(
        device_name='pynet-tst2',
        device_type='cisco_ios',
        ip_address='2.2.2.2',
        port=22,
    )
    pynet_tst2.save()
if __name__ == "__main__":
    main()