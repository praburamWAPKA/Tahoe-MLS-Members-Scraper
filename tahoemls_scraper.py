#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import csv
import time

BASE_URL = "https://members.tahoemls.com/public/members.cfm"
HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://members.tahoemls.com/"
}

OUTFILE = "tahoemls_members.csv"
seen_emails = set()

with open(OUTFILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Office", "Phone", "Email"])

    for start in range(1, 10000, 20):
        params = {
            "Start": start,
            "FirstName": "",
            "LastName": "",
            "OID": "any",
            "alpha": "any",
            "mtype": "1"
        }

        print(f"[+] Fetching page starting at {start}...")
        res = requests.get(BASE_URL, headers=HEADERS, params=params)
        soup = BeautifulSoup(res.text, "html.parser")

        rows = soup.select("tr.trResultsRow, tr.trResultsRowAlt")
        if not rows:
            print("[!] No more rows. Ending.")
            break

        new_entries = 0

        for row in rows:
            cells = row.find_all("td")
            if len(cells) >= 4:
                name = cells[0].get_text(strip=True)
                office = cells[1].get_text(strip=True)
                phone = cells[2].get_text(strip=True)
                email = cells[3].find("a")
                email = email.get("href").replace("mailto:", "") if email else ""

                if email in seen_emails:
                    continue  # Skip duplicates

                seen_emails.add(email)
                writer.writerow([name, office, phone, email])
                print(name, office, phone, email)
                new_entries += 1

        if new_entries == 0:
            print("[✓] No new entries on this page. Exiting.")
            break

        time.sleep(1)  # Rate limit

