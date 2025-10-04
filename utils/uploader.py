import os, base64, requests

def upload_to_github(token, repo, path):
    headers = {'Authorization': f'token {token}'}

    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, path)

            with open(file_path, 'rb') as f:
                content = f.read()

            encoded = base64.b64encode(content).decode('utf-8')
            url = f'https://api.github.com/repos/{repo}/contents/{rel_path}'

            data = {
                'message': f'Add {rel_path}',
                'content': encoded
            }

            r = requests.put(url, headers=headers, json=data)
            if r.status_code in [200, 201]:
                print(f"[+] Uploaded: {rel_path}")
            else:
                print(f"[-] Failed: {rel_path} ({r.status_code})")
