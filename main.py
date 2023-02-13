# Personal usage. Not useful for anyone else, but I want to have it in my repo for future reference and multi-computer use.

import file_management as fm
import image_processing as ip

# Delete the ORF files that are not in the JPG folder (I did the initial selection on the JPGs but want to modify the ORFs)
# fm.read_strip_add_delete_not_in_list("C:\\test\\2022-11-24 IdeaJam Final Pitch", "JPG", "C:\\test\\2022-11-24 IdeaJam Final Pitch\\Raw\\", ["orf"], verbose=True)

# parse the voc format file
image_names, bounding_boxes, labels = ip.read_voc_file("/home/irikos/Work/datasets/rip_currents/training_data/voc_labels.txt", separator=",")

print(image_names[0])
print(bounding_boxes[0])
print(labels[0])


# visualize the bounding boxes
for i in range(1):
    ip.visualize_bounding_box_voc("/home/irikos/Work/datasets/rip_currents/training_data/images/" + str(image_names[i]), bounding_boxes[i], labels[i], (100,0,0), verbose=True)

