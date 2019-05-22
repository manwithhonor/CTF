import os
from .vendor.ziptools import ziptools
from .models import Host, Record


def save_zip_to_hosting(zip_path, out_path):
    zip_path = os.path.abspath(zip_path)

    good = True

    try:
        os.mkdir(out_path)
    except FileExistsError:
        good = False

    if good:
        try:
            ziptools.extractzipfile(zip_path, out_path, maxsize=100 * 1024)
        except Exception as e:
            good = False
        finally:
            os.remove(zip_path)

    return good


def save_new_hosting_item(domain, username, password, directory, my_ip):
    # Save hosting data
    Host(domain=domain,
         username=username,
         password=password,
         directory=directory
         ).save()

    # Create DNS record
    Record(rname=domain,
           rtype="A",
           rdata=[my_ip]
           ).save()
    Record(rname='.'.join(my_ip.split('.')[::-1]) + '.in-addr.arpa.',
           rtype="PTR",
           rdata=[domain]
           ).save()
