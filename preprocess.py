import numpy as np


def main():
    # avgowd()
    # avgowd_multipath()
    # avgowd_var()
    # avgowd_multipath_var()
    # loss()
    # loss_multipath()
    # loss_var()
    # loss_multipath_var()
    # reordering()
    # reordering_multipath()
    # reordering_var()
    # reordering_multipath_var()
    # percentile()
    # percentile_var()
    # percentile_multipath()
    # percentile_multipath_var()
    overhead()


def avgowd():
    rawdata = np.genfromtxt('experiments/logs/avgowd/metrics.csv', delimiter=',')
    filtered_data = convert_to_seconds_and_delete_warmup(rawdata)
    np.savetxt("out-dir/avgowd_out.csv", filtered_data[:, [0, 1]], delimiter=",", fmt='%1.3f')


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
    np.savetxt("out-dir/avgowd_multipath_out.csv", filtered_data[:, [0, 1]], delimiter=",", fmt='%1.3f')


def avgowd_var():
    rawdata = np.genfromtxt('experiments/logs/avg_owd_var/metrics.csv', delimiter=',')
    network_data = np.genfromtxt('experiments/logs/avg_owd_var/network.csv', delimiter=',')
    filtered_data = convert_to_seconds_and_delete_warmup(rawdata, networkdata=network_data)
    np.savetxt("out-dir/avgowd_var_out.csv", filtered_data[:, [0, 1, 9]], delimiter=",", fmt='%1.3f')


def avgowd_multipath_var():
    rawdata = np.genfromtxt('experiments/logs/avg_owd_var/multipath.csv', delimiter=',')
    network_data = np.genfromtxt('experiments/logs/avg_owd_var/network2.csv', delimiter=',')
    filtered_data = convert_to_seconds_and_delete_warmup(rawdata, networkdata=network_data)
    filtered_data[:, 5] = filtered_data[:, 5] * 3
    np.savetxt("out-dir/avgowd_multipath_var_out.csv", filtered_data[:, [0, 1, 5]], delimiter=",", fmt='%1.3f')


def loss():
    rawdata = np.genfromtxt('experiments/logs/loss/metrics.csv', delimiter=',')
    filtered_data = convert_to_seconds_and_delete_warmup(rawdata)
    filtered_data[:, 5] = filtered_data[:, 5] * 100
    print('mean of measured loss: %s' % str(np.mean(filtered_data[:, 5])))
    print('std of measured loss: %s' % str(np.std(filtered_data[:, 5])))
    np.savetxt("out-dir/loss_out.csv", filtered_data[:, [0, 5]], delimiter=",", fmt='%1.4f')


def loss_multipath():
    rawdata = np.genfromtxt('experiments/logs/loss/multipath.csv', delimiter=',')
    filtered_data = convert_to_seconds_and_delete_warmup(rawdata)
    filtered_data[:, 3] = filtered_data[:, 3] * 100
    print('mean of measured loss multipath: %s' % str(np.mean(filtered_data[:, 3])))
    print('std of measured loss multipath: %s' % str(np.std(filtered_data[:, 3])))
    np.savetxt("out-dir/loss_multipath_out.csv", filtered_data[:, [0, 3]], delimiter=",", fmt='%1.4f')


def loss_var():
    rawdata = np.genfromtxt('experiments/logs/packet_loss_var/metrics.csv', delimiter=',')
    network_data = np.genfromtxt('experiments/logs/packet_loss_var/network.csv', delimiter=',')
    filtered_data = convert_to_seconds_and_delete_warmup(rawdata, networkdata=network_data)
    filtered_data[:, 5] = filtered_data[:, 5] * 100
    filtered_data[:, 9] = (1 - (1 - filtered_data[:, 9] / 100) ** 3) * 100
    print('mean of measured loss var: %s' % str(np.mean(filtered_data[:, 5])))
    print('std of measured loss var: %s' % str(np.std(filtered_data[:, 5])))
    np.savetxt("out-dir/loss_var_out.csv", filtered_data[:, [0, 5, 9]], delimiter=",", fmt='%1.3f')


