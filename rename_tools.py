import os
from datetime import datetime
def file_rename():
    print('功能：对输入的文件类型进行更名')
    print('方法：输入要更改的文件类型如“jpg - txt - xlsx”')
    print('再输入要批量更名的名称，如‘学校、生活、工资表’会自动序号生成‘学校-1.jpg、学校-2.jpg、学校-3.jpg等')
    path = os.getcwd()
    file_class = input('请输入要更名的文件类型（jpg - txt - xlsx）')
    re_file_name = input('请输入要设定的名称：')
    if file_class is None or re_file_name is None:
        print("文件名或格式类型不能为空。")
        file_class = input('请输入要更名的文件类型（jpg - txt - xlsx）')
        re_file_name = input('请输入要设定的名称：')
    file_list = os.listdir(path)
    print(file_list)
    n = 1
    for name in file_list:
        if name.endswith(f'.{file_class}'):
            newname = f'{re_file_name}-{n}.{file_class}'
            os.rename(name,f'{re_file_name}-{n}.{file_class}')
            n += 1
            date = datetime.now().date().strftime('%Y%m%d')
            with open(f"./{date}.log",'a',encoding='utf-8')as f:
                f.write(f"{date}--旧名字{name},更新成{newname} \n")
        else:
            with open(f"./{date}.log",'a',encoding='utf-8')as f:
                f.write(f"{name}不是{file_class}格式。 \n")
            
if __name__ == "__main__":
    file_rename()