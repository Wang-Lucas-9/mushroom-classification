Note để đọc cái này đẹp thì ae dùng cái extension e gửi kèm (image.png) hoặc đọc trên github

**Hướng dẫn quy trình làm việc với Git**

### 1. Kiểm tra trạng thái của repository
Chạy lệnh sau để xem những thay đổi trong repository:
```bash
git status
```

### 2. Thêm file vào staging area
- Thêm tất cả các file đã thay đổi:
```bash
git add .
```
- Thêm file cụ thể:
```bash
git add <filename>
```

### 3. Commit thay đổi
Commit thay đổi với mô tả ngắn gọn:
```bash
git commit -m "Mô tả thay đổi"
```
**Ví dụ:**
- `git commit -m "Thêm chức năng trích xuất màu"`
- `git commit -m "Sửa lỗi khi đọc ảnh"`

### 4. Push code lên GitHub
- Nếu branch đã thiết lập upstream:
```bash
git push
```
- Nếu lần đầu push branch này:
```bash
git push --set-upstream origin main
```

### 5. Kết hợp với code mới nhất
Trước khi push, nên cập nhật code từ GitHub:
```bash
git pull
```

### Tóm tắt quy trình chuẩn
```bash
git status  
git add .  
git commit -m "Mô tả thay đổi"  
git push  
```



