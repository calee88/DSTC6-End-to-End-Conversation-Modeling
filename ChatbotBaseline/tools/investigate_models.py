import pickle
import argparse
import numpy as np

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--model', '-m', required=True, help='set prefix of model files')
	args = parser.parse_args()

	with open(args.model + '.1', 'rb') as f0:
		_, model0, _ = pickle.load(f0)
	for name0, _ in model0.namedparams():
		print(name0)
		i = 1
		while True:
			try:
				with open(args.model + '.' + str(i), 'rb') as f:
					_, model, _ = pickle.load(f)
			except FileNotFoundError:
				break
	
			# print(args.model + "." + str(i))

			for name, param in model.namedparams():
				if name == name0:
					array = param.data
					print("mean: " + "{:02.4f}".format(np.mean(array)) + ", max: " + "{:02.4f}".format(np.max(array)) + ", min: " + "{:02.4f}".format(np.min(array)))

			i = i + 1

if __name__ == "__main__":
	main()
