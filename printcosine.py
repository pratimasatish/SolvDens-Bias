import numpy as np
import matplotlib.pyplot as plt
import argparse

# parser = argparse.ArgumentParser(description="")
# parser.add_argument("-bias", type=float, default=2500.0, help="bias value for spring constant")
# parser.add_argument("-at_lower", type=float, default=-0.75, help="lower limit of order parameter in biased simulation")
# parser.add_argument("-at_upper", type=float, default=-0.73, help="upper limit of order parameter in biased simulation")
# parser.add_argument("-at_step", type=float, default=0.01, help="step between each consecutive umbrella")
# parser.add_argument("-timestep", type=int, default=5000, help="timesteps after which umbrella is moved")
# args   = parser.parse_args()

# at_range = np.arange(args.at_lower, args.at_upper+args.at_step, args.at_step)
str_out = ""
str_out = str_out + "UNITS ENERGY=kcal/mol\n"
count = 1
sigma = 20.0
prefac = 1/np.sqrt(2 * np.pi * sigma * sigma)
denom = 2 * sigma * sigma
centre = 20.0

for i in range(1, 3001, 1):
    str_out = str_out + "p{}: POSITION ATOM={}\n".format(count, i)
    count = count + 1

for i in range(1, count):
    str_out = str_out + "\nMATHEVAL ...\n"
    str_out = str_out + "LABEL=exp{}\nARG=p{}.y".format(i, i)
    str_out = str_out + "\nFUNC=exp(-(x-{})*(x-{})/{})\n".format(centre, centre, denom)
    str_out = str_out + "PERIODIC=NO\n"
    str_out = str_out + "... MATHEVAL\n"

str_out = str_out + "\ntotexp: COMBINE ARG="

for i in range(1, count):
    str_out = str_out + "exp{},".format(i)
str_out = str_out.rstrip(",")

str_out = str_out + " COEFFICIENTS="

for i in range(1, count):
    str_out = str_out + "{},".format(prefac)
str_out = str_out.rstrip(",")

str_out = str_out + " PERIODIC=NO"

# str_out = str_out + "\n\nMOVINGRESTRAINT ...\n"
# str_out = str_out + "  ARG=avgtheta\n"
# for i in range(len(at_range)):
#     str_out = str_out + "  STEP{}={} AT{}={} KAPPA{}={}\n".format(i, i*args.timestep, i, at_range[i], i, args.bias)
# str_out = str_out + "... MOVINGRESTRAINT\n"

# str_out = str_out + "\nPRINT ARG="
# for i in range(1, count):
#     str_out = str_out + "theta{},".format(i)
# str_out = str_out + ",avgtheta STRIDE=10\n"

str_out = str_out + "\n\nRESTRAINT ARG=totexp AT=0.0 KAPPA=2000.0\n"

str_out = str_out + "\nPRINT ARG=totexp,exp1,exp100,exp1000,exp2000 STRIDE=10\n"
str_out = str_out.rstrip(",")

print str_out
