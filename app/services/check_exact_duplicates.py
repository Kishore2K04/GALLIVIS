from app.services.exact_duplicate_detector import find_exact_duplicates


def main():
    duplicates = find_exact_duplicates()

    print("\nGALLIVIS Exact Duplicate Analysis")
    print("=" * 50)

    print(f"Exact duplicate groups: {len(duplicates)}")

    if not duplicates:
        print("\nNo exact duplicates found.")
        return

    for file_hash, paths in duplicates.items():

        print(f"\nSHA-256: {file_hash}")

        for path in paths:
            print(f"  - {path}")


if __name__ == "__main__":
    main()