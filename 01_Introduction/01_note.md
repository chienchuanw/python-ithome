# Day 1 - 入門概論

## Environment Setup

檢查目前安裝的 Python 版本  

```py
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

### 註解 comment 的意義

註解 comment 顧名思義即是「針對某段的原始碼進行補充與備註，而這段原始碼也**不會**被 Python 執行」。  
通常我們會使用註解解釋某段原始碼的用途，日後我們或是其他人在閱讀這段原始碼的時候，可以更輕鬆地瞭解原始碼的意義。  
同樣地，我們也可以利用「註解段落不會被 Python 執行」的特型，讓 Python 在執行時刻意地跳過某段程式碼，進而改變執行後所得到的結果。  

```py
 # comment starts with hash
 # this is a python comment, because it starts with a (#) symbol
```

## 基礎 Python

