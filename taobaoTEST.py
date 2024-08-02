import uiautomator2 as u2
import time

# 连接到设备
device = u2.connect()

# 获取当前界面信息
device.dump_hierarchy()

# 点击活动页面
x = 950
y = 1990
# 等待界面加载完成
time.sleep(3)
# 等待界面加载完成
# 参与今日赛事
if device(text="参与今日赛事").exists:
    print("参与今日赛事")
    time.sleep(2)
    device(text="去运动").click()
    time.sleep(2)
    device(text="立即参赛", index=2).click()
    time.sleep(5)
    if device(text="立即开始运动").exists:
        time.sleep(3)
        device(text="立即开始运动").click()
        time.sleep(3)
        print("点击立即开始运动")
        device.click(57,190)
        time.sleep(2)
        device.press("back")
        time.sleep(2)
        device.click(x,y)
        time.sleep(3)
        if device(text="去领取").exists:
            time.sleep(2)
            device(text="去领取").click()
            print("参与今日赛事活动完成")