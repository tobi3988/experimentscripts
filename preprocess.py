import numpy as np


def main():
    # avgowd()
    avgowd_multipath()


def avgowd():
    rawdata = np.genfromtxt('experiments/logs/avgowd/metrics.csv', delimiter=',')
    filtered_data = convert_to_seconds_and_delete_warmup(rawdata)
    np.savetxt("out/avgowd_out.csv", filtered_data[:, [0, 1]], delimiter=",", fmt='%1.3f')


def convert_to_seconds_and_delete_warmup(rawdata):
    end = rawdata[-1, 0]
    start = end - 1200000  # -20min
    rawdata[:, 0] = (rawdata[:, 0] - start) / 1000
    filtered_data = rawdata[rawdata[:, 0] > 0]
    return filtered_data


def avgowd_multipath():
    rawdata = np.genfromtxt('experiments/logs/avgowd/multipath.csv', delimiter=',')
    filtered_data = convert_to_seconds_and_delete_warmup(rawdata)
    np.savetxt("out/avgowd_multipath_out.csv", filtered_data[:, [0, 1]], delimiter=",", fmt='%1.3f')


if __name__ == '__main__':
    main()
