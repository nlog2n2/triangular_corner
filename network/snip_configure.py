import re

PATH = ""

# regex to find all interface config
pattern = re.compile(r"interface(.+?\n)\!", re.MULTILINE | re.DOTALL)

# fmt: off
interfaces = ""
lists      = []
# fmt: on

# open the file and store it in a variable
with open(PATH) as file:
    # iterate through the matches
    for match in pattern.finditer(file.read()):
        # store the match in a variable
        interfaces = match.group(0)

# iterate through the interfaces
for _interface_config in lists:
    # make a list for each match
    match = []
    # find all the interface matches in each interface config
    match.extend(re.findall(r"interface.*", _interface_config))
    print(match)
