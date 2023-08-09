# NumpyToPCDConverter

NumpyToPCDConverter is a Python script that converts LiDAR data in numpy format to Point Cloud Data (PCD) format using the Open3D library. This tool simplifies the process of transforming raw numerical data into a widely-used format suitable for various applications, such as camera-lidar calibration and point cloud visualization.

## Features

- Convert LiDAR data from numpy format to PCD format.
- Efficiently process large datasets.
- Retain important metadata during conversion.
- Customizable conversion parameters for optimal results.

## Use Cases

- **Camera-LiDAR Calibration:** Convert LiDAR data to PCD format for accurate calibration with camera data, enabling precise alignment and synchronization between sensor modalities.

- **Point Cloud Visualization:** Convert LiDAR data into a format compatible with point cloud visualization software, allowing easy exploration and analysis of 3D data.

## Dependencies

- Python 3.x
- Open3D library (install using: `pip install open3d`)
- NumPy library (install using: `pip install numpy`)
- tqdm library (install using: `pip install tqdm`)

## Usage

### Run the script using the following command:

``` python NumpyToPCDConverter.py --numpy-dir input_numpy_files --output-dir output_pcd_files ```

- Replace input_numpy_files with the path to your input numpy files directory and output_pcd_files with the desired output directory for PCD files.

- The script will convert each .npy file in the input directory and save the corresponding PCD files in the output directory.
