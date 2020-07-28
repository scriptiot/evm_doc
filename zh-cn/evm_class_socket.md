## class Socket – 套接字

### 构造函数

` class evm.Socket()`
 创建一个Socket对象。

### 对象函数
`Socket.socket(af, type, proto)`
设置回调函数及定时周期。
* af: 指定地址族，对于TCP/IP协议的套接字，它只能是AF_INET
* type: 指定Socket类型，对于1.1版本的Socket，他只支持两种类型的套接字：SOCKE_STREAM指定产生流式套接字，SOCK_DGRAM产生数据报套接字
* proto: 指定地址家族相关的协议，如果指定为0，那么系统就会根据地址格式和套接类别，自动选择一个合适的协议

`Socket.close()`
关闭套接字。

`Socket.bind(ip, port)`
* ip: IP地址
* port: Port端口号
绑定IP和Port

`Socket.connect(address)`
* address: 服务器地址
连接host。

`Socket.listen([backlog])`
监听端口。

`Socket.accept()`
接收连接请求。

`Socket.send(bytes|string)`
发送数据。

`Socket.recv(bufsize)`
接收数据。

`Socket.sendto(bytes, address)`
发送数据指定地址。

`Socket.recvfrom(bufsize)`
接收数据。

`Socket.setsockopt(level, optname, value)`
获取套接字选项。

`Socket.getaddrinfo(level, optname, value)`
返回值：[(family, socktype, proto, canonname, sockaddr)]有元组组成的列表，元组里面包含5个元素，其中sockaddr是(host, port)。

`Socket.inet_pton(af, txt_addr)`
将字符串转换到网络地址，第一个参数af是地址族，第二个参数是点分十进制的字符串。

`Socket.inet_ntop(af, bin_addr)`
将网络二进制结构转换到ASCII类型的地址，参数的作用和上面相同。

### 使用方法
```javascript
var m = require('evm')
var s = new m.Socket()
```
