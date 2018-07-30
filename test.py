import argparse
parser = argparse.ArgumentParser()
parser.add_argument("file", help="select the file of the song",
                    type=str)
parser.add_argument("-s", "--start", help="select the section where start the metronome",
                    type=int, default= 1)
parser.add_argument("-e", "--end", help="select the section where the metronome end",
                    type=int, default = 100)

args = parser.parse_args()
print(args.start**2)
print(args.end**2)
