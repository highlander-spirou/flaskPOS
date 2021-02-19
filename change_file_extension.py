from file_template import get_file_template_dir
import shutil

file_dir = get_file_template_dir()

my_file = file_dir + '/runVBA.txt'

def create_src_code(variable_name, module_name, is_korea=True):

    if is_korea:
        k = "TO_KOREA"
    else:
        k= ""
    code_src = r"""
    Option Explicit

    On Error Resume Next

    ExcelMacroExample

    Sub ExcelMacroExample() 

    Dim xlApp 
    Dim xlBook 

    Set xlApp = CreateObject("Excel.Application") 
    Set xlBook = xlApp.Workbooks.Open("C:\Users\LETPC\Nhan\FlaskPOS\file_template\created_file\WORLD-MNF-{variable_name}{k}.xlsm", 0, True) 
    xlApp.Run "{module_name}"
    xlApp.Quit 

    Set xlBook = Nothing 
    Set xlApp = Nothing 

    End Sub 
    """
    code_src = code_src.format(variable_name=variable_name, k=k, module_name=module_name)

    return code_src


def write_src(my_file, code_src, name):
    with open(my_file, "w") as t:
        t.write(code_src)

    target = file_dir + f"/created_file/{name}.vbs"
    shutil.copyfile(my_file, target)




#### CODE INSTRUCTION

# variable_name = "2021-02-19"
# module_name_1 = "file1"
# module_name_2 = "file2"

# code_src_1 = create_src_code(variable_name, module_name_1, False)
# code_src_2 = create_src_code(variable_name, module_name_2)

# write_src(my_file, code_src_1, "VBA_1")
# write_src(my_file, code_src_2, "VBA_2")