suffixes = {1000: ['KB', 'MB', 'GB', 'TB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB']}


def approximate_size(size, a_kilobyte_is_1024_byte=True):
    if size < 0:
        raise ValueError("Number must be non-negative!")

    multiple = 1024 if a_kilobyte_is_1024_byte else 1000

    for suffix in suffixes[multiple]:
        size /= multiple

        if size < multiple:
            return "{0:.1f} {1}".format(size, suffix)

    raise ValueError("Number is too large")


print(approximate_size(1000000000000, False))
print(approximate_size(1000000000000))