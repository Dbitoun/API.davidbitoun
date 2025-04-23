import requests
import json
import sys

def main():
    url = "https://api.fbi.gov/wanted/v1/list"
    r = requests.get(url)
    if r.status_code != 200:
        print(f"Failed to fetch data: HTTP {r.status_code}")
        sys.exit(1)

    with open('fbi.json', 'w') as outfile:
        json.dump(r.json(), outfile, indent=4)

    items = r.json().get("items", [])
    TARGET = "SHOULD BE CONSIDERED ARMED AND DANGEROUS"

    for person in items:
        if person.get("warning_message") != TARGET:
            continue

        name = person.get("title", "N/A")
        base_url = person.get("url", "")
        direct_pdf = f"{base_url.rstrip('/')}/download.pdf" if base_url else "N/A"
        gender = person.get("sex") or person.get("gender") or "N/A"
        subjects = person.get("subjects", [])

        print(f"Name: {name}")
        print(f"FBI direct link: {direct_pdf}")
        print(f"Gender: {gender}")
        for subj in subjects:
            print(f"subject:{subj}")
        print()

    subject_counts = {}
    for person in items:
        for subj in person.get("subjects", []):
            subject_counts[subj] = subject_counts.get(subj, 0) + 1

    sorted_subjects = sorted(subject_counts.items(),
                    key=lambda pair: pair[1],
                    reverse=True)
    print("Crime counts:")
    for crime, count in sorted_subjects:
        print(f"Crime: {crime} Count: {count}")

if __name__ == "__main__":
    main()