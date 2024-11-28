import numpy as np
import nibabel as nib
import sys


if __name__ == '__main__':
    warp_file = sys.argv[1]
    ants_file=sys.argv[1]
    
    ANTs_NIB = nib.load(ants_file)
    warp_NIB = nib.load(warp_file)
    warp_new = np.expand_dims(warp_NIB.get_fdata(),axis=3)
    warp_new_NIB = nib.Nifti1Image(warp_new, header=ANTs_NIB.header, affine=ANTs_NIB.affine)
    warp_new_NIB.to_filename(warp_file.replace('.nii.gz','_ANTslike.nii.gz'))