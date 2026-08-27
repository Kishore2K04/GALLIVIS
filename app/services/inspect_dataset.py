from app.services.dataset_scanner import scan_ultrasound_directory


def main():
    result = scan_ultrasound_directory()

    print("\nGALLIVIS Dataset Inspection")
    print("=" * 40)

    print(f"Directory: {result['directory']}")
    print(f"Total files: {result['total_files']}")
    print(f"Valid images: {result['valid_images']}")
    print(f"Invalid files: {len(result['invalid_images'])}")

    if result["invalid_images"]:
        print("\nInvalid files:")

        for file_path in result["invalid_images"]:
            print(f"- {file_path}")


if __name__ == "__main__":
    main()