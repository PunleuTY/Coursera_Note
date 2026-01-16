# Introduction to Digital Image
## Digital Image: Understanding Image Types and Formats

This lesson explores how digital images are captured, represented, and stored, and how different file formats impact image processing.

### Image Capture and Formation
- **Digital Cameras:** Use **electronic light receptors** to convert light waves into electrical signals, stored as numeric intensity values.
- **Brightness:** Determined by light amplitude; monochrome sensors capture grayscale images.
- **Color Images:** Created using three sensors that record light intensities for **red, green, and blue (RGB)** wavelengths.
- **Channels:** The RGB components that combine to form full-color images.

### Pixels and Resolution
- **Pixel:** The smallest element of a digital image, representing the intensity captured by one receptor.
- **Resolution:** Number of pixels in an image (vertical × horizontal).  
  - Higher resolution = more detail and better quality.
- **Other Quality Factors:** Sensor efficiency, focus, and exposure (light reaching the sensor).

### Beyond Visible Light
- **Scientific Imaging:** Uses non-visible wavelengths like **ultraviolet and infrared** to capture data.
- **Specialized Images:**
  - **Weather maps:** Created using radar signals.
  - **Medical imaging:** Includes **X-rays** and **MRI scans**, often using 3D data with **voxels** (3D pixels).
  - **3D Images:** Typically viewed as **2D slices** for easier analysis.
  - **Videos:** Represented as sequential 2D frames stacked over time.

### Image Storage and File Formats
- **Variety of Formats:** Due to different data dimensions (2D, 3D, time-based) and compression methods.
- **Compression:**
  - **Lossless:** Exact reproduction, minimal size reduction.
  - **Lossy:** Greater size reduction, minor visual loss.
- **Raw Images:** Uncompressed, very large files that store full sensor data.

### Metadata and Multimedia
- **Metadata:** Extra text data embedded in image/video files, may include:
  - Capture date and location  
  - Device information  
  - Frame rate, resolution, and description
- **Multimedia Files:** Can include both image/video and audio data.

### Choosing the Right Format
- **Key Factors:**
  - Trade-off between **quality and compression**
  - Number of images and **dimensionality (2D/3D)**
  - **Processing tasks** (e.g., deep learning, computer vision)
  - **Hardware limitations** like memory and processing power
- **Note:** Format choice is often predefined by the capture device, though conversion is possible.
### Type of Image & Video

| Image                                                 | Video                           |
| ----------------------------------------------------- | ------------------------------- |
| JPEG: Joint Photographic Experts Group                | GIF: Graphic Interchange Format |
| PNG: Portable Network Graphic                         | AVI: Audio Video Interleave     |
| PBM: Portable Bitmap                                  |                                 |
| RAS: Sun Raster                                       |                                 |
| HDF4: Hierarchical Dat Format                         |                                 |
| DICOM: Digital Imaging and Communication in Medicine  |                                 |
| NIFTI: Neuroimaging informatics Technology Initiative |                                 |
| TIFF: Tagged Image File Format                        |                                 |
| PGM: Portable Graymap                                 |                                 |

### Conclusion
Digital image formats vary by purpose, dimensionality, and compression method.  
Once imported into MATLAB, however, most image data is represented similarly—regardless of its original format.


# Working with Image Data


# Threshold Images


# Adjusting Image Contrast  