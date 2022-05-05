import Wk2_3
from pyautogui import press, typewrite, hotkey
def test_get_user_input():
    input_str = "1,2,6,7,9,3"
    assert (Wk2_3.get_user_input(input_str) == [1,2,6,7,9,3])
def test_calc_average():
    input_arr = [5,3,4,2,1,0]
    result = Wk2_3.calc_average_temperature(input_arr)

    assert (result == 2.5)
