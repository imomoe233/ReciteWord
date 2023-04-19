import win32gui
import win32con

class TaskbarWindow:
    def __init__(self, text):
        # 创建一个窗口
        self.hwnd = win32gui.CreateWindowEx(
            win32con.WS_EX_TOOLWINDOW, # 避免出现任务栏按钮
            win32gui.GetClassName(win32gui.GetDesktopWindow()),
            "", # 标题为空
            win32con.WS_POPUP, # 弹出式窗口
            0, 0, 10, 10, # 位置和大小为 0
            None, None, 0, None
        )

        # 将窗口嵌入任务栏
        win32gui.SetWindowLong(self.hwnd, win32con.GWL_EXSTYLE,
                               win32gui.GetWindowLong(self.hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_TOOLWINDOW)
        win32gui.SetWindowPos(self.hwnd, win32con.HWND_TOPMOST, 10, 10, 10, 10,
                              win32con.SWP_NOACTIVATE | win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_SHOWWINDOW)

        # 在窗口上显示文本
        self.text = text
        self.draw_text()

    def draw_text(self):
        hdc = win32gui.GetDC(self.hwnd)
        rect = win32gui.GetClientRect(self.hwnd)
        win32gui.SetBkMode(hdc, win32con.TRANSPARENT)
        win32gui.DrawText(hdc, self.text, -1, rect,
                          win32con.DT_SINGLELINE | win32con.DT_CENTER | win32con.DT_VCENTER | win32con.DT_NOPREFIX)
        win32gui.ReleaseDC(self.hwnd, hdc)

    def run(self):
        # 显示窗口
        win32gui.ShowWindow(self.hwnd, win32con.SW_SHOWNOACTIVATE)

        # 处理消息循环
        while True:
            win32gui.PumpWaitingMessages()

window = TaskbarWindow("Hello, World!")
window.run()
