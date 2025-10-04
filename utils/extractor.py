import zipfile

def extract_zip(zip_path, extract_to):
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        print(f"[+] Ekstrak sukses ke: {extract_to}")
    except Exception as e:
        print(f"[-] Gagal ekstrak: {e}")
