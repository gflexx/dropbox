from dotenv import load_dotenv
import dropbox
import os

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

# Initialize Dropbox client
dbx = dropbox.Dropbox(ACCESS_TOKEN)


def get_root_folders():
    """
    get root folders
    """
    print("Getting root folder list...")

    folder_list = dbx.files_list_folder("")
    for entry in folder_list.entries:
        print(entry.name)

def main():
    try:
        user_account = dbx.users_get_current_account()
        print("Connected Succesfully to dbx...")
        print(f"User Email: {user_account.email} \n")

    except dropbox.exceptions.AuthError as e:
        print(f"Authentication error: {e}")

    get_root_folders()

    

    

if __name__ == "__main__":
    main()