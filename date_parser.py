from datetime import date, datetime


def parse_date(date_string):
    """Parse a date string in DD/MM/YYYY format into a datetime.date.

    Input dates are always expected to use DD/MM/YYYY format, e.g.
    '03/04/2024' is interpreted as the 3rd of April 2024 (day=03,
    month=04, year=2024).

    Args:
        date_string: The date string to parse, e.g. '03/04/2024'.

    Returns:
        A datetime.date object representing the parsed date.

    Raises:
        ValueError: If date_string is not a valid DD/MM/YYYY date.
            For example, parse_date('April 3rd, 2024') raises a
            ValueError because 'April 3rd, 2024' is never a valid
            DD/MM/YYYY date string.

    Examples:
        >>> parse_date('03/04/2024')
        datetime.date(2024, 4, 3)

        >>> parse_date('April 3rd, 2024')
        Traceback (most recent call last):
            ...
        ValueError: invalid date 'April 3rd, 2024': expected DD/MM/YYYY format (e.g. '03/04/2024')
    """
    try:
        parsed = datetime.strptime(date_string, "%d/%m/%Y")
    except (TypeError, ValueError) as exc:
        raise ValueError(
            f"invalid date {date_string!r}: expected DD/MM/YYYY format (e.g. '03/04/2024')"
        ) from exc

    return date(parsed.year, parsed.month, parsed.day)
