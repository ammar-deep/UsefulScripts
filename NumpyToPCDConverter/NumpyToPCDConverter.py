import argparse
from glob import glob
import open3d as o3d
import numpy as np
import os
from tqdm import tqdm

def convert_numpy_to_pcd(numpy_dir, output_dir):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Find all numpy files in the specified directory
    numpy_paths = glob(os.path.join(numpy_dir, "*.npy"))

    for numpy_path in tqdm(numpy_paths):
        # Load numpy data
        numpy_data = np.load(numpy_path)

        # Extract XYZ coordinates and transpose
        xyz = numpy_data[:3, :].transpose()

        # Create a basename for the output PCD file
        basename = os.path.basename(numpy_path)
        basename = basename.replace('npy', 'pcd')
        pcd_path = os.path.join(output_dir, basename)

        # Create an Open3D PointCloud object and set points
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(xyz)

        # Write the PointCloud to the output PCD file
        o3d.io.write_point_cloud(pcd_path, pcd)

def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(description="Convert numpy files to PCD format")

    # Add arguments for input and output directories
    parser.add_argument("--numpy-dir", required=True, help="Directory containing numpy files")
    parser.add_argument("--output-dir", required=True, help="Directory to save PCD files")

    # Parse the arguments
    args = parser.parse_args()

    # Convert numpy files to PCD format
    convert_numpy_to_pcd(args.numpy_dir, args.output_dir)

if __name__ == "__main__":
    main()
