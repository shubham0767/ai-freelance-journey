import requests
def get_github_profile(username):
    url = f"https://api.github.com/users/{username}"

    try :
        response=requests.get(url)

        if response.status_code==200:
            data=response.json()
            return data

        else:
            return None

    except requests.exceptions.RequestException:
        print("Error : Could not Connect to github.")
        return None

def display_profile(data):
    print("=" * 40)
    print("       GITHUB PROFILE ANALYZER")
    print("=" * 40)

    print("Name        :", data["name"])
    print("Username    :", data["login"])
    print("Bio         :", data["bio"])
    print("Repositories:", data["public_repos"])
    print("Followers   :", data["followers"])
    print("Following   :", data["following"])
    print()
    print("Profile     :", data["html_url"])

    print("=" * 40)

username = input("Enter github username:")

profile=get_github_profile(username)

if profile:
    display_profile(profile)
else:
    print("Github user not found")