#Advent of Code 2023: Day 19
from icecream import ic
from copy import deepcopy


def cut_intervals(interval, cut):
    cut_variable, sign, border = cut
    start, end = interval[cut_variable]
    if sign == "<": # result = (condtition accepted, condition not accepted), -1 = no match
        if border <= start:
            result = (-1, (start, end))
        elif border > end:
            result = ((start, end), -1)
        else:
            result = ((start, border-1), (border, end))
    elif sign == ">":
        if border >= end:
            result = (-1, (start, end))
        elif border < start:
            result = ((start, end), -1)
        else:
            result = ((border+1, end), (start, border))
    accepted, not_accepted = result
    interval_accepted = deepcopy(interval)
    if accepted != -1:
        interval_accepted[cut_variable] = accepted
    else:
        interval_accepted = -1
    if not_accepted != -1:
        interval[cut_variable] = not_accepted
    else:
        interval = -1
    return interval_accepted, interval

#MAIN
interval = {"x": (1, 4000), "m": (1, 4000), "a": (1000, 3000), "s": (1, 4000), "path": ""}

#cut = ("a", ">", 1000)
#a,b = (cut_intervals(interval, cut))

