#!/usr/bin/python

import os, sys
from subprocess import check_output, check_call
import usage

def main():
    usage.check_args(sys.argv, os.path.basename(__file__), usage.RECV_FIRST)
    option = sys.argv[1]
    src_dir = os.path.abspath(os.path.dirname(__file__))
    find_unused_port_file = os.path.join(src_dir, 'find_unused_port')
    src_file = 'iperf'

    # build dependencies
    if option == 'deps':
        print 'iperf'

    # build commands
    if option == 'build':
        pass

    # commands to be run after building and before running
    if option == 'initialize':
        pass

    # who goes first
    if option == 'who_goes_first':
        print 'Receiver first'

    # receiver
    if option == 'receiver':
        port = check_output([find_unused_port_file])
        sys.stderr.write('Listening on port: %s\n' % port)
        cmd = [src_file, '-s', '-p', port]
        check_call(cmd)

    # sender
    if option == 'sender':
        ip = sys.argv[2]
        port = sys.argv[3]
        cmd = [src_file, '-c', ip, '-p', port, '-t', '75']
        check_call(cmd)

if __name__ == '__main__':
    main()
