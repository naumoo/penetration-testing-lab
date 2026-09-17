#!/usr/bin/env python3
"""Simple qualitative risk helper for lab vulnerability reports."""

import argparse


def rate(impact: int, likelihood: int):
    score = impact * likelihood
    if score >= 7:
        return score, "High"
    if score >= 4:
        return score, "Medium"
    return score, "Low"


def main():
    parser = argparse.ArgumentParser(description="Calculate a simple lab risk rating")
    parser.add_argument("--impact", type=int, choices=range(1, 4), required=True, help="1=low, 2=medium, 3=high")
    parser.add_argument("--likelihood", type=int, choices=range(1, 4), required=True, help="1=low, 2=medium, 3=high")
    args = parser.parse_args()
    score, rating = rate(args.impact, args.likelihood)
    print(f"Risk score: {score}/9")
    print(f"Risk rating: {rating}")


if __name__ == "__main__":
    main()
