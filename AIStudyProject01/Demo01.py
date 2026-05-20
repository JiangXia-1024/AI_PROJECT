# 案例01 ：gradio 学习
# 01、导入gradio库
import gradio as gr

#02、定义一个函数，用于反转文本
def reverse_text(text):
    reversed_text = text[::-1]
    print(reversed_text)
    return reversed_text

#03、创建一个gradio界面
# 参数：
# fn：要执行的函数
# inputs：输入类型，这里为文本输入框
# outputs：输出类型，这里为文本输出框
demo = gr.Interface(
    fn=reverse_text, 
    inputs="text", 
    outputs="text")

#04、启动应用
demo.launch(share=True)
