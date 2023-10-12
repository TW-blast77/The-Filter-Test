# 圖像濾鏡示範

這是一個使用均值濾鏡和中值濾鏡處理圖像的示範代碼。它展示了如何讀取一張圖像、添加噪音，然後使用兩種不同的濾鏡方法進行圖像處理。

## 依賴

- Python 3.x
- OpenCV (cv2)
- NumPy

你可以使用以下命令來安裝所需的Python庫：

```bash
pip install opencv-python-headless numpy

**如何使用**

準備一張圖像並保存到指定的路徑。確保已經建立了./photo/output-photo/noise-photo目錄，以便存儲噪音圖像。

運行add_noise.py以添加隨機噪音到圖像：

```bash
python add_noise.py

運行filter_images.py來應用均值濾鏡和中值濾鏡：
```bash
python filter_images.py

處理後的圖像將保存在./photo/output-photo/Mean-photo和./photo/output-photo/Meadian-photo目錄下。

**文件說明**
add_noise.py：添加隨機噪音到圖像並保存。
filter_images.py：使用均值濾鏡和中值濾鏡處理圖像。
./photo/origin-photo/Lenna.png：原始圖像文件。
./photo/output-photo/noise-photo：用於存儲噪音圖像的目錄。
./photo/output-photo/Mean-photo：用於存儲均值濾鏡後圖像的目錄。
./photo/output-photo/Meadian-photo：用於存儲中值濾鏡後圖像的目錄。

**注意事項**

請確保已經準備好原始圖像，並且相關目錄已經建立。
你可以根據需要調整濾鏡的參數，例如k值，以控制濾鏡的大小。
在運行代碼前，確保已安裝所需的Python庫。
如果你有任何問題或疑問，歡迎隨時聯絡我。


請根據實際情況調整文件路徑和其他細節。這個README文件將提供有關你的代碼如何運作和如何運行的重要信息。
