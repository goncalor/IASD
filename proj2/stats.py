
# other modules
import argparse
import statistics

parser = argparse.ArgumentParser(description='Computes stats from output files.')
parser.add_argument('outfile', type=argparse.FileType('r'), nargs='+',
        help='a file in DIMACS format, containing the solution')
args = parser.parse_args()


times = []
solutions_found = 0

print("Reading", len(args.outfile), "solution files")
for f in args.outfile:
    f.readline()
    line = f.readline()

    time_ = float(line.split()[5])
    times.append(time_)

    if line.split()[2] == '1':
        solutions_found += 1

    #print(time_)

print("Found", solutions_found, "satisfied sentences")
print("mean:\t", statistics.mean(times))
print("median:\t", statistics.median(times))
