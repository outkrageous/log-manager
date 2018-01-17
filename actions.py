#!/usr/bin/python

from logmanager import logOperations
import sys

def main():
    instances()

def instances():
    logops = logOperations()

    logops.printlogsize()

if __name__ == "__main__":
    main()

