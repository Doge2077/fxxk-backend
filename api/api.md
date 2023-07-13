### 登录

post传参

```
http://127.0.0.1:8000/login/login/
```

```json
{
    "username":"123",
	"password":"123"
}
```

成功回传登陆成功标识符和token

```json
{
	"token": key,
	"success": "login successfully"
}
```

失败回传失败标识符

```json
{
	"error": "not registered"
}
```

### 注册

post传参

```
http://127.0.0.1:8000/login/register/
```

```json
{
    "username":"123",
	"password":"123"
}
```

成功回传注册成功标识符和token

```json
{
	"token": hash_code,
    "success": "finished"	
}
```

失败回传失败标识符和原因例如（用户名已存在...）

```json
{
	"error": "registered"
}
```

### 上传简历

post传参

```
http://127.0.0.1:8000/usercenter/loadinfo/
```

```json
{
    "token":"123",
    "id";"123",
    "conList":[{"word":""},...]
}
```

成功回传成功标识符

```json
{
	"success": "ok"
}
```

失败回传失败标识符

```json
{
	"error": "worker existed"
}

{
    "error":"user token not existed"
}
```



### 上传文本岗位

post传参

```
http://127.0.0.1:8000/usercenter/addworkneed/
```

```json
{
    "jname": "123",         # 工作名称
    "jneed_age": 123,       # 年龄要求 25表示25岁以上 -25 表示25岁以下
    "jneed_edu": "123",     # 教育要求
    "jneed_year": "123",    # 工作经验
    "jneed_other": "123",   # 其他所有的要求
}
```

成功回传成功标识符

失败回传失败标识符

### 查询某用户上传的所有简历（分页）

post传参

```
http://127.0.0.1:8000/analysis/loadallinfo/
```

```json
{
    "token":"123",
	"page":1
}
```

成功回传(一页十个即可)

```json
{
    content:[
        {
            "id":"简历id",
        	"name":"123",
        	"sex":"男",
        	"age":"123",
        	"education":"123",
        	"college":"123",
        },
        {
            "id":"简历id",
        	"name":"123",
        	"sex":"男",
        	"age":"123",
        	"education":"123",
        	"college":"123",
        },
    ]
}
```

失败回传失败标识符

```json
{
	"error": "workers not existed"
}
```

### 关键词查询简历

post传参

```
http://127.0.0.1:8000/analysis/loadnameinfo/
```

```json
{
    "token":"123",
	"key":"暂定简历姓名"
}
```

成功回传(不分页)

```json
{
    content:[
        {
            "id":"简历id",
        	"name":"123",
        	"sex":"男",
        	"age":"123",
        	"education":"123",
        	"college":"123",
        },
        {
            "id":"简历id",
        	"name":"123",
        	"sex":"男",
        	"age":"123",
        	"education":"123",
        	"college":"123",
        },
    ]
}
```

失败回传失败标识符

```json
{
	"error": "worker not existed"
}
```

### 根据id查询岗位

post传参

```
http://127.0.0.1:8000/analysis/loadonejob/
```

```json
{
    "token":"123",
	"id":"123",
}
```

成功回传

```json
{
    "jname": "123",         # 工作名称
    "jneed_age": 123,       # 年龄要求 25表示25岁以上 -25 表示25岁以下
    "jneed_edu": "123",     # 教育要求
    "jneed_year": "123",    # 工作经验
    "jneed_other": "123",   # 其他所有的要求
}
```

失败返回

```json
{
	"error": "job not found"
}
```

### 查询所有岗位及其id

post传参

```
http://127.0.0.1:8000/analysis/loadalljob/
```

```json
{
    "token":"123"
}
```

成功回传

```json
{
    "content":
    [
        {
            "id": "id",
            "job_name": "name"
        },
        {
            "id": "id",
            "job_name": "name"
        }
    ]
}
```

### 根据id列表查询所有简历信息（分页）

post传参

```
http://127.0.0.1:8000/analysis/loadidinfo/
```

```json
{
	"content": [123, 11, 0...],
     "page": 1
}
```

成功回传(一页十个即可)

```json
{
    "content":
    [
        {
            "fileid": worker.fileid,
            "worker_name": worker.worker_name,
            "sex": worker.sex,
            "age": worker.age,
            "phone_number": worker.phone_number,
            "e_mail": worker.e_mail,
            "location": worker.location,
            "edu_school": worker.edu_school,
            "edu_level": worker.edu_level,
            "work_year": worker.work_year,
            "statue": worker.statue,
            "hash_code": worker.hash_code
        },
        {
            "fileid": worker.fileid,
            "worker_name": worker.worker_name,
            "sex": worker.sex,
            "age": worker.age,
            "phone_number": worker.phone_number,
            "e_mail": worker.e_mail,
            "location": worker.location,
            "edu_school": worker.edu_school,
            "edu_level": worker.edu_level,
            "work_year": worker.work_year,
            "statue": worker.statue,
            "hash_code": worker.hash_code
        }
    ]
}
```

### 根据id查询简历可信度

post传参

```
http://127.0.0.1:8000/analysis/loadscore/
```

```json
{
	"token":"token"
	"id":"id"
}
```

成功回传

```json
{
	"score":19.19
}
```

失败返回

```json
{
	"error": "user token not existed"
}
```

