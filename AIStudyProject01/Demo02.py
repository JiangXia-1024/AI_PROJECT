# 图画转铅笔画案例
import gradio as gr
import cv2
import numpy as np

# 功能实现
def pencil_sketch(image):
     # 转换为灰度图
    gray_image = image.convert('L')
    inverted_image = 255 - np.array(gray_image)
    blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    inverted_blurred_image = 255 - blurred_image
    pencil_sketch = cv2.divide(np.array(gray_image), inverted_blurred_image, scale=256.0)
    # 创建粉色底色
    height, width = pencil_sketch.shape
    pink_background = np.zeros((height, width, 3), dtype=np.uint8)
    pink_background[:] = (147, 112, 219)  # RGB: 219, 112, 147 粉色
    
    # 将灰度铅笔画与粉色底色混合
    # 将灰度图转换为三通道
    pencil_sketch_rgb = cv2.cvtColor(pencil_sketch.astype(np.uint8), cv2.COLOR_GRAY2BGR)
    # 混合：使用灰度图作为权重，控制粉色的强度
    pink_effect = cv2.addWeighted(pencil_sketch_rgb, 0.3, pink_background, 0.7, 0)
    
    return pink_effect

    # 参数：
    # fn：要执行的函数
    # inputs：输入类型，这里为图片输入框
    # outputs：输出类型，这里为图片输出框
demo = gr.Interface(
        fn=pencil_sketch, 
        inputs=[gr.Image(label="上传图片",type="pil")], 
        outputs=[gr.Image(label='铅笔画')],
        title = "图片转铅笔画",
        description = "上传图片，返回对应的铅笔画效果")
#04、启动应用
demo.launch(share=True)