from ioutils import read_floats
from mathutils import geom_mean, harm_mean

if __name__ == "__main__":
    nums = read_floats()
    print(geom_mean(nums))
    print(harm_mean(nums))

