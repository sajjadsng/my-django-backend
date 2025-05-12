# راهنمای استفاده از API برای فرانت‌اند

## آدرس مستندات (Swagger)

- [Swagger UI](http://127.0.0.1:8000/swagger/)
- [ReDoc](http://127.0.0.1:8000/redoc/)
- [Swagger JSON](http://127.0.0.1:8000/swagger.json)

---

## لیست Endpoints مهم

### ثبت‌نام (Register)
```
POST /api/users/
Content-Type: application/json

{
  "email": "test@example.com",
  "username": "test",
  "password": "test123456",
  "role": "employee" // یا "admin"
}
```

### لاگین (Login)
```
POST /api/login/
Content-Type: application/json

{
  "email": "test@example.com",
  "password": "test123456"
}
```
پاسخ:
```
{
  "access": "...",
  "refresh": "...",
  "user": {
    "id": 1,
    "email": "test@example.com",
    "username": "test"
  }
}
```

### دریافت توکن جدید (Refresh Token)
```
POST /api/token/refresh/
Content-Type: application/json

{
  "refresh": "..."
}
```

### لاگ‌اوت (Logout)
```
POST /api/logout/
Content-Type: application/json
Authorization: Bearer <access_token>

{
  "refresh": "..."
}
```

### نمونه درخواست با fetch (جاوااسکریپت)
```js
// لاگین
fetch('http://127.0.0.1:8000/api/login/', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ email: 'test@example.com', password: 'test123456' })
})
  .then(res => res.json())
  .then(data => {
    // data.access و data.refresh را ذخیره کن
  });

// درخواست محافظت‌شده
fetch('http://127.0.0.1:8000/api/users/', {
  headers: { 'Authorization': 'Bearer <access_token>' }
})
  .then(res => res.json())
  .then(data => console.log(data));
```

---

## نکات مهم
- برای همه درخواست‌های محافظت‌شده، هدر Authorization را به صورت `Bearer <access_token>` بفرستید.
- همه ورودی‌ها و خروجی‌ها در Swagger UI قابل مشاهده و تست است.
- اگر پروژه روی سرور است، آدرس را جایگزین localhost کنید.
- اگر سوالی بود، با بک‌اند تماس بگیرید! 