def loss_multipath_var():
    rawdata = np.genfromtxt('experiments/logs/packet_loss_var/multipath.csv', delimiter=',')
    network_data = np.genfromtxt('experiments/logs/packet_loss_var/network.csv', delimiter=',')
    filtered_data = convert_to_seconds_and_delete_warmup(rawdata, networkdata=network_data)
    filtered_data[:, 3] = filtered_data[:, 3] * 100
    filtered_data[:, 5] = (1 - (1 - filtered_data[:, 5] / 100) ** 9) * 100
    print('mean of measured loss multipath var: %s' % str(np.mean(filtered_data[:, 3])))
    print('std of measured loss multipath var: %s' % str(np.std(filtered_data[:, 3])))
    np.savetxt("out-dir/loss_multipath_var_out.csv", filtered_data[:, [0, 3, 5]], delimiter=",", fmt='%1.3f')


def reordering():
    rawdata = np.genfromtxt('experiments/logs/reordering/metrics.csv', delimiter=',')
    filtered_data = convert_to_seconds_and_delete_warmup(rawdata)
    filtered_data[:, 6] = filtered_data[:, 6] * 100
    print('mean of measured reordering: %s' % str(np.mean(filtered_data[:, 6])))
    print('std of measured reordering: %s' % str(np.std(filtered_data[:, 6])))
    np.savetxt("out-dir/reordering_out.csv", filtered_data[:, [0, 6]], delimiter=",", fmt='%1.3f')


def reordering_multipath():
    rawdata = np.genfromtxt('experiments/logs/reordering/multipath.csv', delimiter=',')
    filtered_data = convert_to_seconds_and_delete_warmup(rawdata)
    filtered_data[:, 4] = filtered_data[:, 4] * 100
    print('mean of measured reordering multipath: %s' % str(np.mean(filtered_data[:, 4])))
    print('std of measured reordering multipath: %s' % str(np.std(filtered_data[:, 4])))
    np.savetxt("out-dir/reordering_multipath_out.csv", filtered_data[:, [0, 4]], delimiter=",", fmt='%1.3f')


def reordering_var():
    rawdata = np.genfromtxt('experiments/logs/pkt_reord_var/metrics.csv', delimiter=',')
    network_data = np.genfromtxt('experiments/logs/pkt_reord_var/network.csv', delimiter=',')
    filtered_data = convert_to_seconds_and_delete_warmup(rawdata, networkdata=network_data)
    filtered_data[:, 6] = filtered_data[:, 6] * 100
    filtered_data[:, 9] = (1 - (1 - filtered_data[:, 9] / 100) ** 3) * 100
    print('mean of measured reordering var: %s' % str(np.mean(filtered_data[:, 6])))
    print('std of measured reordering var: %s' % str(np.std(filtered_data[:, 6])))
    np.savetxt("out-dir/reordering_var_out.csv", filtered_data[:, [0, 6, 9]], delimiter=",", fmt='%1.3f')


def reordering_multipath_var():
    rawdata = np.genfromtxt('experiments/logs/pkt_reord_var/multipath.csv', delimiter=',')
    network_data = np.genfromtxt('experiments/logs/pkt_reord_var/network.csv', delimiter=',')
    filtered_data = convert_to_seconds_and_delete_warmup(rawdata, networkdata=network_data)
    filtered_data[:, 4] = filtered_data[:, 4] * 100
    filtered_data[:, 5] = (1 - (1 - filtered_data[:, 5] / 100) ** 9) * 100
    print('mean of measured reordering multipath var: %s' % str(np.mean(filtered_data[:, 4])))
    print('std of measured reordering multipath var: %s' % str(np.std(filtered_data[:, 4])))
    np.savetxt("out-dir/reordering_multipath_var_out.csv", filtered_data[:, [0, 4, 5]], delimiter=",", fmt='%1.3f')


