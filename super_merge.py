# super_merge.py
import requests

txt_urls = [
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/main/mtn/sub_1.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/main/mtn/sub_2.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/main/mtn/sub_3.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/main/mtn/sub_4.txt",
]

output_file = "super_subscription.txt"
merged = []

for url in txt_urls:
    try:
        print(f"Fetching {url}...")
        resp = requests.get(url)
        if resp.status_code == 200:
            merged.append(resp.text.strip())
        else:
            print(f"❌ Failed to fetch {url}: {resp.status_code}")
    except Exception as e:
        print(f"❌ Error fetching {url}: {e}")

with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n\n".join(merged))

print(f"✅ Merged {len(txt_urls)} files into {output_file}")
