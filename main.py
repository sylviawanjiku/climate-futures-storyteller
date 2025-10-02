#!/usr/bin/env python3
"""
Main interface for the Climate Futures Storyteller.

This script provides a command-line interface for generating climate change narratives.
"""

import argparse
import sys

from climate_storyteller import ClimateStoryteller


def main():
    """Main function for the Climate Futures Storyteller interface."""
    parser = argparse.ArgumentParser(
        description="Generate compelling climate change narratives",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py                                    # Generate a random story
  python main.py --location "Miami, Florida"       # Generate story for specific location
  python main.py --impact drought --character rural_farmer  # Specify impact and character
  python main.py --list-locations                  # List available locations
  python main.py --list-impacts                    # List available climate impacts
  python main.py --list-characters                 # List available character types
        """,
    )

    parser.add_argument(
        "--location",
        "-l",
        type=str,
        help='Specific location for the story (e.g., "Miami, Florida", "Bangladesh Delta")',
    )

    parser.add_argument(
        "--impact",
        "-i",
        type=str,
        help='Climate impact type (e.g., "sea_level_rise", "drought", "extreme_heat", "wildfire")',
    )

    parser.add_argument(
        "--character",
        "-c",
        type=str,
        help='Character focus type (e.g., "coastal_community", "urban_worker", "rural_farmer")',
    )

    parser.add_argument(
        "--length",
        "-len",
        type=int,
        default=1200,
        help="Target word count for the story (default: 1200)",
    )

    parser.add_argument(
        "--output",
        "-o",
        type=str,
        help="Output file to save the story (default: print to console)",
    )

    parser.add_argument(
        "--list-locations", action="store_true", help="List all available locations"
    )

    parser.add_argument(
        "--list-impacts", action="store_true", help="List all available climate impacts"
    )

    parser.add_argument(
        "--list-characters",
        action="store_true",
        help="List all available character types",
    )

    args = parser.parse_args()

    # Initialize the storyteller
    storyteller = ClimateStoryteller()

    # Handle list commands
    if args.list_locations:
        print("Available locations:")
        for location in storyteller.list_available_locations():
            print(f"  - {location}")
        return

    if args.list_impacts:
        print("Available climate impacts:")
        for impact in storyteller.list_available_impacts():
            print(f"  - {impact}")
        return

    if args.list_characters:
        print("Available character types:")
        for character in storyteller.list_available_characters():
            print(f"  - {character}")
        return

    # Generate the story
    try:
        print("Generating climate futures story...")
        if args.location:
            print(f"Location: {args.location}")
        if args.impact:
            print(f"Climate impact: {args.impact}")
        if args.character:
            print(f"Character focus: {args.character}")
        print(f"Target length: {args.length} words")
        print("-" * 50)

        story = storyteller.generate_story(
            location=args.location,
            climate_impact=args.impact,
            character_focus=args.character,
            story_length=args.length,
        )

        # Output the story
        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(story)
            print(f"Story saved to {args.output}")
        else:
            print(story)

    except Exception as e:
        print(f"Error generating story: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