def percentile():
    rawdata = np.genfromtxt('experiments/logs/variation/metrics.csv', delimiter=',')
    filtered_data = convert_to_seconds_and_delete_warmup(rawdata)
    print('mean of measured percentile: %s' % str(np.mean(filtered_data[:, 4])))
    print('std of measured percentile: %s' % str(np.std(filtered_data[:, 4])))
    np.savetxt("out-dir/percentile_out.csv", filtered_data[:, [0, 4]], delimiter=",", fmt='%1.3f')


def percentile_multipath():
    rawdata = np.genfromtxt('experiments/logs/variation/multipath.csv', delimiter=',')
    filtered_data = convert_to_seconds_and_delete_warmup(rawdata)
    filtered_data[:, 2] = filtered_data[:, 2]
    print('mean of measured percentile multipath: %s' % str(np.mean(filtered_data[:, 2])))
    print('std of measured percentile multipath: %s' % str(np.std(filtered_data[:, 2])))
    np.savetxt("out-dir/percentile_multipath_out.csv", filtered_data[:, [0, 2]], delimiter=",", fmt='%1.3f')


def percentile_var():
    rawdata = np.genfromtxt('experiments/logs/variation_var/metrics.csv', delimiter=',')
    network_data = np.genfromtxt('experiments/logs/variation_var/network.csv', delimiter=',')
    filtered_data = convert_to_seconds_and_delete_warmup(rawdata, networkdata=network_data)
    filtered_data[:, 4] = filtered_data[:, 4]
    filtered_data[:, 9] = filtered_data[:, 9] * 6
    print('mean of measured percentile var: %s' % str(np.mean(filtered_data[:, 4])))
    print('std of measured percentile var: %s' % str(np.std(filtered_data[:, 4])))
    np.savetxt("out-dir/percentile_var_out.csv", filtered_data[:, [0, 4, 9]], delimiter=",", fmt='%1.3f')


def percentile_multipath_var():
    rawdata = np.genfromtxt('experiments/logs/variation_var/multipath.csv', delimiter=',')
    network_data = np.genfromtxt('experiments/logs/variation_var/network.csv', delimiter=',')
    filtered_data = convert_to_seconds_and_delete_warmup(rawdata, networkdata=network_data)
    filtered_data[:, 2] = filtered_data[:, 2]
    filtered_data[:, 5] = filtered_data[:, 5] * 6
    print('mean of measured percentile multipath var: %s' % str(np.mean(filtered_data[:, 2])))
    print('std of measured percentile multipath var: %s' % str(np.std(filtered_data[:, 2])))
    np.savetxt("out-dir/percentile_multipath_var_out.csv", filtered_data[:, [0, 2, 5]], delimiter=",", fmt='%1.3f')


def overhead():
    handle_data_base = np.genfromtxt('experiments/logs/overhead/overhead_handle.csv', delimiter=',')
    propagate_data_base = np.genfromtxt('experiments/logs/overhead/overhead_propagate.csv', delimiter=',')
    handle_data = np.genfromtxt('experiments/logs/overhead-old/overhead_handle.csv', delimiter=',')
    propagate_data = np.genfromtxt('experiments/logs/overhead-old/overhead_propagate.csv', delimiter=',')
    print('handel base mean: %s' % str(np.mean(handle_data_base)))
    print('propagate base mean: %s' % str(np.mean(propagate_data_base)))
    print('handel mean: %s' % str(np.mean(handle_data)))
    print('propagate mean: %s' % str(np.mean(propagate_data)))
    print('handel base std: %s' % str(np.std(handle_data_base)))
    print('propagate base std: %s' % str(np.std(propagate_data_base)))
    print('handel std: %s' % str(np.std(handle_data)))
    print('propagate std: %s' % str(np.std(propagate_data)))


if __name__ == '__main__':
    main()
