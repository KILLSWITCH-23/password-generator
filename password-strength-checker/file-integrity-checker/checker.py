import hashlib
import os
import json
import argparse

HASH_DB = "hashes.json"

def calculate_hash(filepath):
    sha256 = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for block in iter(lambda: f.read(4096), b""):
                sha256.update(block)
        return sha256.hexdigest()
    except Exception as e:
        print(f"\033[91m❌ Error reading {filepath}: {e}\033[0m")
        return None


def get_all_files(path):
    files = []
    if os.path.isfile(path):
        files.append(path)
    elif os.path.isdir(path):
        for root, _, filenames in os.walk(path):
            for name in filenames:
                files.append(os.path.join(root, name))
    return files


def load_hashes():
    if not os.path.exists(HASH_DB):
        return {}
    with open(HASH_DB, "r") as f:
        return json.load(f)


def save_hashes(data):
    with open(HASH_DB, "w") as f:
        json.dump(data, f, indent=4)


def monitor(path):
    files = get_all_files(path)
    hashes = load_hashes()

    if not files:
        print("\033[91m❌ No files found.\033[0m")
        return

    for file in files:
        file_hash = calculate_hash(file)
        if file_hash:
            hashes[file] = file_hash
            print(f"\033[92m✅ Monitored: {file}\033[0m")

    save_hashes(hashes)
    print("\n\033[96m🔒 Monitoring complete.\033[0m")


def verify():
    hashes = load_hashes()

    if not hashes:
        print("\033[91m❌ No hashes to verify.\033[0m")
        return

    print("\n🔍 Verifying file integrity...\n")

    for file, old_hash in hashes.items():
        if not os.path.exists(file):
            print(f"\033[91m❌ MISSING: {file}\033[0m")
            continue

        new_hash = calculate_hash(file)
        if new_hash != old_hash:
            print(f"\033[91m⚠️ TAMPERED: {file}\033[0m")
        else:
            print(f"\033[92m✔ OK: {file}\033[0m")


def main():
    parser = argparse.ArgumentParser(
        description="File Integrity Checker (SHA-256)"
    )
    parser.add_argument("path", nargs="?", help="File or folder to monitor")
    parser.add_argument("--verify", action="store_true", help="Verify file integrity")

    args = parser.parse_args()

    if args.verify:
        verify()
    elif args.path:
        monitor(args.path)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
