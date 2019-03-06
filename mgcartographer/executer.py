import argparse
from mgcartographer.cartographer import *


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("link", help="srv link to your MongoDB Atlas Cluster",
                        type=str)
    parser.add_argument("database", help="path to your local database directory",
                        type=str)
    args = parser.parse_args()
    cartographer = MongoCartographer(args.link)
    cartographer.push(os.path.join(args.database))

if __name__ == '__main__':
    	main()
