def swap_tile(map_file):
    """
    Swap specific tiles inside the declared .txt file for mapping.
    Reference maps.py for tile codes.
    """
    with open(map_file, "r+") as f:
        file_text = f.read()
        for line in file_text:
            file_text = file_text.replace('', '') # <----- ('old_tile', 'new_tile')
        f.seek(0)
        f.write(file_text)
        f.truncate()

    return
