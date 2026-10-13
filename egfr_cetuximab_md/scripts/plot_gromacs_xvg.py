#!/usr/bin/env python3
"""Plot a GROMACS .xvg file to PNG using matplotlib.

Usage:
    python plot_gromacs_xvg.py input.xvg output.png --title "Backbone RMSD"

The script skips GROMACS metadata lines beginning with @ or #.
It plots the first numeric column as x and the second as y.
Check the axis labels and units for each input before using the figure.
"""
import argparse
from pathlib import Path

import matplotlib.pyplot as plt


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Input GROMACS .xvg file")
    parser.add_argument("output", help="Output PNG path")
    parser.add_argument("--title", default="GROMACS analysis")
    parser.add_argument("--xlabel", default="Time / frame")
    parser.add_argument("--ylabel", default="Value")
    args = parser.parse_args()

    rows = []
    with open(args.input, "r", encoding="utf-8", errors="replace") as handle:
        for line in handle:
            line = line.strip()
            if not line or line.startswith(("#", "@")):
                continue
            parts = line.split()
            if len(parts) >= 2:
                try:
                    rows.append((float(parts[0]), float(parts[1])))
                except ValueError:
                    continue

    if not rows:
        raise SystemExit(f"No numeric x/y data found in {args.input}")

    x, y = zip(*rows)
    plt.figure(figsize=(8, 4.8))
    plt.plot(x, y)
    plt.title(args.title)
    plt.xlabel(args.xlabel)
    plt.ylabel(args.ylabel)
    plt.tight_layout()
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(args.output, dpi=200)
    print(f"Saved plot: {args.output}")


if __name__ == "__main__":
    main()
