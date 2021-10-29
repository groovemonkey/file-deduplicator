#!/usr/bin/env python3
# dave@tutorialinux.com

# deduplicator; like uniq but remembers lines

import sys

# To avoid unnecessary/expensive iteration through a dict that ALSO has to keep order (which defeats the point), we write each line to two datastructures
# one that tells us if we've seen it before, and another (ordered) datastructure to create the de-duped output
seen_lines = {}
deduped_lines = []

try:
    with open(sys.argv[1], 'r') as dedupfile:
        for line in dedupfile:
            # we only care if it's not in there, else we discard the line
            # also we want to respect (repeating) newlines
            if line not in seen_lines or line == "\n":
                seen_lines[line] = 1
                deduped_lines.append(line)
except Error as err:
    print(err)
    sys.exit(1)


print("".join(deduped_lines))


