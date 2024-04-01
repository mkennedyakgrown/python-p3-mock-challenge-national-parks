#!/usr/bin/env python3
import ipdb

from classes.many_to_many import NationalPark
from classes.many_to_many import Visitor
from classes.many_to_many import Trip

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    park = NationalPark("Yosemite")
    visitor_1 = Visitor("John")
    visitor_2 = Visitor("Jake")
    trip_1 = Trip(visitor_1, park, "May 1st", "May 31st")
    trip_2 = Trip(visitor_2, park, "June 2nd", "June 4th")

    print(park)
    print(park.name)

    # ipdb.set_trace()
