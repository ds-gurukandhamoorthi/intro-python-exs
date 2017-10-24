import os
import argparse
from Sketch import Sketch


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Compare documents')
    parser.add_argument('k', type=int, help='k as in kgrams')
    parser.add_argument('d', type=int, help='dimension : how fine-grained is your reality?')
    parser.add_argument('files', nargs='+', help='files to compare')
    args = parser.parse_args()
    k = args.k
    d = args.d
    files = args.files

    print('    ', end=' ')
    for f2 in files:
        fn = os.path.splitext(f2)[0]
        fn = os.path.basename(fn)
        print(fn[:4], end=' ')
    print()
    for f1 in files:
        fn = os.path.splitext(f1)[0]
        fn = os.path.basename(fn)
        print(fn[:4], end=' ')
        with open(f1) as f1_:
            txt1 = f1_.read()
            for f2 in files:
                with open(f2) as f2_:
                    txt2 = f2_.read()
                    sim = Sketch(txt1, k, d).similar_to(Sketch(txt2, k, d))
                    print('%3.2f' % sim, end=' ')
            print()
