# Tahoe MLS Members Scraper

A simple Python 3 script that crawls the public **Tahoe MLS** member directory and exports the results to a CSV file.

---

## ✨ Features

* **Automated pagination** – iterates through the directory 20 records per page until no more data are returned.
* **Duplicate protection** – skips rows whose e‑mail address has already been seen.
* **Custom headers** – sends a realistic `User‑Agent` and `Referer` to reduce the risk of blocks.
* **Respectful rate‑limiting** – one‑second delay between requests (adjustable).
* **UTF‑8 CSV output** – writes `tahoemls_members.csv` with `Name`, `Office`, `Phone`, and `Email` columns.

---

## 🛠 Prerequisites

| Requirement              | Notes                           |
| ------------------------ | ------------------------------- |
| **Python 3.8 or higher** | Check with `python3 --version`  |
| **pip**                  | Comes with most Python installs |
| **requests**             | HTTP client                     |
| **beautifulsoup4**       | HTML parser                     |

Install the libraries in one shot:

```bash
pip install -r requirements.txt
```

<details>
<summary><code>requirements.txt</code> (copy & paste)</summary>

```
requests
beautifulsoup4
```

</details>

---

## 🚀 Usage

1. **Clone or download** this repository.
2. Open a terminal in the project directory.
3. Run the scraper:

   ```bash
   python3 tahoemls_scraper.py
   ```
![image](https://github.com/user-attachments/assets/5409004a-e87e-4a83-a17e-5fc4301d1f70)

The script will print progress to the console and create **tahoemls\_members.csv** in the same directory.

### Command‑line options (optional)

Currently all settings are hard‑coded for simplicity. Edit the constants at the top of `tahoemls_scraper.py` to:

* Change the **output filename** (`OUTFILE`).
* Adjust the **pagination range** (default `1 … 9999`).
* Increase/decrease the **sleep interval** (`time.sleep(1)`).
* Modify request **headers**.

---

## 📄 Output format

| Column   | Description                          |
| -------- | ------------------------------------ |
| `Name`   | Member’s full name                   |
| `Office` | Brokerage / agency name              |
| `Phone`  | Primary contact number               |
| `Email`  | E‑mail address (blank if not listed) |

---

## 🧩 How it works

1. Builds the query parameters required by the members directory (e.g. `mtype=1`).
2. Sends an HTTP GET request and parses the HTML with **BeautifulSoup**.
3. Selects rows using the CSS selectors `tr.trResultsRow` and `tr.trResultsRowAlt`.
4. Extracts the four fields, cleans whitespace, and writes to CSV.
5. Repeats with the next `Start` value until the page returns **no rows** or only duplicates.

---

## ⏱ Rate‑limiting & etiquette

The Tahoe MLS site appears to tolerate modest traffic, but it’s best to:

* Keep `time.sleep(1)` or longer between requests.
* Run the script during off‑peak hours.
* Cache results instead of scraping repeatedly.

---

## ⚖️ Legal & Ethical Notice

This script is provided **for educational purposes only**. Before scraping any website:

* Review the site’s **Terms of Service**.
* Respect `robots.txt` and copyright.
* Obtain explicit permission if required.

The author **assumes no liability** for misuse or violations of Tahoe MLS policies. Use responsibly.

### 📢 Disclaimer

This tool is not affiliated with or endorsed by the Tahoe MLS. The information scraped using this script may be subject to copyright or privacy considerations. Use of this script is at your own risk. The developer is not responsible for any legal consequences or damages arising from its use.

---

## 🩹 Troubleshooting

| Symptom         | Possible cause       | Fix                                            |
| --------------- | -------------------- | ---------------------------------------------- |
| `403 Forbidden` | Site blocked your IP | Increase delay, rotate IP, or reduce frequency |
| Empty CSV       | No matching rows     | Verify parameters (e.g., `mtype`)              |
| Garbled output  | Wrong file encoding  | Ensure you open the CSV with UTF‑8 support     |

---

## 🤝 Contributing

Pull requests are welcome! Feel free to open an issue to suggest improvements.

---

## 📜 License

Released under the **MIT License** – see `LICENSE` for details.

---

### Acknowledgements

* [Requests](https://docs.python-requests.org/)
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)

> “What gets measured gets improved.” — Peter Drucker
