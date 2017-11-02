import argparse
from Queue import Queue


def josephus(nb_people, nth_kill):
    who_to_kill = Queue()
    def kill(queue, n):
        person = queue.dequeue()
        if n == 1:
            who_to_kill.enqueue(person)
            return
        else:
            queue.enqueue(person)
            kill(queue, n - 1)

    q = Queue()
    for i in range(nb_people):
        q.enqueue(i)
    while q:
        kill(q, nth_kill)
    return who_to_kill



def main():
    parser = argparse.ArgumentParser(description='Solve the Josephus problem')
    parser.add_argument('nb_people', type=int, help='number of people')
    parser.add_argument('nth', type=int, help='nth person to kill')
    args = parser.parse_args()
    nb_people = args.nb_people
    nth = args.nth
    print(josephus(nb_people, nth))


if __name__ == '__main__':
    main()
