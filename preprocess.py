import numpy as np


def main():
    # avgowd()
    # avgowd_multipath()
    # avgowd_var()
    # avgowd_multipath_var()
    loss()
    loss_multipath()


def avgowd():
    rawdata = np.genfromtxt('experiments/logs/avgowd/metrics.csv', delimiter=',')
    filtered_data = convert_to_seconds_and_delete_warmup(rawdata)
    np.savetxt("out/avgowd_out.csv", filtered_data[:, [0, 1]], delimiter=",", fmt='%1.3f')


def convert_to_seconds_and_delete_warmup(rawdata, networkdata=None):
    end = rawdata[-1, 0]
    start = end - 1200000  # -20min
    rawdata[:, 0] = (rawdata[:, 0] - start) / 1000
    filtered_data = rawdata[rawdata[:, 0] > 0]
    number_of_dimensions = len(filtered_data[0])
    extended_data = np.zeros((len(filtered_data), number_of_dimensions + 1))
    extended_data[:, :-1] = filtered_data
    if networkdata is not None:
        networkdata[:, 0] = (networkdata[:, 0] - start) / 1000
        for element in extended_data:
            settings = networkdata[0, 1]
            for network in networkdata:
                if network[0] > element[0]:
                    break
                settings = network[1]
            element[number_of_dimensions] = settings
    return extended_data


def avgowd_multipath():
    rawdata = np.genfromtxt('experiments/logs/avgowd/multipath.csv', delimiter=',')
    filtered_data = convert_to_seconds_and_delete_warmup(rawdata)
    np.savetxt("out/avgowd_multipath_out.csv", filtered_data[:, [0, 1]], delimiter=",", fmt='%1.3f')


def avgowd_var():
    rawdata = np.genfromtxt('experiments/logs/avg_owd_var/metrics.csv', delimiter=',')
    network_data = np.genfromtxt('experiments/logs/avg_owd_var/network.csv', delimiter=',')
    filtered_data = convert_to_seconds_and_delete_warmup(rawdata, networkdata=network_data)
    np.savetxt("out/avgowd_var_out.csv", filtered_data[:, [0, 1, 9]], delimiter=",", fmt='%1.3f')


def avgowd_multipath_var():
    rawdata = np.genfromtxt('experiments/logs/avg_owd_var/multipath.csv', delimiter=',')
    network_data = np.genfromtxt('experiments/logs/avg_owd_var/network2.csv', delimiter=',')
    filtered_data = convert_to_seconds_and_delete_warmup(rawdata, networkdata=network_data)
    filtered_data[:, 5] = filtered_data[:, 5] * 3
    np.savetxt("out/avgowd_multipath_var_out.csv", filtered_data[:, [0, 1, 5]], delimiter=",", fmt='%1.3f')


def loss():
    rawdata = np.genfromtxt('experiments/logs/loss/metrics.csv', delimiter=',')
    filtered_data = convert_to_seconds_and_delete_warmup(rawdata)
    filtered_data[:, 5] = filtered_data[:, 5] * 100
    print('mean of measured loss: %s' % str(np.mean(filtered_data[:, 5])))
    print('std of measured loss: %s' % str(np.std(filtered_data[:, 5])))
    np.savetxt("out/loss_out.csv", filtered_data[:, [0, 5]], delimiter=",", fmt='%1.4f')


def loss_multipath():
    rawdata = np.genfromtxt('experiments/logs/loss/multipath.csv', delimiter=',')
    filtered_data = convert_to_seconds_and_delete_warmup(rawdata)
    filtered_data[:, 3] = filtered_data[:, 3] * 100
    print('mean of measured loss multipath: %s' % str(np.mean(filtered_data[:, 3])))
    print('std of measured loss multipath: %s' % str(np.std(filtered_data[:, 3])))
    np.savetxt("out/loss_multipath_out.csv", filtered_data[:, [0, 3]], delimiter=",", fmt='%1.4f')


if __name__ == '__main__':
    main()
