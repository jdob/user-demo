import random
import re
import subprocess

from flask import Flask

app = Flask(__name__)


@app.route('/')
def root():
    # Retrieve user info
    # Ex: uid=1000(jdob) gid=1000(jdob) groups=1000(jdob),10(wheel),973(pkg-build),981(libvirt) context=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023
    out = subprocess.Popen(['id'],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT)
    stdout, stderr = out.communicate()

    # Parse apart what we care about
    x = stdout.split()

    username = extract_name(str(x[0]))
    uid = extract_uid(str(x[0]))

    groupname = extract_name(str(x[1]))
    gid = extract_gid(str(x[1]))

    return {'username': username,
            'uid': uid,
            'groupname': groupname,
            'gid': gid
            }


@app.route('/write')
def write():
    # Writes a file with a random name to root
    filename = str(random.randrange(1000, 9999))
    with open(filename, 'w') as f:
        f.write('user demo test')
    return {'filename': filename}


def extract_name(x):
    return re.search(r'(\(.*?\))', x).group(0)[1:-1]


def extract_uid(x):
    return re.search(r'uid=(.*?)\(', x).group(1)


def extract_gid(x):
    return re.search(r'gid=(.*?)\(', x).group(1)
