from ioutils import read_ints

if __name__ == "__main__":
    nums = set(read_ints())
    n = len(nums)
    for i in range(1, n+2):
        if i not in nums:
            print('missing number:', i)
            break
