"""Row-level cleaning of raw records."""

from __future__ import annotations


def drop_missing(rows: list[dict], required: list[str]) -> list[dict]:
    """Drop rows missing any of the required fields (empty string counts as missing)."""
    return [r for r in rows if all(r.get(k, "") != "" for k in required)]


def coerce_floats(rows: list[dict], fields: list[str]) -> list[dict]:
    """Convert given fields to float in place, leaving other fields untouched.

    Raises:
        ValueError: if a value cannot be converted.
    """
    out = []
    for r in rows:
        r = dict(r)
        for f in fields:
            r[f] = float(r[f])
        out.append(r)
    return out
