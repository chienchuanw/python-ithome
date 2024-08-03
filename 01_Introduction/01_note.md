# Day 1 - 入門概論

## Environment Setup

檢查目前安裝的 Python 版本  

```console
python --version
```

使用指令開啟 Python Interactive shell

```console
python
```

關閉並離開 Python Interactive Shell，也可以使用 `ctrl + d`

```python
exit()
```

### 常見的錯誤類型 Error Types

如果執行的內容有錯誤，Python 會顯示相關的錯誤 (Error) 訊息內容，因此可以多瞭解常見的 Python 錯誤訊息類型，常見的**Error Types 錯誤類型**有：

- `SyntaxError`  

    ```py
    # SyntaxError: Missing colon after if statement
    if True
    print("This will cause a SyntaxError")
    ```

- `IndexError`

    ```py
    # IndexError: Trying to access an index that doesn't exist
    my_list = [1, 2, 3]
    print(my_list[3])
    ```

- `NameError`  

    ```py
    # NameError: Using a variable that hasn't been defined
    print(non_existent_variable)
    ```

- `ModuleNotFoundError`  

    ```py
    # ModuleNotFoundError: Trying to import a module that doesn't exist
    import non_existent_module
    ```

- `KeyError`  

    ```py
    # KeyError: Accessing a non-existent key in a dictionary
    my_dict = {"a": 1, "b": 2}
    print(my_dict["c"])
    ```

- `ImportError`  

    ```py
    # ImportError: Importing a non-existent name from a module
    from math import non_existent_function
    ```

- `AttributeError`  

    ```py
    # AttributeError: Accessing a non-existent attribute of an object
    my_list = [1, 2, 3]
    my_list.non_existent_method()
    ```

- `TypeError`  

    ```py
    # TypeError: Performing an operation on incompatible types
    print("String" + 5)
    ```

- `ValueError`  

    ```py
    # ValueError: Passing an invalid value to a function
    int("not_a_number")
    ```

- `ZeroDivisionError`  

    ```py
    # ZeroDivisionError: Dividing a number by zero
    print(10 / 0)
    ```

為什麼需要瞭解這些 Error Types 呢？  
因為透過這些 Error Types 的訊息內容，我們可以更快得知程式碼中的錯誤原因，並根據其內容進行除錯（Debug），節省一步步偵查、測試的時間。  

### 常見的運算子 Operator

除了一般的加減乘除，在 Python 中常見的運算子還有平方 `**`、餘數 `%`、商數 `\\`。  

```py
print(2 + 3)    # 5
print(3 - 1)    # 2
print(3 * 2)    # 6
print(3 / 2)    # 1.5
print(3 ** 2)   # 9
print(11 % 3)   # 2
print(11 // 3)  # 1
```

## 基礎 Python 知識

- Python 的檔案名稱會以 `.py` 的副檔名結尾。  

### 縮排 indentation 的重要性

縮排指的是「在每一行的開頭，新增指定次數的空白鍵」，因為在許多程式語言中，正確的縮排可以大幅增加程式碼的可閱讀性，而這一點在 Python 中尤其重要，因為 Python 是透過縮排來辨別各區塊的程式碼，剛開始學習 Python 時，時常會因為縮排錯誤導致程式碼執行後發生錯誤，但隨著對於 Python 的熟悉與 IDE 擴充程式的協助，不知不覺會下意識地進行縮排，依照 Python 的慣例————「使用 4 個空白鍵作為縮排」。  

```py

print("hello world")

def greeting(text):
    # 由於我們希望這邊的內容是 def greeting(text) 的一部分，所以要進行縮排。
    print("hi, how are you?")
    print("I am fine.")

# 這邊則希望開始編寫其他獨立於 def greeting(text) 的其他內容，所以不需要縮排，直接從頭開始編寫。
print("this is a new beginning.")
```

### 註解 comment 的意義

註解 comment 顧名思義即是「針對某段的原始碼進行補充與備註，而這段原始碼也**不會**被 Python 執行」。  
通常我們會使用註解解釋某段原始碼的用途，日後我們或是其他人在閱讀這段原始碼的時候，可以更輕鬆地瞭解原始碼的意義。  
同樣地，我們也可以利用「註解段落不會被 Python 執行」的特型，讓 Python 在執行時刻意地跳過某段程式碼，進而改變執行後所得到的結果。  

