import argparse
from data_models import UserProfile, build_profiles
from legacy_utils import legacy_signature_report, legacy_event_loop


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True)
    parser.add_argument("--count", type=int, default=1)
    return parser.parse_args()


def main():
    args = parse_args()
    profiles = build_profiles(args.name, args.count)

    for profile in profiles:
        print("User:", profile.display_name())

    print(legacy_signature_report(UserProfile))
    print(legacy_event_loop())


if __name__ == "__main__":
    main()
