import platform
import subprocess
from urllib.parse import urlsplit

links = ['https://buaya.klas.or.id/ubuntu/', 'http://mirror.biznetgio.com/ubuntu/', 'https://mirror.nevacloud.com/ubuntu/ubuntu-archive/', 'http://mirror.deace.id/ubuntu/', 'http://mirror.beon.co.id/ubuntu/', 'https://repo.usk.ac.id/ubuntu/', 'https://mirror.faizuladib.com/ubuntu/', 'http://kartolo.sby.datautama.net.id/ubuntu/', 'https://mirror-gw.elastis.id/ubuntu/', 'http://mirror.unej.ac.id/ubuntu/', 'http://mirror.cloudxchange.id/ubuntu/', 'https://mirror.repository.id/ubuntu/', 'http://mirror.cepatcloud.id/ubuntu/', 'https://mirror.unair.ac.id/ubuntu/', 'http://mirror.citraix.net/ubuntu/', 'https://linux.domainesia.com/ubuntu/ubuntu-archive/', 'http://kebo.pens.ac.id/ubuntu/', 'https://mr.heru.id/ubuntu/', 'https://mirror.amscloud.co.id/ubuntu/', 'http://mirror.labkom.id/ubuntu/', 'http://mirror.telkomuniversity.ac.id/ubuntu/', 'http://suro.ubaya.ac.id/ubuntu/', 'http://mirror.poliwangi.ac.id/ubuntu/', 'http://archive.ubuntu.com/ubuntu/']

def ping(host):
    param = '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', param, '1', host]
    return subprocess.call(command) == 0

for link in links:
    print(ping(urlsplit(link).netloc))
