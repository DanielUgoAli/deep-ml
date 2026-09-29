import numpy as np

def calculate_brightness(img):
    if img is None:
        return -1

    try:
        # Convert to a numpy array, forcing float type
        img_arr = np.asarray(img, dtype=float)
    except (ValueError, TypeError):
        return -1
    
    # Check if the array is empty or if it became an object array (due to jagged rows)
    if img_arr.size == 0 or img_arr.dtype == object:
        return -1
        
    # Check for invalid pixel values outside the standard 0-255 range
    if np.any(img_arr < 0) or np.any(img_arr > 255):
        return -1
        
    return float(np.mean(img_arr))

# Test invalid pixel values
print(calculate_brightness([[100, 300]]))  # Now correctly returns -1