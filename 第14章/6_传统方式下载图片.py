import requests

def download_picture(url):
    print(f"开始下载{url}")
    response = requests.get(url)
    print("下载完毕")
    with open(f"{url[-10:]}.jpg","wb") as file:
        file.write(response.content)

def main():
    url_list = [
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhFcqE9Ht9Z_dTYV2MgzxSsOM7WNstAnsKpzQ23x5AFw&s=10",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPS2Q2yHjKfD9ynhy43r-OPHjmub4HE60ayqNWRZkjEg&s=10",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQyTebqfsC5M4PTmTUPf8JcS7nP6ni2uzuB-zeooYrYPw&s=10"
    ]

    for url in url_list:
        download_picture(url)

main()
