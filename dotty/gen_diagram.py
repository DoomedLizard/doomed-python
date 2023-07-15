#!/usr/bin/env python3

"""
Module creating a GraphViz diagram
"""

nodes=[
    "a",
    "b",
    "c"
]

edges = [
    ["a", "b"],
    ["b", "c"],
    ["c", "a"]
]

print("digraph G {")

for node in nodes:
    print("  " + node)

print("")

for edge in edges:
    print("  " + edge[0] + " -> " + edge[1])

print("}")
