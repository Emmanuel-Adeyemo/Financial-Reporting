
def match_headers(headers):
    """Map dynamic headers to standard keys using predefined mapping."""
    mapped_headers = {}
    lowercase_headers = [header.lower() for header in headers]  # Convert headers to lowercase for case-insensitive matching
    for standard_key, possible_headers in header_mapping.items():
        for possible_header in possible_headers:
            if possible_header in lowercase_headers:
                original_header = headers[lowercase_headers.index(possible_header)]  # Get the original header name
                mapped_headers[original_header] = standard_key
    return mapped_headers


