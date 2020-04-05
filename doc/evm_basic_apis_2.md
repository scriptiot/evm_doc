## 2.虚拟机类型转换API

---

### 2.1 evm_val_t数字对象是转浮点

```c
double evm_2_double(evm_val_t *v)

```

### 2.2 evm_val_t数字对象是转整数

```c
double evm_2_integer(evm_val_t *v)

```

### 2.3 evm_val_t对象是转布尔

```c
int evm_2_boolean(evm_val_t *v)

```

### 2.3 evm_val_t对象是转字符串

```c
const char *evm_2_string(evm_val_t *v);

```

### 2.4 evm_val_t数字对象是转指针

```c
intptr_t evm_2_intptr(evm_val_t *v)
