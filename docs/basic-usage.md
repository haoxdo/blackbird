# 🔍 Basic Usage

{% hint style="warning" %}
Blackbird can make mistakes. Consider checking the information.
{% endhint %}

### 👤 Username Reverse Search

```bash
python blackbird.py --username username1
```

```bash
python blackbird.py --username username1 username2 username3
```

```bash
python blackbird.py --username-file usernames.txt
```

### 📧 Email Reverse Search

```bash
python blackbird.py --email email1@email
```

```bash
python blackbird.py --email email1@email email2@email email3@email
```

```bash
python blackbird.py --email-file emails.txt
```

### 📁 Export

#### PDF

```bash
python blackbird.py --username p1ngul1n0 --pdf
```

<figure><img src=".gitbook/assets/pdf-full.png" alt=""><figcaption></figcaption></figure>

#### CSV

A CSV is saved to the `results/` directory automatically after every search, so no flag is required:

```
python blackbird.py --username username1
```

To skip the CSV export, use `--no-csv`:

```
python blackbird.py --username username1 --no-csv
```

#### JSON

```
python blackbird.py --username username1 --json
```

#### DUMP

Dump all found account HTTP responses.

```
python blackbird.py --username username1 --dump
```

### 🧹 Log Cleanup

Blackbird removes its own log file (`logs/blackbird.log`) once a search finishes, so only the exported results remain on disk.

To keep the log for troubleshooting, use `--no-clean`:

```
python blackbird.py --username username1 --no-clean
```
