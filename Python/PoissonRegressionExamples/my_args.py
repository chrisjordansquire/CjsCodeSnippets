import argparse
import sys

def parseArgs():
    print " ".join(sys.argv)
    parser = argparse.ArgumentParser() 
    parser.add_argument("--test", action="store_true", default=False)
    parser.add_argument("--exper", action="store_true", default=False)
    parser.add_argument("--reps", action="store", default=0)
    parser.add_argument("--opt", action="store", type=str, default="pure")

    args = parser.parse_args()
    return args

