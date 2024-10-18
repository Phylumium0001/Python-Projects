import re

def get_lines(filepath):
    """
    Returns the lines in the md
    """
    with open(filepath) as file:
        lines = file.readlines()
        return lines
    
def translate_lines(lines):
    """
    Converts the lines of md to HTML
    """
    # regexes
    results = []
    
    hash = re.compile(r"^#+")
    hyphene = re.compile(r"^-+")
    #TODO: Fix the italics regex, it matches for the bold **bold** => *bold*
    italics = re.compile(r"\*(\w+)\*")
    bold = re.compile(r"\*\*(\w)\*\*")
    numbering = re.compile(r"\d+\.")

    # for encapsulating the lists with <ul></ul>
    list_counter = 0
    list = False

    for line in lines:
        if line == "\n":
            # Empty line, do not inspect, just increment
            results.append(line)
            continue


        header = False
        # remove newline
        line = line.replace("\n","")

        # Search for matching objects
        # Returns a list of matches
        mo_hash_tags = hash.search(line)
        mo_hyphene = hyphene.search(line)
        mo_italics = italics.findall(line)
        mo_numbering = numbering.search(line)
        
        if mo_italics:
            # Can have more than one match
            for match in mo_italics:
                # Remove the asterix
                line = line.replace(f"**{match}**",f"<strong>{match}</strong>")
            

        if mo_hash_tags:
            # Defines a header tag
            match = mo_hash_tags.group()
            magnitude = len(match)
            line = line.replace(f"{match}","")
            line = f"<h{magnitude}>{line}</h{magnitude}>"
            header = True

        if not header:
            # Encapsulates with ptag if the line is not a header
            line = f"<p>{line}</p>"

        if mo_hyphene:
            # Defines undordered lists
            match = mo_hyphene.group()
            line = line.replace("- ","")
            line = f"<li>{line}</li>"

            # Handle the <ul> tag 
            if list_counter == 0:
                line = f"<ul>{line}"
                list_counter += 1

            # Update list checker
            list = True

        if mo_numbering and header:
            # Defines numbered lists
            match = mo_numbering.group()
            line = f"<ol>{line}</ol>"

        # Check whether the current element is a a list
        if not list and list_counter > 0:
            # The list has ended
            # access previous list and update
            previous_list = results.pop()
            previous_list = f"{previous_list[:-2]}</ul>"
            # Return it back
            results.append(previous_list)
            list_counter = 0

        # Add back the line
        line += "\n"
        results.append(line)

        # Change the list checker 
        list = False

    return results