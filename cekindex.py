import requests
import concurrent.futures

# Fungsi untuk memeriksa keberadaan index.php
def check_index_php(url):
    try:
        response = requests.get(f"{url}/index.php")
        if response.status_code == 200:
            return f"index.php found at: {url}/index.php"
        else:
            return f"index.php not found at: {url}"
    except requests.exceptions.RequestException as e:
        return f"Error checking {url}: {e}"

# Fungsi utama untuk memeriksa keberadaan index.php di semua situs web
def check_websites_for_index_php(websites):
    notifications = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_url = {executor.submit(check_index_php, url): url for url in websites}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                result = future.result()
                notifications.append(result)
            except Exception as e:
                notifications.append(f"An error occurred with {url}: {e}")
    return notifications

# Daftar situs web yang akan diperiksa
websites = [
    "https://example1.com",
    "https://example2.com",
    "https://example3.com",
    # Tambahkan situs web lainnya di sini
]

# Memeriksa situs web dan menampilkan notifikasi
notifications = check_websites_for_index_php(websites)
for notification in notifications:
    print(notification)