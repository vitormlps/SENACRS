# ### Built-in deps
import os

# ### Third-party deps
# ### Local deps


def clean_exports_folder():
    folder_path = "./exports/"

    if os.path.isdir(folder_path):
        dir_files = os.listdir(folder_path)

        if len(dir_files) > 5:
            for filename in os.listdir(folder_path):
                full_path = folder_path + filename

                if os.path.isfile(full_path) or os.path.islink(full_path):
                    os.unlink(full_path)
