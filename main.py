# Personal usage. Not useful for anyone else, but I want to have it in my repo for future reference and multi-computer use.

import file_management as fm

# Delete the ORF files that are not in the JPG folder (I did the initial selection on the JPGs but want to modify the ORFs)
fm.read_strip_add_delete_not_in_list("C:\\test\\2022-11-24 IdeaJam Final Pitch", "JPG", "C:\\test\\2022-11-24 IdeaJam Final Pitch\\Raw\\", ["orf"], verbose=True)