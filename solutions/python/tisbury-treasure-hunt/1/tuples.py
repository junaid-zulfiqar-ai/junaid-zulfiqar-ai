"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate."""
    return record[1]

def convert_coordinate(coordinate):
   """Split the given cordinates into tuple containing its individual components"""
   return tuple(coordinate)

def compare_records(azara_record, rui_record):
    """Compare two record types and detemine if their coordinates match."""
    azara_coord = convert_coordinate(get_coordinate(get_coordinate(azara_record))
    return azara_coord == rui_record[1]

def create_record(azara_record, rui_record):
    """"Combine the two record (if possible) and create a combined record group."""
    if compare_records(azara_record, rui_record):
       return azara_record + rui_record

    return "not a match"  

def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records."""
    report = ""
    for item in combined_record_group:
        # Reconstruct the tuple using indices 0, 2, 3, and 4
        clean_tuple = (item[0], item[2], item[3], item[4])
        report += f"{clean_tuple}/n"

    return report