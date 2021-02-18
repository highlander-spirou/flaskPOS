from subprocess import Popen, PIPE, STDOUT


command1= "python"
command2 = "weblogic.py"
input1 = "a"
input2 = "b"
input3 = "c"
input4 = "d"
input_string = f'{input1}\n{input2}\n{input3}\n{input4}\n'.encode()
args = [command1,command2]

proc = Popen(args, stdout=PIPE, stdin=PIPE, stderr=STDOUT, shell=True)
grep_stdout = proc.communicate(input=input_string)[0]
print(grep_stdout.decode())