#dad.py
###Q1
def automatic_histogram(dataset, x):
    """create function automatic_histogram(dataset, x)
        input: dataset (array), x (int) 
        return: dictionary of range (key), count (value)
    """

    if x < 1:
        raise Exception('input x must be greater than 0.')

    sorted_data = sorted(dataset)
    unique_counts = dict()

    #create new dictionary of dataset value:count in dataset pairs
    for data in sorted_data:
        key = data
        if key not in unique_counts:
            unique_counts[key] = count(data, sorted_data)
    #if number of bins greater than or equal to the number of unique values,
    #format accordingly and return
    if x >= len(unique_counts):
        result = {str(k):v for k, v in unique_counts}
        return result
    #else, construct new dictionary with correctly formatted bins and counts
    else:
        result = format_output(unique_counts, x)
        return result


def format_output(u_dict, num_bins):
    """helper function that given a unique value counts dictionary,
    constructs a histogram with num_bins correctly formatted bins.
    """
    result = dict()
    bin_length = len(u_dict) / num_bins
    for i in range(num_bins):
        bin_low = bin_length * i
        bin_high = bin_length * (i + 1)
        new_key = '%d-%d', (bin_low, bin_high)
        result[new_key] = 0
        for j in range(bin_length):
            curr_idx = bin_low + j
            count = u_dict.get(curr_idx)
            result[new_key] += count 

    return result


        

###Q2
def cal_percentile(array, percentile):
    index = len(array) * (percentile / 100)
    upper_idx = ceil(index)
    lower_idx = floor(index)
    value = linear_interpolation(upper_idx, lower_idx, array, percentile)
    return value

def linear_interpolation(upper_idx, lower_idx, array, p):
    l = array[lower_idx]
    p1 = lower_idx - 1 / len(array) * 100
    u = array[upper_idx]
    p2 = lower_idx / len(array) * 100

    return l + (u - l) * ((p - p1) / (p2 - p1))




    
        

    

        






