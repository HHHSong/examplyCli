#!/usr/bin/env python3
# encoding: utf-8

import argparse
import grpc
import sys
import prettytable
import json
import textwrap


def _poolCli(mainSub):
    pass


def _volCli(mainSub):
    pass


def _help(args):
    print('Please input -h to help.')


def poolRun():
    pass


def volRun():
    pass


_opTargetList = {
    'pool': poolRun,
    'vol': volRun,
    None: _help,
}


def run(args):
    _opTargetList[args.opTarget](args)


def _cli():
    print("examply Cli")
    mainParser = argparse.ArgumentParser(description='examply Cli')
    mainParser.add_argument('--host-ip', type=str, action='store', dest='host_ip', default='127.0.0.1',
                            help='The host you want run command, default is 127.0.0.1')
    mainSub = mainParser.add_subparsers(title='opreation target', dest='opTarget')

    # pool cli
    _poolCli(mainSub)
    # vol cli
    _volCli(mainSub)

    try:
        args = mainParser.parse_args()
        run(args)
    except IOError as msg:
        mainParser.error(str(msg))

def Cli():
    if __name__ == "__main__":
        _cli()
