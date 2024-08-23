import SimpleITK as sitk

# DICOM dizinini belirtin
dicom_directory = "path_to_dicom_directory"

# DICOM serisini okuma
reader = sitk.ImageSeriesReader()
dicom_filenames = reader.GetGDCMSeriesFileNames(dicom_directory)
reader.SetFileNames(dicom_filenames)

# Görüntüyü okuma
image = reader.Execute()

# Görüntü özelliklerini alma
size = image.GetSize()
spacing = image.GetSpacing()
direction = image.GetDirection()

print(f"Boyut: {size}")
print(f"Çözünürlük: {spacing}")
print(f"Yönlendirme: {direction}")

# Görüntüyü array formatında almak için
image_array = sitk.GetArrayFromImage(image)

# Örneğin, görüntünün ilk dilimini gösterme
import matplotlib.pyplot as plt
plt.imshow(image_array[0], cmap='gray')
plt.show()
