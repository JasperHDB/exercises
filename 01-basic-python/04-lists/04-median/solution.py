def median(ns):
    ns = sorted(ns)     # Sort ns
    i = len(ns) // 2    # Divide the length of ns by 2

    if len(ns) % 2 == 0:    # Check if ns is even or uneven
        return (ns[i - 1] + ns[i]) / 2  # If even, add the element of i - 1 with i, and divide by 2
    else:
        return ns[i]    # If uneven, print the element with index i