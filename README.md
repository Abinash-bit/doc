# Document Layout Analysis.

In this project, I have implemented a comprehensive document layout analysis tool that utilizes PaddleOCR to analyze the structure of document images. The functionality includes detecting the image orientation, enabling proper adjustment for further processing. Additionally, the system accurately recognizes tables within the document, extracting relevant data with high precision. Beyond table detection, the tool performs detailed layout analysis, identifying text blocks, images, and other elements in the document, making it easier to interpret and process complex multi-element documents. This tool streamlines document digitization, enhancing efficiency and accuracy in information extraction.






<a name="1"></a>
## 1. Environment Preparation
### 1.1 Install PaddlePaddle

> If you do not have a Python environment, please refer to [Environment Preparation](./environment_en.md).

- If you have CUDA 9 or CUDA 10 installed on your machine, please run the following command to install

  ```bash
  python3 -m pip install paddlepaddle-gpu -i https://mirror.baidu.com/pypi/simple
  ```

- If you have no available GPU on your machine, please run the following command to install the CPU version

  ```bash
  python3 -m pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple
  ```

For more software version requirements, please refer to the instructions in [Installation Document](https://www.paddlepaddle.org.cn/install/quick) for operation.

### 1.2 Install PaddleOCR Whl Package

```bash
# Install paddleocr, version 2.6 is recommended
pip3 install "paddleocr>=2.6.0.3"

# Install the image direction classification dependency package paddleclas (if you do not use the image direction classification, you can skip it)
pip3 install paddleclas>=2.4.3
```
