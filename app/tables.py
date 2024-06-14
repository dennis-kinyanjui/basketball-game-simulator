# app/tables.py

def print_table(data, headers):
    """Print a formatted table."""
    if not data:
        return

    # Print headers
    header_row = " | ".join(headers)
    print(header_row)
    print("-" * len(header_row))

    # Print data rows
    for item in data:
        row_values = [str(item.get(header.lower().replace(" ", "_"))) for header in headers]
        print(" | ".join(row_values))
