import socket
import sys
import time
from threading import Thread
import tqdm


def scan_port(ip, port, opened_ports):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((ip, port))
        if result == 0:
            opened_ports.append(port)
            s.close()
    except:
        pass


def print_header(target):
    print('\n' + '-' * 50)
    print("Target:", target)
    print('-' * 50 + '\n')


if len(sys.argv) == 2:
    try:
        target = socket.gethostbyname(sys.argv[1])
    except Exception:
        print('\nPlease type your ip target correctly.\n')
        sys.exit(0)
else:
    print("Invalid systax. Use python3 port_scan.py <ip address>")
    sys.exit(0)

# print header
print_header(target)
opened_port = []
start = time.time()

# start scanning
# create progress bar to display status
for i in tqdm.tqdm(range(10000)):
    th = Thread(target=scan_port, args=(target, i, opened_port))
    th.daemon = True
    th.start()

# report result
end = time.time()
cost_time = end - start
print(f"\nThe scan took {round(cost_time, 2)} seconds.")
print(f'Total {len(opened_port)} opened ports in [1, 9999].\n')
if opened_port:
    print(opened_port)
