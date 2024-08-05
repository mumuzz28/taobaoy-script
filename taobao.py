import uiautomator2 as u2
import time

# 连接到设备
device = u2.connect("192.168.0.231")

# 获取当前界面信息
for i in range(1,5):

    print(f"第{i}个任务开始")
    device.dump_hierarchy()

    # 点击活动页面
    x = 950
    y = 1990
    # 等待界面加载完成
    time.sleep(3)
    # 等待界面加载完成

    if device(text="去入会").exists:
        while device(text="去入会").exists:
            print("去入会任务开始")
            device(text="去入会").click()
            time.sleep(2)
            device.dump_hierarchy()
            if device(description="下一步").exists:
                time.sleep(2)
                device(description="下一步").click()
                time.sleep(2)
            device(description="授权同意").click()
            print("点击授权同意")
            time.sleep(2)
            if device(description="开通会员").exists:
                device(description="开通会员").click()
                print("点击开通会员")
            elif device(description="开通品牌会员").exists:
                device(description="开通品牌会员").click()
                print("点击开通品牌会员")
            else:
                device(description="接受入会邀请").click()
                print("接受入会邀请")
            time.sleep(2)
            device.press("back")
            time.sleep(2)
            print("去入会任务完成")
            device.click(x, y)
            time.sleep(3)

    # 浏览李宁旗舰店
    if device(text="浏览李宁旗舰店").exists:
        print("浏览李宁旗舰店")
        if device(text="去浏览").exists:
            device(text="去浏览").click()
        if device(text="去完成").exists:
            device(text="去完成").click()
        time.sleep(15)
        device.press("back")
        time.sleep(5)
        print("浏览李宁旗舰店")
    # 浏览李宁旗舰店
    if device(text="浏览美的旗舰店").exists:
        print("浏览美的旗舰店")
        device(text="去完成").click()
        time.sleep(15)
        device.press("back")
        time.sleep(5)
        print("浏览美的旗舰店")

    if device(text="去完成").exists:
        count = device(text="去完成").count
        print(f"去浏览任务{count}个")
        for i in range(count):
            time.sleep(2)
            print(f"浏览任务{i + 1}开始")
            device(text="去完成").click()
            time.sleep(3)
            if device(text="立即参赛").exists:
                print("点击参赛按钮")
                device(text="立即参赛", index=3).click()
            # # 去蚂蚁森林收能量
            # if device(text="去蚂蚁森林收能量").exists:
            #     print("去蚂蚁森林收能量")
            #     device(text="去蚂蚁森林收能量").click()
            #     time.sleep(2)
            #     device.press("back")
            #     continue
            time.sleep(2)
            device.swipe(550, 1800, 800, 550, 0.5)
            time.sleep(12)
            device.press("back")
            time.sleep(3)
            print(f"浏览任务{i + 1}完成！")

    if device(text="去领取").exists:
        print("去领取任务开始")
        device(text="去领取").click()
        time.sleep(2)

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
            device.click(57, 190)
            time.sleep(2)
            device.press("back")
            time.sleep(2)
            device.click(x, y)
            time.sleep(3)
            if device(text="去领取").exists:
                time.sleep(2)
                device(text="去领取").click()
                print("参与今日赛事活动完成")
    # 去运动
    if device(text="去运动").exists:
        device(text="去运动").click()
        print("去运动任务开始")
        time.sleep(2)
        if device(text="立即参赛").exists:
            print("点击参赛按钮")
            device(text="立即参赛", index=3).click()
            time.sleep(5)
            if device(text="开始运动").exists:
                time.sleep(3)
                device(text="开始运动").click()
                time.sleep(5)
                device(text="暂停走路").click()
        time.sleep(2)
        device.press("back")
        time.sleep(3)
        device.click(x, y)
        time.sleep(5)
        if device(text="去领取").exists:
            time.sleep(2)
            device(text="去领取").click()


    print(f"第{i}个任务结束")
    time.sleep(5)
