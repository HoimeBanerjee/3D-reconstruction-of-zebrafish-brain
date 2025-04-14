##calling the library
!pip install nibabel pillow numpy


##Setting the directory and checking the files
import osdirectory = r'E:\Brain 1\3D reconstruction_viewer'files = os.listdir(directory)print(files)

##Providing the path
tiff_file_path = r'E:\Brain 1\3D reconstruction_viewer\Section01.tif’

##Changing the format
import nibabel as nib
import numpy as np
from PIL import Image

def tiff_to_nifti(tiff_file, nii_file):    
img = Image.open(tiff_file)    
img_array = np.array(img)    
nifti_img = nib.Nifti1Image(img_array, affine=np.eye(4)) 
 nib.save(nifti_img, nii_file)


# Example usagetiff_file_path = r'E:\4\Brain 1\3D reconstruction_viewer\Section01.tif'  # Adjust based on the listing
nii_file_path = r'E:\3D reconstruction_viewer\Section01.nii’
tiff_to_nifti(tiff_file_path, nii_file_path)
