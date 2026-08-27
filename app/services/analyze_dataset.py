from app.services.image_analysis import analyze_images


def main():
    result = analyze_images()

    print("\nGALLIVIS Ultrasound Dataset Analysis")
    print("=" * 50)

    print(f"Total images: {result['total_images']}")

    print("\nImage dimensions:")
    for dimension, count in result["dimensions"].most_common():
        print(f"  {dimension}: {count}")

    print("\nImage formats:")
    for image_format, count in result["formats"].most_common():
        print(f"  {image_format}: {count}")

    print(f"\nCorrupted images: {len(result['corrupted'])}")

    duplicate_groups = result["duplicates"]

    print(f"Duplicate groups: {len(duplicate_groups)}")

    if duplicate_groups:
        print("\nDuplicate groups:")

        for file_hash, paths in duplicate_groups.items():
            print(f"\nHash: {file_hash}")

            for path in paths:
                print(f"  - {path}")


if __name__ == "__main__":
    main()