import requests

global current_version
current_version = float(1.00)


url = "https://github.com/actionschnitzel/PiGro-Aid-/releases/latest"
r = requests.get(url)

global github_release
github_release = r.url.split("/")[-1]
github_release = (float(github_release))
#print(github_release)

try:
    if github_release > current_version:
        print("[Info]: An Update is avalible !!!")
        update_checker()
    elif github_release < current_version:
        print("WTF HAPPEND HERE?!!")
    elif github_release == current_version:
        print("[Info]: All up to date!!!")
except:
    print("[Info]: Version Check not Possible")
