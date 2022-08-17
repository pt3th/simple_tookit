import argparse
from distutils.util import strtobool

parser = argparse.ArgumentParser(description='PyTorch Cifar Training')
parser.add_argument('--seed', default=0, type=int, help='seed for initializing training. ')
parser.add_argument('--object', default='traffic_light', type=str, help='base model object')
parser.add_argument('--epsilon', default=8/255, type=float, help='attack epsilon')

'''
Parse Boolean Values With Argparse in Python
'''
parser.add_argument('--patch', default=False, type=lambda x:bool(strtobool(x)), help='bool: use patch dataset')

args = parser.parse_args()

config['seed'] = seed

#...