我們可以使用 `#` 井字號達到註解單行程式碼的效果，同時依照慣例，我們會在 `#` 後面空一格，才開始編寫想要輸入的註解內容。

```py
 # comment starts with hash
 # this is a python comment, because it starts with a (#) symbol
```

我們也可以透過 `"""` （三個引號）達到多行註解的效果。

```py
"""
上面三個引號，代表是註解的開始。

註解註解註解註解註解註解註解註解
多行註解有開始，就要有結束。

下面三個引號，代表是註解的結束。
"""
```

### 有哪些資料類型 Data Types

Python 中，不同的資料種類有不同的負責內容與運算規則，下面是幾種常見的資料類型（Data Types）：

**String 字串**  
`String` 字串應該是 Python 中最常見到的資料種類，當我們想要表達一個字詞時，我們可以使用「單引號或是雙引號」表示這是一個字串。

```py
"這是使用雙引號的字串"
'這是使用雙引號的字串'
'不可以單引號開始，雙引號結束！"
```

**Number 數字**  
除了字串，在 Python 中第二常見的資料類型就屬 `Number` 數字了，數字的又可以再細分成：

- `Integer` 整數：包含正整數、負整數、零。
- `Float` 浮點數：代表的帶有小數的數值。
- `Complex` 複數：由實部與虛部所組成的數字類型。

```py
123     # 這是 Integer 整數
9.1     # 這是 Float 小數
2 + 4j  # 這是 Complex 複數
```

> 請問以下分別是哪種資料類型呢？  

1. "132"
2. 1.0
3. -3
4. 0.0

> 答案

1. `String` 字串
2. `Float` 浮點數
3. `Integer` 整數
4. `Float` 浮點數

**Boolean 布林值**  
`Boolean` 布林值又可稱作「真假值」，因為布林值只有 `True` 跟 `False`，如果不是真的，那就一定是假的，沒有曖昧的存在。

```py
True    # 真的，記得 T 要大寫
False   # 假的，記得 F 要大寫
```

**List 串列**  

**Dictionary 字典**  

**Tuple 元組**  
A tuple is an ordered collection of different data types like list but tuples can not be modified once they are created. They are immutable.  

**Set 集合**  
A set is a collection of data types similar to list and tuple. Unlike list and tuple, set is not an ordered collection of items. Like in Mathematics, set in Python stores only unique items.  

### 如何檢查資料類型

使用 `type` function

```py
type("hello")       # str
type(10)            # int
type(3.14)          # float
type(1 + 3j)        # complex
type([1, 2, "abc"]) # list
type({"age": 18})   # dict
type((2, 4, "go",)) # tuple
type({0.5, 3, 10})  # set
```

## 練習題

### 基礎題

1. Check the python version you are using
2. Open the python interactive shell and do the following operations. The operands are 3 and 4.  
   - addition(`+`)
   - subtraction(`-`)
   - multiplication(`*`)
   - modulus(`%`)
   - division(`/`)
   - exponential(`**`)
   - floor division operator(`//`)
  
3. Write strings on the python interactive shell. The strings are the following:  
    - Your name
    - Your family name
    - Your country
    - I am enjoying 30 days of python

4. Check the data types of the following data:  
    - 10
    - 9.8
    - 3.14
    - 4 - 4j
    - ['Frank', 'Python', 'Finland']
    - Your name
    - Your family name
    - Your country

### 進階題

Create a folder named day_1 inside 30DaysOfPython folder. Inside day_1 folder, create a python file `hello_world.py` and repeat questions 1, 2, 3 and 4. Remember to use `print()` when you are working on a python file. Navigate to the directory where you have saved your file, and run it.  

### 高階題

1. Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.  

    ```py
    print(type(1))
    print(type(2.0))
    print(type(3 + 4j))
    print(type("Hello"))
    print(type(True))
    print(type(["a", "b", "c"]))
    print(type((5, 6, 7)))
    print(type({"andy", "james", "taylor"}))
    print(type({"name": "Frank", "age": 18}))
    ```

2. Find an Euclidian distance between (2, 3) and (10, 8)  

    ```py
    import math
    distance = math.sqrt(((10 - 2)) ** 2 + ((8 - 3)) ** 2) 
    print(distance)
    ```

    或是

    ```py
    import math
    # Define coordinate
    x1, y1 = 2, 3
    x2, y2 = 10, 8

    # Calculate distance between two coordinates
    distance - math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    ```
