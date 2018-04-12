import numpy as np


def main():
    rawdata = np.genfromtxt('experiments/logs/avgowd/metrics.csv', delimiter=',')
    print(rawdata)
    end = rawdata[-1, 0]
    print(end)
    start = end - 1200000  # -20min
    print(start)
    print(len(rawdata))
    rawdata[:, 0] = (rawdata[:, 0] - start) / 1000
    print(rawdata[:, 0])
    filtered_data = rawdata[rawdata[:, 0] > 0]
    print(filtered_data)
    np.savetxt("out/avgowd_out.csv", filtered_data[:, [0, 1]], delimiter=",",fmt='%1.3f')


if __name__ == '__main__':
    main()
