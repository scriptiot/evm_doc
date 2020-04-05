## 1. 虚拟机类型判断API

---

### 1.1 判断evm_val_t对象是否为数字

```c
int evm_is_number(evm_val_t *v)

```

### 1.2 判断evm_val_t对象是否为整数

```c
int evm_is_integer(evm_val_t *v)

```

### 1.3 判断evm_val_t对象是否为堆字符串

```c
int evm_is_heap_string(evm_val_t *v)

```

### 1.4 判断evm_val_t对象是否为外部字符串

```c
int evm_is_foreign_string(evm_val_t *v)

```

### 1.5 判断evm_val_t对象是否为字符串

```c
int evm_is_string(evm_val_t *v)

```

### 1.6 判断evm_val_t对象是否为布尔值

```c
int evm_is_boolean(evm_val_t *v)

```

### 1.7 判断evm_val_t对象是否为字符数组

```c
int evm_is_buffer(evm_val_t *v)

```

### 1.8 判断evm_val_t对象是否为脚本函数

```c
int evm_is_script(evm_val_t *v)

```

### 1.9 判断evm_val_t对象是否为内置函数

```c
int evm_is_native(evm_val_t *v)

```

### 1.10 判断evm_val_t对象是否为数组、列表

```c
int evm_is_list(evm_val_t *v)

```

### 1.11 判断evm_val_t对象是否为外部指针

```c
int evm_is_foreign(evm_val_t *v)

```


### 1.12 判断evm_val_t对象是否为函数

```c
int evm_is_function(evm_val_t *v)

```

### 1.13 判断evm_val_t对象是否为undefined

```c
int evm_is_undefined(evm_val_t *v)

```

### 1.14 判断evm_val_t对象是否为空

```c
int evm_is_null(evm_val_t *v)

```

### 1.15 判断evm_val_t对象是否为NaN

```c
int evm_is_nan(evm_val_t *v)

```

### 1.16 判断evm_val_t对象是否为对象

```c
int evm_is_object(evm_val_t *v)

```

### 1.17 判断evm_val_t对象是否为类

```c
int evm_is_class(evm_val_t *v)

```