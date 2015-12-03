#!/usr/bin/env python
'''
Description:
    Scans hardware and pairs any bluetooth device that is found.

Usage:
    pair [options]

Options:
    -h --help            This message
    -l --list            Lists available devices
    -d --debug           Run with debug on
    -R --remove-all      Removes all current devices
    -D --disconnect-all  Disconnects all connected devices
'''
from __future__ import print_function

import logging
import subprocess
import re


log = logging.getLogger('bluetooth_pairing')


def run(cmd):
    '''Runs a command intelligently'''
    log.debug('Running:{cmd}'.format(cmd=cmd))
    proc = subprocess.Popen(
        cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    if stderr.strip():
        for err in stderr.split('\n'):
            log.error(err)
    for line in stdout.split('\n'):
        log.debug(line)
    return stdout

def scan_for_devices():
    '''Returns a list of devices'''
    devices = []
    cmd = 'hcitool scan'
    log.debug('Starting scanning...')
    raw_result = run(cmd)
    pattern = r'^\s+(?P<mac>(([0-9A-Za-z]{2}\:?){6}))\s+(?P<desc>(.*))$'
    matcher = re.compile(pattern)
    for line in raw_result.split('\n'):
        matched = matcher.search(line)
        if matched:
            data = matched.groupdict()
            mac, desc = data.get('mac'), data.get('desc')
            log.debug('Found: mac={mac}, desc={desc}'.format(mac=mac, desc=desc))
            devices.append((mac, desc))
    devices = {k: v for k, v in devices}
    if not devices:
        log.warn('No devices found to pair.')
    return devices

def list_known_devices():
    '''Finds all the known bluetooth deviecs'''
    cmd = 'sudo bluez-test-device list'
    raw_result = run(cmd)
    devices = {
        line.split(' ', 1)[0]: line.split(' ', 1)[-1]
        for line in run(cmd).split('\n')
    }
    return devices

def remove_known_devices():
    '''Drops all bluetooth devices which have been paired at some point'''
    for mac, desc in list_known_devices().items():
        remove_device(mac)

def create_device(mac):
    '''Creates the devices'''
    cmd = 'sudo bluez-simple-agent hci0 {mac}'.format(mac=mac)
    raw_result = run(cmd)
    if raw_result.strip().endswith('Already Exists'):
        remove_device(mac)
        create_device(mac)

def trust_device(mac):
    '''Tells bluetooth to trust the device'''
    cmd = 'sudo bluez-test-device trusted {mac} yes'.format(mac=mac)
    raw_result = run(cmd)

def connect_device(mac):
    '''Connects to bluetooth device'''
    cmd = 'sudo bluez-test-input connect {mac}'.format(mac=mac)
    raw_result = run(cmd)

def disconnect_device(mac):
    '''Disconnects to bluetooth device'''
    cmd = 'sudo bluez-test-input disconnect {mac}'.format(mac=mac)
    raw_result = run(cmd)

def remove_device(mac):
    '''Removes a bluetooth device'''
    cmd = 'sudo bluez-test-device remove {mac}'.format(mac=mac)
    raw_result = run(cmd)

def main(**options):
    '''Pairs all devices found'''
    if options.get('remove-all'):
        remove_known_devices()
    for mac, desc in scan_for_devices().items():
        log.info('Pairing: "{desc}" using address: "{mac}"'.format(desc=desc, mac=mac))
        create_device(mac)
        trust_device(mac)
        connect_device(mac)
        log.info(' Paired: "{desc}" using address: "{mac}"'.format(desc=desc, mac=mac))


if __name__ == '__main__':
    from docopt import docopt

    options = {k.lstrip('--'): v for k, v in docopt(__doc__).items()}
    if not options.get('debug'):
        logging.basicConfig(level=logging.INFO)
    else:
        logging.basicConfig(level=logging.DEBUG)

    main(**options)
