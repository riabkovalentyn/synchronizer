import argparse

def parse():
    parser = argparse.ArgumentParser(description='File synchronization')
    parser.add_argument("source", type=str, help = "File source")
    parser.add_argument("replica", type= str, help='File replica')
    parser.add_argument("interval", type= str,  help='Timeout interval')
    parser.add_argument("log", type=str, help='Log file')

    return parser.parse_args()