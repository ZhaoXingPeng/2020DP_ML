# 图像处理工具类
from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter("logs")
# writer.add_image()
for i in range(100):
    # 第一个参数是标题
    writer.add_scalar("y=x", i, i)
    writer.add_scalar("y=2x", i*2, i)
# 打开logs生成的文件 tensorboard --logdir=logs --port=6007 指定端口 控制台打开
writer.close()
