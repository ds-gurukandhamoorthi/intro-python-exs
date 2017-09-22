#!/usr/bin/env python3
import argparse
import random

def diff(array, without):
    return [x for x in array if x not in without]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='random pair of integers')
    parser.add_argument('nb_pages', type=int, help='number of pages')
    parser.add_argument('nb_links', type=int, help='number of links')
    parser.add_argument('--hubs', type=int, help='number of hubs')
    parser.add_argument('--authorities', type=int, help='number of authorities')
    PRCT = 10
    args = parser.parse_args()
    nb_pages = args.nb_pages
    nb_links = args.nb_links
    nb_hubs  = args.hubs
    nb_authorities = args.authorities
    
    NB_PAGES_LINK_HUB = int(nb_pages * PRCT /100)
    NB_PAGES_LINK_AUTH = int(nb_pages * PRCT /100)
    PAGES = range(0,nb_pages)
    print(nb_pages)
    if nb_hubs:
        HUBS  = random.sample(PAGES, nb_hubs)
        for hub in HUBS:
            to_pages = random.sample(diff(PAGES,[hub]) , NB_PAGES_LINK_HUB)
            for pg in to_pages:
                print(pg, hub, end='  ')
            print('')
    if nb_authorities:
        AUTHORITIES  = random.sample(PAGES, nb_authorities)
        for auth in AUTHORITIES:
            to_pages = random.sample(diff(PAGES,[auth]) , NB_PAGES_LINK_AUTH)
            for pg in to_pages:
                print(auth, pg, end='  ')
            print('')
    for i in range(nb_links):
        print(*random.sample(PAGES,2))

