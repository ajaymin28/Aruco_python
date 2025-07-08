# Augmented Reality with Aruco Markers in Python

A Python project that brings augmented reality to life by overlaying 3D objects on Aruco markers using OpenCV and OpenGL.

## Demo

<p align="center">
  <a href="http://www.youtube.com/watch?v=RNwTGPvuhPw">
    <img src="http://img.youtube.com/vi/RNwTGPvuhPw/0.jpg" alt="YouTube Demo" />
  </a>
</p>

---

## Requirements

* **Python** 3.x
* **OpenCV** 3.x (`opencv_contrib` required for Aruco support)
* **imutils**
* **PyYAML**
* **pygame**
* **PyOpenGL**

Install Python packages via pip:

```bash
pip install imutils pyyaml pygame PyOpenGL
```

> Developed and tested on Anaconda 4 (Python 3.x, Windows 10), but should work on most platforms.

---

## Project Structure

* `main.py`: Main code. Loads the 3D object, initializes your camera, detects Aruco markers, and overlays the 3D object.
* `objloader.py`: Utility for loading OBJ files (see [PyGame Wiki](https://www.pygame.org/wiki/OBJFileLoader)).
* `.obj` and `.mtl` files: Your 3D model (exported from Blender or other 3D software). Both are required for proper rendering.

---

## Getting Started

1. **Camera Calibration**

   * Calibrate your camera first. Use scripts in the `calibration` directory (see details below).
   * This generates a `.yaml` file for your camera matrix.
2. **Prepare Your Files**

   * Place your `camera_matrix.yaml`, `.obj`, and `.mtl` files in the project’s main directory.
3. **Run the Demo**

   ```bash
   python main.py
   ```

---

## Calibration

You can calibrate using either a chessboard or an Aruco board.

### Aruco Board Calibration

* Edit `calibration/main.py`:

  * Set your video source (camera index or file).
  * Set output YAML filename.
* Run and follow the instructions.
* When done, copy the generated YAML to the main directory.

### Chessboard Calibration

* Edit `calibration/aruco.py`:

  * Set your video source and output YAML filename.
* Run the script.
* Move or rename the generated YAML file to match the main directory config.

---

## Using Your Own 3D Objects

* Download `.obj` models with matching `.mtl` files (e.g., from [Free3D](https://free3d.com/3d-models/obj-file)).
* Replace the `.obj` and `.mtl` files in your main directory.
* Without an `.mtl` file, objects will render black.
* You can create/edit models in Blender or other 3D tools.

---

## Troubleshooting & Tips

* OpenGL window lighting may be dimmer than OpenCV—work in a well-lit room.
* All required files (`main.py`, `objloader.py`, model files, `camera_matrix.yaml`) must be in the same folder.
* Report bugs or issues by opening an issue or reaching out.

---

## License & Attribution

* 3D models included are not owned by me. See the license/readme in `models/` or `zip/sinband/` for details.

## References

* [University of Cordoba: Aruco Documentation](https://www.uco.es/investiga/grupos/ava/node/26)
* [Augmented Reality using OpenCV, OpenGL, and Blender](https://rdmilligan.wordpress.com/2015/10/15/augmented-reality-using-opencv-opengl-and-blender/)
* [JeVois Aruco Demo](http://jevois.org/moddoc/DemoArUco/modinfo.html)

---
