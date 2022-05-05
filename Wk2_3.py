def display_main_menu():
    print("Enter some numbers seperated by commas : ")
def get_user_input(tempbuffer):
    n = 0
    if tempbuffer == '\0':
        tempbuffer = str(input())
    nums = tempbuffer.split(",")
    for number in nums:
        nums[n] = float(number)
        n += 1
    return nums
def calc_average_temperature(list):
    total = 0
    for num in list:
        total += num
    average = total/len(list)
    return average
def calc_min_max_temperature(list):
    minmax = [list[0], list[0]]
    for num in list:
        if num < minmax[0]:
            minmax[0] = num
        elif num > minmax[1]:
            minmax[1] = num
    return minmax
def sort_temperature(list):
    sortedlist = sorted(list)
    return sortedlist
def calc_median_temperature(list):
    sortedlist = sorted(list)
    i = len(list)/2
    if len(list)%2 == 0:
        #print(str(list[int(i - 1)]) + ", " + str(list[int(i)]))
        median = (sortedlist[int(i - 1)] + sortedlist[int(i)]) / 2
        print("1")
        return median
    else:
        print("2")
        return sortedlist[int(i - 0.5)]
def main():
    a = 2
    print(f"hi {a} ppl")
    print(hex(11))
    display_main_menu()
    num_list = get_user_input('\0')
    minmax = calc_min_max_temperature(num_list)
    print(str(num_list))
    print(str(type(num_list[0])))
    print("The average of the temperatures given is : " + str(calc_average_temperature(num_list)) + " degrees")
    print("The lowest temperature is : " + str(minmax[0]) + " degrees. The highest temperature is : " + str(minmax[1]) + " degrees")
    print("The temperatures in ascending order is " + str(sort_temperature(num_list)))
    print("The median temperature is : " + str(calc_median_temperature(num_list)))

if __name__ == "__main__":
    main()