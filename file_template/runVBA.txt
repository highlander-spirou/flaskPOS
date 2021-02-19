
    Option Explicit

    On Error Resume Next

    ExcelMacroExample

    Sub ExcelMacroExample() 

    Dim xlApp 
    Dim xlBook 

    Set xlApp = CreateObject("Excel.Application") 
    Set xlBook = xlApp.Workbooks.Open("C:\Users\LETPC\Nhan\FlaskPOS\file_template\created_file\WORLD-MNF-2021-02-19TO_KOREA.xlsm", 0, True) 
    xlApp.Run "file2"
    xlApp.Quit 

    Set xlBook = Nothing 
    Set xlApp = Nothing 

    End Sub 
    