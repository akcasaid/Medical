import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt

def load_dicom_series(directory):
    """DICOM serisini yükleyip SimpleITK görüntüsü olarak döndür."""
    reader = sitk.ImageSeriesReader()
    dicom_names = reader.GetGDCMSeriesFileNames(directory)
    reader.SetFileNames(dicom_names)
    image = reader.Execute()
    return image

def normalize_image(image):
    """Görüntünün yoğunluğunu normalleştir."""
    arr = sitk.GetArrayFromImage(image)
    normalized_arr = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))
    return sitk.GetImageFromArray(normalized_arr)

def segment_brain(image):
    """Beyin dokusunu segmente etmek için basit bir eşikleme yöntemi kullan."""
    otsu_filter = sitk.OtsuThresholdImageFilter()
    otsu_filter.SetInsideValue(0)
    otsu_filter.SetOutsideValue(1)
    segmented = otsu_filter.Execute(image)
    return segmented

# DICOM dizinini belirt
dicom_directory = 'path/to/your/dicom/folder'

# DICOM serisini yükle
dicom_image = load_dicom_series(dicom_directory)

# Görüntüyü normalleştir
normalized_image = normalize_image(dicom_image)

# Beyin dokusunu segmente et
segmented_image = segment_brain(normalized_image)

# Sonuçları görselleştir
fig, axs = plt.subplots(1, 3, figsize=(15, 5))
axs[0].imshow(sitk.GetArrayFromImage(dicom_image)[dicom_image.GetDepth() // 2], cmap='gray')
axs[0].set_title('Original DICOM Image')
axs[1].imshow(sitk.GetArrayFromImage(normalized_image)[normalized_image.GetDepth() // 2], cmap='gray')
axs[1].set_title('Normalized Image')
axs[2].imshow(sitk.GetArrayFromImage(segmented_image)[segmented_image.GetDepth() // 2], cmap='gray')
axs[2].set_title('Segmented Image')
for ax in axs:
    ax.axis('off')
plt.show()
