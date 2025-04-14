import nibabel as nibimport numpy as np
from PIL import Image
import os
import glob
 
def tiff_to_nifti(tiff_file, nii_file):
    img = Image.open(tiff_file)
    img_array = np.array(img)
    nifti_img = nib.Nifti1Image(img_array, affine=np.eye(4))
    nib.save(nifti_img, nii_file)
 
# Directory containing TIFF files
directory = r'E:\Brain 1\3D reconstruction_viewer'
tiff_pattern = os.path.join(directory, '*.tif')  # Adjust pattern if necessary
tiff_files = glob.glob(tiff_pattern)
 
# Loop through each TIFF file and convert it
for tiff_file in tiff_files:
    # Create output NIfTI file name
    nii_file = os.path.splitext(tiff_file)[0] + '.nii'  # Change extension to .nii
    print(f'Converting {tiff_file} to {nii_file}')
    tiff_to_nifti(tiff_file, nii_file)
 
print("Conversion completed.")
