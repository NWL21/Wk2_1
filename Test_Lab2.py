import Wk2_3
import subprocess

def test_get_user_input():
    # p = subprocess.Popen(['python', 'Test_Lab2.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    # buffer_arr = "1,9"
    # buffer_b = buffer_arr.encode("ascii")
    # p.stdin.write(buffer_b)
    result_arr = Wk2_3.get_user_input("1,9")

    assert (result_arr[0] == 1 and result_arr[1] == 9)
def test_calc_average():
    input_arr = [5,3,4,2,1,0]
    result = Wk2_3.calc_average_temperature(input_arr)

    assert (result == 2.5)
