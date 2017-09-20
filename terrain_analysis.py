from geomutils import POINTS, neighbours

def valsAt(matr, coord_list):
    res = []
    for coord in coord_list:
        l, c = coord
        res += [matr[l][c]]
    return res

def greatestNeighbour(matr, coord):
    coords = neighbours(coord)
    neighs_vals = valsAt(matr, coords)
    return max(neighs_vals)



def nbPeaks(matr):
    nbRow = len(matr)
    nbCol = len(matr[0])
    countPeaks = 0
    for i in range(1,nbRow-1):
        for j in range(1,nbCol-1):
            if matr[i][j] > greatestNeighbour(matr, (i,j)):
                countPeaks += 1
    return countPeaks


if __name__ == "__main__":
    a =[[0,0,0,0],
            [0,1,2,0],
            [0,0,0,3]]
    print(nbPeaks(a))



            
