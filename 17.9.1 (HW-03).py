def qsort(array, left, right):
    middle = (left + right) // 2
    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)


def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


while True:
    try:
        s = input('Введите последовательность чисел через пробел:\n')
        element = input('Введите элемент:\n')
        st = s + ' ' + element  # добавляю элемент к первой последовательности, чтобы он точно был в списке
        array = list(map(int, st.split()))
        break
    except:
        print('Введенные символы не соответствуют условию. Повторите ввод.')


element = int(element)
qsort(array, 0, len(array) - 1)
index = binary_search(array, element, 0, len(array) - 1)
if index > 0:
    print(f'Предыдущй элемент {index - 1} по счету')
else:
    print('Предыдущего элемента не существует')
array.pop(index)  # удаляю вставленный элемент
print('Отсортированный список:', array)