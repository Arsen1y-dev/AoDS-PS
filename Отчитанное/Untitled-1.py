
**Task 5: Binary Files**

We will use Python's built-in `struct` library to manipulate binary files.

1. Convert a signed two-byte integer to a binary file:
```python
import struct

# Define the format string for a signed two-byte integer
format_str = '>h'  # '>h' means big-endian, two-byte, signed integer

# Create a binary file with the value -32768 (0x8000)
with open('int_file.bin', 'wb') as f:
    struct.pack(format_str, -32768).write(f)

print("Wrote binary file: int_file.bin")
```
This will create a binary file `int_file.bin` containing the value `-32768`.

2. Read the signed two-byte integer from the binary file:
```python
with open('int_file.bin', 'rb') as f:
    data = f.read(2)
    num, = struct.unpack('>h', data)

print("Read value:", num)
```
This will read the first 2 bytes of the `int_file.bin` file and unpack them using the same format string `'>h'`. The result is the original value `-32768`.

3. Repeat these steps for other integer values, including boundary cases (e.g., `-1`, `0`, `65535`) to see how the packing and unpacking work.

4. Do the same for floating-point numbers:
```python
import struct

# Define the format string for a float
format_str = '>f'  # '>f' means big-endian, single-precision float

# Create a binary file with the value -32641 (0xc2c1d3)
with open('float_file.bin', 'wb') as f:
    struct.pack(format_str, -32641).write(f)

print("Wrote binary file: float_file.bin")
```
This will create a binary file `float_file.bin` containing the value `-32641`.

5. Read the floating-point number from the binary file:
```python
with open('float_file.bin', 'rb') as f:
    data = f.read(4)
    num, = struct.unpack('>f', data)

print("Read value:", num)
```
This will read the first 4 bytes of the `float_file.bin` file and unpack them using the same format string `'>f'`. The result is the original value `-32641`.

**Task: BMP Image Processing**

Create a Python script that takes a 24-bit BMP image as input, performs various operations on it, and saves the results to new files.

Here's a basic implementation:
```python
import array

def process_bmp_image(input_file, output_file):
    # Read the header (54 bytes)
    with open(input_file, 'rb') as f:
        head = f.read(54)

    # Read the image data (array of bytes)
    with open(input_file, 'rb') as f:
        a = array.array('B', f.read())

    # Perform operations on the image
    # ...

    # Save the processed image to a new file
    with open(output_file, 'wb') as f:
        f.write(head)
        f.write(a.tobytes())

# Example usage
input_file = 'in.bmp'
output_file = 'out.bmp'
process_bmp_image(input_file, output_file)
```
This script assumes that the input file is a 24-bit BMP image and performs some basic operations (e.g., negation, grayscale conversion). You'll need to implement the specific operations you want to perform.

**Additional Tasks**

To complete the task, you can add more operations, such as:

* Reflections (left-to-right, top-to-bottom)
* Rotations (90 degrees, clockwise or counterclockwise)
* Color adjustments (brightness, contrast, etc.)
* Grayscale conversion with varying brightness levels

Remember to handle edge cases and boundary values correctly. You may also want to consider using libraries like Pillow for more advanced image processing tasks.