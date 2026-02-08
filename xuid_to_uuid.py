#!/usr/bin/env python3
"""
XUID to UUID Converter

This script takes a userid/gamertag as input, queries the GeyserMC API
to get the XUID (DEC), converts it to HEX, then converts it to UUID format.

API: https://api.geysermc.org/v2/xbox/xuid/{gamertag}
"""

import argparse
import json
import sys

import requests


def lookup_xuid_dec(session, url, gamertag):
    """Lookup XUID (DEC) for the given gamertag using GeyserMC API."""
    try:
        response = session.get(f"{url}{gamertag}")
        response.raise_for_status()

        data = response.json()
        if 'xuid' in data:
            return data['xuid']
        return None

    except requests.RequestException as e:
        print(f"Error during XUID lookup: {e}", file=sys.stderr)
        return None
    except json.JSONDecodeError:
        print("Error: Invalid JSON response from API", file=sys.stderr)
        return None


def xuid_dec_to_hex(xuid_dec):
    """Convert XUID (DEC) to XUID (HEX) - 16 character hex string."""
    try:
        # Convert decimal to hex and ensure it's 16 characters (padded with leading zeros)
        xuid_hex = format(int(xuid_dec), '016X')
        return xuid_hex
    except (ValueError, TypeError):
        return None


def xuid_hex_to_uuid(xuid_hex):
    """Convert XUID HEX to UUID format: 00000000-0000-0000-xxxx-xxxxxxxxxxxx"""
    if not xuid_hex or len(xuid_hex) != 16:
        return None

    # Format as UUID: 00000000-0000-0000-xxxx-xxxxxxxxxxxx
    uuid = f"00000000-0000-0000-{xuid_hex[:4]}-{xuid_hex[4:]}"
    return uuid


def main():
    parser = argparse.ArgumentParser(
        description='Convert Xbox Gamertag to UUID via XUID lookup'
    )
    parser.add_argument(
        'userid',
        help='Xbox Gamertag/UserID to lookup'
    )

    args = parser.parse_args()

    # Create a session
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'xuid-to-uuid/1.0'
    })

    url = "https://api.geysermc.org/v2/xbox/xuid/"

    # Lookup the XUID (DEC)
    xuid_dec = lookup_xuid_dec(session, url, args.userid)

    if not xuid_dec:
        print(f"Failed to retrieve XUID for gamertag '{args.userid}'. The gamertag may not exist.", file=sys.stderr)
        sys.exit(1)

    # Convert to HEX
    xuid_hex = xuid_dec_to_hex(xuid_dec)
    if not xuid_hex:
        print("Failed to convert XUID to HEX.", file=sys.stderr)
        sys.exit(1)

    # Convert to UUID
    uuid = xuid_hex_to_uuid(xuid_hex)

    if not uuid:
        print("Failed to convert XUID to UUID.", file=sys.stderr)
        sys.exit(1)

    # Output the result
    result = {
        "uuid": uuid,
        "name": "." + args.userid
    }

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
